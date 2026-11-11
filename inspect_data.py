import json

with open(/data/workspace/yanmy/SR_Demo_Review/dist/data/formula_1.json) as f:
    d = json.load(f)

o = d.get(ontology, {})
print(Objects count:, len(o.get(objects, [])))
print(Edges count:, len(o.get(edges, [])))
print(Tables count:, len(o.get(tables, [])))

kinds = set(x.get(kind) for x in o.get(objects, []))
print(Object kinds:, kinds)

for k in kinds:
    sample = next((x for x in o.get(objects, []) if x.get(kind) == k), None)
    print(fSample of kind  -encodedCommand awA= :, json.dumps(sample, indent=2, ensure_ascii=False)[:300])

print(Sample edges:, json.dumps(o.get(edges, [])[:3], indent=2, ensure_ascii=False))
