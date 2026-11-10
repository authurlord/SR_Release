from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from threading import Lock
import time
from typing import Any

import httpx
from json_repair import loads as repair_json_loads


class TokenBudgetExceeded(RuntimeError):
    """Raised before a request whose conservative bound exceeds the run cap."""


def decode_json_content(content: str) -> tuple[dict[str, Any], bool]:
    try:
        value = json.loads(content)
        repaired = False
    except json.JSONDecodeError:
        value = repair_json_loads(content)
        repaired = True
    if isinstance(value, list) and len(value) == 1 and isinstance(value[0], dict):
        value = value[0]
        repaired = True
    if not isinstance(value, dict):
        raise ValueError("structured model response must decode to a JSON object")
    return value, repaired


class VLLMClient:
    def __init__(self, config: dict[str, Any]):
        self.base_url = config["base_url"].rstrip("/")
        self.api_key = config["api_key"]
        self.model = config["model"]
        self.temperature = config.get("temperature", 0.0)
        self.top_p = config.get("top_p", 1.0)
        self.max_tokens = config.get("max_output_tokens", 2048)
        self.request_timeout_seconds = float(
            config.get("request_timeout_seconds", 180)
        )
        if self.request_timeout_seconds <= 0:
            raise ValueError("llm.request_timeout_seconds must be positive")
        self.compatibility = str(config.get("compatibility", "vllm"))
        if self.compatibility not in {"vllm", "deepseek_v4"}:
            raise ValueError(f"unsupported LLM compatibility mode: {self.compatibility}")
        self.thinking = config.get("thinking")
        if self.thinking not in {None, "enabled", "disabled"}:
            raise ValueError("llm.thinking must be enabled, disabled, or omitted")
        self.reasoning_effort = config.get("reasoning_effort")
        if self.reasoning_effort not in {None, "high", "max"}:
            raise ValueError("llm.reasoning_effort must be high, max, or omitted")
        self.provider = config.get("provider")
        self.release_label = config.get("release_label")
        self.require_exact_model = bool(config.get("require_exact_model", False))
        audit_log_path = config.get("audit_log_path")
        self.audit_log_path = Path(audit_log_path) if audit_log_path else None
        self._audit_lock = Lock()
        token_cap = config.get("max_total_tokens")
        self.max_total_tokens = int(token_cap) if token_cap is not None else None
        if self.max_total_tokens is not None and self.max_total_tokens < 1:
            raise ValueError("llm.max_total_tokens must be positive when supplied")
        if self.max_total_tokens is not None and self.audit_log_path is None:
            raise ValueError(
                "llm.max_total_tokens requires audit_log_path for cumulative accounting"
            )
        self._budget_lock = Lock()
        self._budget_charged_tokens = self._load_budget_charges()
        self._budget_reserved_tokens = 0

    def healthy(self) -> bool:
        try:
            response = httpx.get(
                f"{self.base_url}/models",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=3,
                trust_env=False,
            )
            return response.status_code == 200
        except httpx.HTTPError:
            return False

    def chat_json(self, system: str, user: str) -> dict[str, Any]:
        payload, _ = self.chat_json_with_metadata(system, user)
        return payload

    def chat_json_with_metadata(
        self, system: str, user: str
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        response_payload = self._chat_completion(system, user, json_mode=True)
        content = str(response_payload["choices"][0]["message"]["content"])
        value, repaired = decode_json_content(content)
        usage = self._usage_metadata(response_payload)
        usage["json_repaired"] = repaired
        return value, usage

    def chat_text_with_metadata(
        self, system: str, user: str
    ) -> tuple[str, dict[str, Any]]:
        response_payload = self._chat_completion(system, user, json_mode=False)
        content = response_payload["choices"][0]["message"]["content"]
        return str(content), self._usage_metadata(response_payload)

    def _chat_completion(
        self, system: str, user: str, *, json_mode: bool
    ) -> dict[str, Any]:
        request = self._request_payload(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        if json_mode:
            request["response_format"] = {"type": "json_object"}
        return self._post_chat_completion(request)

    def _request_payload(
        self,
        *,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        tool_choice: str | dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        request: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "max_tokens": self.max_tokens,
        }
        if self.compatibility == "vllm":
            request.update(
                {
                    "temperature": self.temperature,
                    "top_p": self.top_p,
                    # vLLM otherwise inherits Qwen's sampling-oriented
                    # generation_config (top_k=20), even at temperature zero.
                    "top_k": -1,
                    "chat_template_kwargs": {
                        "enable_thinking": self.thinking == "enabled"
                    },
                }
            )
        else:
            if self.thinking is not None:
                request["thinking"] = {"type": self.thinking}
            # DeepSeek documents sampling parameters as ineffective in thinking mode.
            # Omitting them also keeps the frozen request semantically unambiguous.
            if self.thinking != "enabled":
                request["temperature"] = self.temperature
                request["top_p"] = self.top_p
            if self.reasoning_effort is not None and self.thinking == "enabled":
                request["reasoning_effort"] = self.reasoning_effort
        if tools is not None:
            request["tools"] = tools
        # DeepSeek V4 thinking mode rejects tool_choice. Its absence means auto.
        if tool_choice is not None and not (
            self.compatibility == "deepseek_v4" and self.thinking == "enabled"
        ):
            request["tool_choice"] = tool_choice
        return request

    def _context_length_retry_max_tokens(
        self, request: dict[str, Any], response: httpx.Response
    ) -> int | None:
        """Return the exact valid output reserve for one explicit vLLM retry.

        vLLM rejects a request before generation when prompt tokens plus the
        requested output reserve exceed the model window.  Its error only gives
        a lower bound for prompt length, so use the same server's tokenizer HTTP
        endpoint to count the identical messages and tools exactly.  Retrying
        once with only the output ceiling reduced is a transport correction: it
        does not alter messages, tools, sampling, or the method trajectory.
        """

        if response.status_code != 400 or self.compatibility != "vllm":
            return None
        try:
            payload = response.json()
        except (json.JSONDecodeError, ValueError):
            return None
        if not isinstance(payload, dict):
            return None
        error = payload.get("error")
        if not isinstance(error, dict):
            return None
        message = str(error.get("message") or "")
        context_match = re.search(
            r"maximum context length is\s+([\d,]+)\s+tokens", message, re.IGNORECASE
        )
        prompt_match = re.search(
            r"prompt contains at least\s+([\d,]+)\s+input tokens",
            message,
            re.IGNORECASE,
        )
        requested = request.get("max_tokens")
        if (
            context_match is None
            or prompt_match is None
            or not isinstance(requested, int)
        ):
            return None
        tokenize_request = {
            key: request[key]
            for key in (
                "model",
                "messages",
                "tools",
                "chat_template",
                "chat_template_kwargs",
                "add_generation_prompt",
                "continue_final_message",
                "add_special_tokens",
                "mm_processor_kwargs",
                "media_io_kwargs",
            )
            if key in request
        }
        tokenize_base = (
            self.base_url[: -len("/v1")]
            if self.base_url.endswith("/v1")
            else self.base_url
        )
        try:
            tokenize_response = httpx.post(
                f"{tokenize_base}/tokenize",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json=tokenize_request,
                timeout=self.request_timeout_seconds,
                trust_env=False,
            )
            tokenize_response.raise_for_status()
            tokenize_payload = tokenize_response.json()
        except (httpx.HTTPError, json.JSONDecodeError, ValueError):
            return None
        if not isinstance(tokenize_payload, dict):
            return None
        prompt_tokens = tokenize_payload.get("count")
        context_tokens = tokenize_payload.get("max_model_len")
        if not isinstance(prompt_tokens, int) or not isinstance(context_tokens, int):
            return None
        error_context_tokens = int(context_match.group(1).replace(",", ""))
        if context_tokens != error_context_tokens:
            return None
        available = context_tokens - prompt_tokens
        if available < 1 or available >= requested:
            return None
        return available

    def _post_chat_completion(self, request: dict[str, Any]) -> dict[str, Any]:
        try:
            return self._post_chat_completion_once(request)
        except httpx.HTTPStatusError as error:
            retry_max_tokens = self._context_length_retry_max_tokens(
                request, error.response
            )
            if retry_max_tokens is None:
                raise
        retry_request = dict(request)
        retry_request["max_tokens"] = retry_max_tokens
        return self._post_chat_completion_once(retry_request)

    def _post_chat_completion_once(self, request: dict[str, Any]) -> dict[str, Any]:
        started = time.perf_counter()
        reservation = self._reserve_token_bound(request)
        try:
            response = httpx.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json=request,
                timeout=self.request_timeout_seconds,
                trust_env=False,
            )
        except Exception as error:
            budget = self._settle_token_bound(reservation, None)
            self._write_audit_record(
                request=request,
                response_payload={"transport_error": type(error).__name__},
                http_status=0,
                latency_seconds=time.perf_counter() - started,
                budget=budget,
            )
            raise
        try:
            response_payload: Any = response.json()
        except (json.JSONDecodeError, ValueError):
            response_payload = {
                "non_json_body_sha256": hashlib.sha256(response.content).hexdigest()
            }
        budget = self._settle_token_bound(reservation, response_payload)
        self._write_audit_record(
            request=request,
            response_payload=response_payload,
            http_status=response.status_code,
            latency_seconds=time.perf_counter() - started,
            budget=budget,
        )
        response.raise_for_status()
        if not isinstance(response_payload, dict):
            raise ValueError("chat completion response must decode to a JSON object")
        returned_model = response_payload.get("model")
        if self.require_exact_model and returned_model != self.model:
            raise ValueError(
                "provider returned a different model: "
                f"requested={self.model!r}, returned={returned_model!r}"
            )
        return response_payload

    @staticmethod
    def _request_token_upper_bound(request: dict[str, Any]) -> int:
        """Conservative bound: UTF-8 input bytes plus requested output tokens."""

        encoded = json.dumps(
            request, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        max_output = request.get("max_tokens", 0)
        if not isinstance(max_output, int) or max_output < 0:
            raise ValueError("request max_tokens must be a nonnegative integer")
        # A tokenizer cannot emit more input tokens than input bytes.  Reserving
        # every byte as one token plus the full output limit therefore prevents
        # concurrent calls from crossing the cap even before provider usage lands.
        return len(encoded) + max_output

    def _load_budget_charges(self) -> int:
        if self.max_total_tokens is None or self.audit_log_path is None:
            return 0
        if not self.audit_log_path.is_file():
            return 0
        charged = 0
        with self.audit_log_path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as error:
                    raise ValueError(
                        f"invalid token audit JSONL at line {line_number}"
                    ) from error
                budget_charge = row.get("budget", {}).get("charged_tokens")
                if isinstance(budget_charge, int) and budget_charge >= 0:
                    charged += budget_charge
                    continue
                usage_total = row.get("response", {}).get("usage", {}).get(
                    "total_tokens"
                )
                if isinstance(usage_total, int) and usage_total >= 0:
                    charged += usage_total
                else:
                    charged += self._request_token_upper_bound(row["request"])
        if charged > self.max_total_tokens:
            raise TokenBudgetExceeded(
                f"existing audit usage {charged} exceeds cap {self.max_total_tokens}"
            )
        return charged

    def _reserve_token_bound(self, request: dict[str, Any]) -> int | None:
        if self.max_total_tokens is None:
            return None
        upper_bound = self._request_token_upper_bound(request)
        with self._budget_lock:
            projected = (
                self._budget_charged_tokens
                + self._budget_reserved_tokens
                + upper_bound
            )
            if projected > self.max_total_tokens:
                raise TokenBudgetExceeded(
                    "request blocked before dispatch: conservative cumulative token "
                    f"bound {projected} exceeds cap {self.max_total_tokens}"
                )
            self._budget_reserved_tokens += upper_bound
        return upper_bound

    def _settle_token_bound(
        self, reservation: int | None, response_payload: Any
    ) -> dict[str, Any] | None:
        if reservation is None or self.max_total_tokens is None:
            return None
        usage_total = None
        if isinstance(response_payload, dict):
            value = response_payload.get("usage", {}).get("total_tokens")
            if isinstance(value, int) and value >= 0:
                usage_total = value
        charged = usage_total if usage_total is not None else reservation
        if charged > reservation:
            # Provider usage outside the pre-dispatch upper bound is unsafe.  It is
            # still fully charged and the run fails closed on its next call.
            charged = int(charged)
        with self._budget_lock:
            self._budget_reserved_tokens -= reservation
            self._budget_charged_tokens += charged
            cumulative = self._budget_charged_tokens
        return {
            "charged_tokens": charged,
            "charge_source": "provider_usage" if usage_total is not None else "upper_bound",
            "request_upper_bound_tokens": reservation,
            "cumulative_charged_tokens": cumulative,
            "max_total_tokens": self.max_total_tokens,
        }

    def token_budget_status(self) -> dict[str, int | None]:
        with self._budget_lock:
            return {
                "charged_tokens": self._budget_charged_tokens,
                "reserved_tokens": self._budget_reserved_tokens,
                "max_total_tokens": self.max_total_tokens,
                "remaining_tokens": (
                    None
                    if self.max_total_tokens is None
                    else self.max_total_tokens
                    - self._budget_charged_tokens
                    - self._budget_reserved_tokens
                ),
            }

    def _write_audit_record(
        self,
        *,
        request: dict[str, Any],
        response_payload: Any,
        http_status: int,
        latency_seconds: float,
        budget: dict[str, Any] | None = None,
    ) -> None:
        if self.audit_log_path is None:
            return
        request_json = json.dumps(
            request, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        response_json = json.dumps(
            response_payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        record = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "endpoint": f"{self.base_url}/chat/completions",
            "provider": self.provider,
            "release_label": self.release_label,
            "requested_model": self.model,
            "http_status": http_status,
            "latency_seconds": round(latency_seconds, 6),
            "request_sha256": hashlib.sha256(request_json.encode()).hexdigest(),
            "response_sha256": hashlib.sha256(response_json.encode()).hexdigest(),
            # The audit log deliberately contains the public-benchmark prompts and
            # response bodies, but never request headers or the API credential.
            "request": request,
            "response": response_payload,
        }
        if budget is not None:
            record["budget"] = budget
        self.audit_log_path.parent.mkdir(parents=True, exist_ok=True)
        with self._audit_lock, self.audit_log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    def _usage_metadata(self, response_payload: dict[str, Any]) -> dict[str, Any]:
        usage = response_payload.get("usage", {})
        return {
            "provider": self.provider,
            "release_label": self.release_label,
            "requested_model": self.model,
            "model": response_payload.get("model", self.model),
            "system_fingerprint": response_payload.get("system_fingerprint"),
            "response_id": response_payload.get("id"),
            "created": response_payload.get("created"),
            "prompt_tokens": usage.get("prompt_tokens"),
            "completion_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
        }

    def chat_tools(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]],
        tool_choice: str | dict[str, Any] = "auto",
    ) -> dict[str, Any]:
        """Call an OpenAI-compatible model with native function tools."""
        request = self._request_payload(
            messages=messages,
            tools=tools,
            tool_choice=tool_choice,
        )
        return self._post_chat_completion(request)
