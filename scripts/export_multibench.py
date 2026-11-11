#!/usr/bin/env python3
"""Read saved input/ontology/query artifacts into dataset-separated review assets."""
import gzip,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist';M=ROOT.parent/'SchemaRecovery';R=ROOT.parent/'SchemaRecovery-section16-20261026'
A=R/'handoff_live/ontology_appendix_20261107/SchemaRecovery_MainTable_Ontology_Appendix_20261107'
sys.path[:0]=[str(ROOT.parent/'SR_Release/src'),str(ROOT)]
from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
from finsemguard.ontology_discovery.dependency_update import update_layer
from finsemguard.e2e.operational_ontology import OperationalOntology
from native_adapter import physical_catalog

def load(p):
 p=Path(p)
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:
  return json.load(f) if '.jsonl' not in p.name else [json.loads(l) for l in f if l.strip()]
def out(p,d):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,separators=(',',':')))
def slug(s):return re.sub(r'[^A-Za-z0-9_-]','-',s)
def first(p,limit=1):
 rows=load(p);return [x for x in rows if x.get('sql') and x.get('react')][:limit]
def digest(v):return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()[:20]
manifest=load(A/'SOURCE_MANIFEST.json')
def src(dataset,role):return next((Path(x['source_path']) for x in manifest if x['dataset']==dataset and x['role']==role),None)
allcatalog=load(DIST/'data/catalog.json');history_group={'id':'BIRD-History','label':'BIRD-History','databases':allcatalog['databases']}
groups=[history_group];allcases=[c for c in allcatalog['cases'] if c.get('dataset','BIRD-History')=='BIRD-History'];summary=[]

# Genuine native generation records, selected by saved order rather than score.
selection={
 'BIRD-Dev':first(ROOT.parent/'SchemaRecovery-maintenance-20261008/results/v16_iteration_20261009/bird_dev1534_v15_v16_20261009/v15/local/predictions/graph_evo_semantic_program_main_v1.jsonl',2),
 'BIRD-Mini':first(M/'results/v15_crossbench_20261007/bird/full/main/graph_evo_semantic_program_main_v1.jsonl',2),
 'KaggleDBQA':first(M/'results/v15_crossbench_20261007/kaggledbqa/full/main/graph_evo_semantic_program_main_v1.jsonl',2),
 'FIBEN':first(M/'results/v15_crossbench_20261007/fiben/full/main/graph_evo_semantic_program_main_v1.jsonl',2),
 'EvoSchema':first(M/'results/v15_crossbench_20261007/evoschema/full/main/graph_evo_semantic_program_main_v1.jsonl',2),
 'BEAVER':[], 'Spider2-Lite':[]}
beaverbase=R/'results/sr_beaver_opt_20261105/native_v17_first1_phase3_v1'
for db in ['neutron','nova','dw']:
 paths=sorted((beaverbase/'runs/native_sr_opt_v1/B3'/db).glob('*/native_full.json'))
 if paths:
  d=load(paths[0]);d['_demo_source']=str(paths[0]);selection['BEAVER'].append(d)
spiderbase=R/'results/exp_multibench_20261104/spider2_v17_opt_20261108'
for identity in ['local002','local009']:
 p=spiderbase/'questions'/identity/'v17.json'
 if p.exists():
  d=load(p);d['_demo_source']=str(p);selection['Spider2-Lite'].append(d)

for dataset in ['BIRD-Dev','BIRD-Mini','KaggleDBQA','FIBEN','EvoSchema','BEAVER','Spider2-Lite']:
 source_dataset='BIRD-Dev-and-Mini' if dataset.startswith('BIRD-') else dataset
 bundle=load(A/'datasets'/source_dataset/'ONTOLOGY.json') if source_dataset!='Spider2-Lite' else None
 inputs_path=src(source_dataset,'table_inputs');inputs=load(inputs_path) if inputs_path else []
 recovery_path=src(source_dataset,'table_recovery');recovery=load(recovery_path) if recovery_path else []
 state_path=src(source_dataset,'semantic_state');state=load(state_path) if state_path else None
 if dataset=='EvoSchema':contexts=sorted({d['database_id'] for d in selection[dataset]})
 elif dataset=='Spider2-Lite':contexts=sorted({d['database_id'] for d in selection[dataset]})
 else:contexts=sorted({row['schema_context'] for row in inputs})
 entries=[]
 for context in contexts:
  dbinputs=[row for row in inputs if row['schema_context']==context]
  dbrecovery=[row for row in recovery if row['input_id'] in {t['input_id'] for t in dbinputs}]
  sources=[];objects=[];edges=[];maintenance=[]
  if state:
   records={k:v for k,v in state['records'].items() if v['schema_context']==context};layer=WorkloadSemanticLayer(records,state['revision']);objects=layer.objects();sources=[{'evidence_id':'sql_log::'+k,**row} for k,row in records.items()]
  if dataset=='EvoSchema':
   tables=[t for t in bundle['tables'] if t['context']==context];cols=[c for c in bundle['columns'] if c['context']==context]
   dbinputs=[{'input_id':'current_schema::'+context+'::'+t['physical_table'],'schema_context':context,'physical_table':t['physical_table'],'columns':[{'physical_column':c['physical_column'],'declared_type':c.get('declared_type','unknown'),'observed_values':[],'primary_key':c.get('primary_key',False)} for c in cols if c['physical_table']==t['physical_table']],'relationships':[],'target_disjoint_workload':[]} for t in tables]
   # Preserve current physical names and actual released lineage; no recovered names are inserted.
  if dataset=='Spider2-Lite':
   dbmap=load(spiderbase/'databases.json');dbinputs,_=physical_catalog(dbmap[context],context)
  if not sources:
   history={}
   for table in dbinputs:
    for h in table.get('target_disjoint_workload',[]):
     key=h.get('evidence_id') or h.get('history_id') or digest(h['sql'])
     history.setdefault(key,{'history_id':h.get('history_id',key),'evidence_id':key,'sql':h['sql'],'schema_context':context,'facts':[],'source_kind':'saved_historical_sql'})
   sources=list(history.values())
   recovered_by_table={row['prediction']['physical_table']:row['prediction'] for row in dbrecovery}
   for table in dbinputs:
    rec=recovered_by_table.get(table['physical_table'],{})
    rec_cols={c['physical_column']:c for c in rec.get('columns',[])}
    if not sources:
     pass
    fallback_id='schema::'+context+'::'+table['physical_table']
    if True:
     sources.append({'history_id':'schema / '+table['physical_table'],'evidence_id':fallback_id,'schema_context':context,'source_kind':'saved_physical_schema','sql':'CREATE TABLE "'+table['physical_table']+'" (\n'+',\n'.join('  "'+c['physical_column']+'" '+(c.get('declared_type') or 'unknown') for c in table['columns'])+'\n);','facts':[]})
    for column in table['columns']:
     p=table['physical_table']+'.'+column['physical_column'];rec_col=rec_cols.get(column['physical_column'],{})
     evidence=[h.get('evidence_id') or h.get('history_id') or digest(h['sql']) for h in table.get('target_disjoint_workload',[]) if column['physical_column'] in h.get('physical_columns',[])]
     if not evidence:evidence=[fallback_id] if any(s['evidence_id']==fallback_id for s in sources) else [h['evidence_id'] for h in sources if h.get('history_id') in column.get('history_ids',[])][:5]
     obj={'id':'recovery_column::'+context+'::'+table['physical_table']+'::'+column['physical_column'],'schema_context':context,'kind':'column','physical_identifiers':[p],'physical_tables':[table['physical_table']],'expression':'"'+table['physical_table']+'"."'+column['physical_column']+'"','roles':rec_col.get('query_phrases',[]),'aliases':rec_col.get('aliases',[]),'evidence_ids':evidence,'source_kind':'saved_recovery_prediction' if rec_col else 'released_physical_schema'};objects.append(obj)
     for source in sources:
      if source['evidence_id'] in evidence:source['facts'].append(obj)
   if dataset=='EvoSchema':
    for fact in [f for f in bundle['facts'] if f.get('context')==context]:
     obj={'id':'lineage::'+digest(fact),'kind':'binding','schema_context':context,'physical_identifiers':[fact.get('physical_table','')+'.'+fact.get('physical_column','')],'physical_tables':[fact.get('physical_table','')],'expression':json.dumps(fact),'aliases':[],'evidence_ids':[sources[0]['evidence_id']] if sources else [],'source_kind':'released_evolution_lineage'};objects.append(obj)
     if sources:sources[0]['facts'].append(obj)
  try:edges=[e.as_dict() for e in OperationalOntology.from_recovery_inputs(dbinputs,[]).edges]
  except ValueError:pass
  # Add preserved business knowledge as separate native evidence records when present.
  knowledge_path=src(source_dataset,'knowledge')
  knowledge=load(knowledge_path) if knowledge_path and knowledge_path.exists() else []
  for k in knowledge:
   ctx=str(k.get('schema_context') or k.get('database_id') or k.get('db_id') or '')
   if ctx!=context:continue
   obj={'id':str(k.get('knowledge_id') or k.get('id') or 'kb::'+digest(k)),'schema_context':context,'kind':'metric','aliases':k.get('aliases') or [str(k.get('name') or k.get('knowledge') or 'Business definition')],'expression':k.get('definition') or k.get('description') or json.dumps(k),'physical_identifiers':k.get('physical_columns',[]) or ([k['physical_identifier']] if k.get('physical_identifier') else []),'physical_tables':[],'evidence_ids':[],'source_kind':'saved_business_knowledge'};objects.append(obj)
   source_id=str(k.get('evidence_id') or obj['id']);obj['evidence_ids']=[source_id];sources.append({'history_id':source_id,'evidence_id':source_id,'sql':str(obj['expression']),'facts':[obj],'schema_context':context,'source_kind':'saved_business_knowledge'})
  cases=[]
  for pred in selection[dataset]:
   if pred['database_id']!=context:continue
   question=pred.get('question') or pred.get('react',{}).get('initial_search_query') or pred.get('react',{}).get('initial_search',{}).get('query')
   if not question:continue
   identity=pred['example_id'];file='data/'+slug(dataset)+'/cases/'+slug(identity)+'.json'
   case={'id':identity,'origin':'archive','title':question[:75],'database':context,'question':question,'dataset':dataset,'provenance':{'archive':'Saved native SR run','source':pred.pop('_demo_source',str(M/'results/v15_crossbench_20261007'))},'prediction':pred}
   # Cases use their database bundle at load time; avoid duplicating large ontology JSON.
   out(DIST/file,case);cases.append({k:case[k] for k in ['id','origin','title','database','question','dataset']}|{'path':file});allcases.append(cases[-1])
  if state and sources:
   from copy import deepcopy
   records={key:row for key,row in state['records'].items() if row['schema_context']==context}
   if records:
    _,h=next(iter(records.items()));after,receipt=update_layer(WorkloadSemanticLayer(deepcopy(records),state['revision']),objects,[],retract=((context,h['history_id']),))
    new={o['id']:o for o in after};changes=[{'physical_identifiers':o['physical_identifiers'],'before':o.get('aliases',[]),'after':new.get(o['id'],{}).get('aliases',[]),'status':'updated' if o['id'] in new else 'removed'} for o in objects if o['kind']=='column' and o!=new.get(o['id'])]
    maintenance=[{'title':'Source withdrawal preview · '+h['history_id'],'event_type':'source_withdrawal_preview_on_copy','source':'Review event: withdraw this saved source on a copied ontology','method':'dependency_update.update_layer','model_calls':0,'receipt':receipt,'column_changes':changes,'source_sql':h['sql']}]
  path='data/'+slug(dataset)+'/'+slug(context)+'.json';data={'database':context,'dataset':dataset,'provenance':{'archive':'Saved SR input and ontology artifacts','input_source':str(inputs_path or source_dataset),'ontology_source':str(A/'datasets'/source_dataset)},'ontology':{'sources':sources,'objects':objects,'tables':dbinputs,'recovery':dbrecovery,'edges':edges,'construct':[]},'maintenance':maintenance,'cases':cases}
  out(DIST/path,data);entries.append({'id':context,'path':path,'sources':len(sources),'objects':len(objects),'columns':sum(len(t['columns']) for t in dbinputs),'cases':cases})
 groups.append({'id':dataset,'label':dataset,'databases':entries});summary.append({'dataset':dataset,'databases':len(entries),'cases':sum(len(x['cases']) for x in entries)});print(summary[-1],flush=True)
out(DIST/'data/catalog.json',{**allcatalog,'datasets':groups,'cases':allcases})
out(DIST/'data/dataset-coverage.json',summary)
