"""Construct the main method's semantic assets from the released history pool.

Only historical SQL enters construction. Target questions, target SQL and BIRD
evidence strings are excluded. LLM labels augment immutable parsed computations.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import argparse
import json
from pathlib import Path
import time

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer, extract_sql_evidence

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'results/bird_history_main_20261002'
PROMPT = '''Interpret a past SQL computation to build reusable semantic assets.
Only this past SQL and its parsed objects are evidence. There is no current user
question. Preserve relation roles, filters, formulas and aggregation stages.
Return JSON {"objects":[{"id":"copy supplied object id", "label":"concise
business or structural role", "description":"what this computation returns,
including its population and grain"}]}. Include useful metric, binding and full
program objects. Names are hypotheses grounded in actual SQL identifiers, aliases,
literals and usage; avoid inventing business definitions or units. Do not rewrite
SQL. Use the same language as the identifiers, generally English. Distinguish
self-join roles and conditional metrics. Descriptions must support future reuse.
'''


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n');tmp.replace(path)


def main():
    global OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-root', type=Path, default=OUT)
    parser.add_argument('--history', type=Path)
    args = parser.parse_args()
    OUT = args.output_root.resolve()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.history:
        history=[json.loads(s) for s in args.history.read_text().splitlines() if s.strip()]
        allowed = {'history_id', 'database_id', 'schema_context', 'sql', 'dialect'}
        if any(set(r) - allowed for r in history):
            raise ValueError('History input must contain SQL and source identity only')
    else:
        raw=json.loads((ROOT/'data/raw/bird_full_dev/dev.json').read_text())
        history=[{'history_id':f"bird_dev:{r['question_id']}", 'database_id':r['db_id'],
              'schema_context':r['db_id'], 'sql':r['SQL'], 'dialect':'sqlite'} for r in raw]
    assert len(history)==1534 and len({r['history_id'] for r in history})==1534
    (OUT/'history_sql_only.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in history))
    write(OUT/'BUILD_PROTOCOL.json', {'history_records':len(history),'databases':11,
        'view':'prepared SQL history' if args.history else 'author named-schema reference',
        'source':str(args.history) if args.history else 'data/raw/bird_full_dev/dev.json',
        'fields_exposed':['SQL','db_id','question_id as source identity'],
        'target_data_exposed':False,'historical_nl_and_evidence_exposed':False,
        'main_change':'SQL-derived role and computation interpretations enter persistent assets before query generation',
        'concurrency':8,'max_output_tokens':2500,'started_unix':time.time(),
        'prompt_sha256':sha256(PROMPT.encode()).hexdigest()})
    cfg=load_config(ROOT/'configs/experiments/qwen38_27b_fp8_balanced_20261002.yaml')['llm']
    cfg['max_output_tokens']=2500
    started=time.time()
    def run(row):
        target=OUT/'construction'/f"{row['history_id'].replace(':','_')}.json"
        if target.exists():
            old=json.loads(target.read_text())
            if not old.get('error') and old.get('source_sql')==row['sql']:return old
        try:
            parsed=extract_sql_evidence(row['sql'],row['schema_context'],'sqlite')
            useful=[f for f in parsed['facts'] if f['kind'] in {'metric','binding','program'}]
            objects=[{k:v for k,v in f.items() if k in {'id','kind','expression','grain','aliases','roles','row_context'}} for f in useful]
            response,usage=VLLMClient(cfg).chat_json_with_metadata(PROMPT,json.dumps({'sql':row['sql'],'objects':objects},ensure_ascii=False))
            by_id={f['id']:f for f in parsed['facts']};annotations=[]
            for item in response.get('objects',[]):
                if not isinstance(item,dict) or item.get('id') not in by_id:continue
                label=str(item.get('label') or '').strip();description=str(item.get('description') or '').strip()
                if not label and not description:continue
                annotations.append({'id':item['id'],'label':label,'description':description})
                fact=by_id[item['id']]
                fact['aliases']=sorted(set(fact.get('aliases',[])) | {x for x in [label,description] if x})
                fact['interpretation_source']='llm_from_this_historical_sql_only'
            if useful and not annotations:raise ValueError('No supported object interpretations returned')
            result={**row,'source_sql':row['sql'],'parsed':parsed,'annotations':annotations,'usage':usage}
        except Exception as exc:result={**row,'source_sql':row['sql'],'error':str(exc)}
        write(target,result);return result
    done=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        for future in as_completed([pool.submit(run,r) for r in history]):
            done.append(future.result())
            errors=sum(bool(r.get('error')) for r in done)
            write(OUT/'construction_status.json',{'written':len(done),'target':len(history),'errors':errors,
                'updated_unix':time.time(),'elapsed_seconds':time.time()-started})
            print('history semantic construction',len(done),'/',len(history),'errors',errors,flush=True)
    if any(r.get('error') for r in done):raise RuntimeError('Construction errors saved; resume before downstream use')
    layer=WorkloadSemanticLayer()
    # Preserve the established source-key construction and canonical identities.
    layer.update(history)
    by_source={r['history_id']:r for r in done}
    for record in layer.records.values():
        record.update(by_source[record['history_id']]['parsed'])
    layer.save(OUT/'semantic_layer/state.json')
    inputs,recovery,_=layer.export_assets()
    for name,values in [('table_inputs.jsonl',inputs),('table_recovery.jsonl',recovery)]:
        (OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in values))
    write(OUT/'SEMANTICS_READY.json',{'records':len(history),'objects':len(layer.objects()),'finished_unix':time.time()})


if __name__=='__main__':main()
