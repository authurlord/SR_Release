#!/usr/bin/env python3
"""Export the fixed saved main populations; no inference, SQL execution or scoring."""
import gzip,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist';M=ROOT.parent/'SchemaRecovery';R=ROOT.parent/'SchemaRecovery-section16-20261026';F=ROOT.parent/'SchemaRecovery-r05-anchor-20261016'
DEV=ROOT.parent/'SchemaRecovery-maintenance-20261008/results/v16_iteration_20261009/bird_dev1534_v15_v16_20261009'
SPIDER=R/'results/exp_multibench_20261104/spider2_v17_opt_20261108';BEAVER=R/'results/sr_beaver_opt_20261105/native_v17_first1_phase3_v1'
A=R/'handoff_live/ontology_appendix_20261107/SchemaRecovery_MainTable_Ontology_Appendix_20261107'
def load(p):
 p=Path(p)
 with (gzip.open(p,'rt')if p.suffix=='.gz' else p.open())as f:return [json.loads(l)for l in f if l.strip()]if '.jsonl'in p.name else json.load(f)
def dump(p,v):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,separators=(',',':')))
def slug(s):return re.sub('[^A-Za-z0-9_-]','-',s)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def key(s):return hashlib.sha256(json.dumps(s,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:20]
cat=load(D/'data/catalog.json');old_groups={g['id']:g for g in cat['datasets']}
if not (D/'data/examples-catalog.json').exists():dump(D/'data/examples-catalog.json',cat)
specs=[
 ('BIRD-History',1393,F/'repro/v17_r05/predictions.jsonl.gz',M/'results/bird_history_opaque_20261002/online.jsonl'),
 ('BIRD-Dev',1534,DEV/'v15.jsonl',DEV/'online.jsonl'),
 ('BIRD-Mini',300,M/'results/performance_first_dual_evidence_20260821_v1/full/bird_schema_priority_main_300/predictions.jsonl',None),
 ('KaggleDBQA',185,M/'results/v15_crossbench_20261007/kaggledbqa/full/main/graph_evo_semantic_program_main_v1.jsonl',M/'results/v15_crossbench_20261007/kaggledbqa/online.jsonl'),
 ('FIBEN',52,M/'results/v15_crossbench_20261007/fiben/full/main/graph_evo_semantic_program_main_v1.jsonl',M/'results/v15_crossbench_20261007/fiben/online.jsonl'),
 ('EvoSchema',295,M/'results/v15_crossbench_20261007/evoschema/full/main/graph_evo_semantic_program_main_v1.jsonl',M/'results/v15_crossbench_20261007/evoschema/online.jsonl'),
 ('BEAVER',500,None,BEAVER/'questions.json'),('Spider2-Lite',135,None,SPIDER/'questions.json')]
coverage=[];groups=[];allcases=[]
evo_bundle=None

def ensure_schema(dataset,context):
 global evo_bundle
 group=old_groups[dataset];entry=next((e for e in group['databases']if e['id']==context),None)
 if entry:return entry,load(D/entry['path'])
 tables=[];objects=[];sources=[];edges=[]
 if dataset=='EvoSchema':
  if evo_bundle is None:evo_bundle=load(A/'datasets/EvoSchema/ONTOLOGY.json')
  ts=[t for t in evo_bundle['tables']if t['context']==context];cs=[c for c in evo_bundle['columns']if c['context']==context]
  for t in ts:tables.append({'input_id':'current_schema::'+context+'::'+t['physical_table'],'schema_context':context,'physical_table':t['physical_table'],'columns':[{'physical_column':c['physical_column'],'declared_type':c.get('declared_type','unknown'),'primary_key':c.get('primary_key',False)}for c in cs if c['physical_table']==t['physical_table']],'relationships':[]})
 elif dataset=='Spider2-Lite':
  docs=load(SPIDER/'indexes'/context/'documents.json')
  for t in [d for d in docs if d['kind']=='table']:
   cols=[d for d in docs if d['kind']=='column'and d['table']==t['name']]
   tables.append({'input_id':t['candidate_id'],'schema_context':context,'physical_table':t['name'],'columns':[{'physical_column':c['name'].split('.',1)[-1],'declared_type':re.search(r'type:\s*([^\n]+)',c['text']).group(1)if re.search(r'type:\s*([^\n]+)',c['text'])else'unknown','primary_key':False}for c in cols],'relationships':[],'saved_ddl':t['text']})
 else:raise ValueError('unrecognized schema context '+dataset+' '+context)
 if not tables:raise ValueError('missing saved schema metadata '+context)
 for t in tables:
  eid='schema::'+context+'::'+t['physical_table'];facts=[]
  for c in t['columns']:
   fact={'id':'column::'+context+'::'+t['physical_table']+'::'+c['physical_column'],'kind':'column','schema_context':context,'physical_identifiers':[t['physical_table']+'.'+c['physical_column']],'physical_tables':[t['physical_table']],'aliases':[],'roles':[],'evidence_ids':[eid],'source_kind':'released_physical_schema'};objects.append(fact);facts.append(fact)
  ddl=t.get('saved_ddl')or'CREATE TABLE "'+t['physical_table']+'" (\n'+',\n'.join('  "'+c['physical_column']+'" '+str(c.get('declared_type')or'unknown')for c in t['columns'])+'\n);'
  sources.append({'history_id':'schema / '+t['physical_table'],'evidence_id':eid,'schema_context':context,'sql':ddl,'facts':facts,'source_kind':'saved_physical_schema'})
 path='data/'+slug(dataset)+'/'+slug(context)+'.json';db={'database':context,'dataset':dataset,'ontology':{'sources':sources,'objects':objects,'tables':tables,'recovery':[],'edges':edges,'construct':[]},'maintenance':[],'cases':[],'provenance':{'archive':'Saved schema metadata','source':str(A/'datasets/EvoSchema/ONTOLOGY.json')if dataset=='EvoSchema'else str(SPIDER/'indexes'/context/'documents.json')}}
 entry={'id':context,'path':path,'columns':sum(len(t['columns'])for t in tables),'sources':len(sources),'objects':len(objects),'cases':[]};return entry,db

for dataset,expected,pred_path,question_path in specs:
 questions=load(question_path)if question_path else[];qmap={q['example_id']:q for q in questions};records=[]
 if pred_path:
  for p in load(pred_path):records.append((p,None,str(pred_path)))
 elif dataset=='BEAVER':
  for q in questions:
   folder=BEAVER/'runs/native_sr_opt_v1/B3'/q['database_id']/key(q['example_id']);p=folder/'prediction.json';n=folder/'native_full.json';records.append((load(p),load(n)if n.exists()else None,str(p)))
 else:
  for q in questions:
   p=SPIDER/'questions'/q['example_id']/'v17.json';records.append((load(p),None,str(p)))
 ids=[r[0]['example_id']for r in records];assert len(ids)==len(set(ids))==expected,(dataset,len(ids))
 if questions:assert set(ids)==set(qmap),(dataset,'fixed IDs mismatch')
 if dataset=='BIRD-Dev':assert set(ids)==set(load(DEV/'PROTOCOL.json')['ids'])
 if dataset=='BIRD-Mini':assert load(pred_path.parent/'GENERATION_SUMMARY.json')['rows']==expected
 db_cases={};native_count=0;failure_count=0
 for prediction,native,source in records:
  identity=prediction['example_id'];q=qmap.get(identity,{});context=str(prediction.get('database_id')or q['database_id']);r=(native or prediction).get('react')or{}
  question=q.get('question')or prediction.get('question')or r.get('initial_search_query')or(r.get('initial_search')or{}).get('query')
  if not question:raise ValueError('missing saved question '+dataset+' '+identity)
  path='data/'+slug(dataset)+'/all-questions/'+slug(identity)+'.json';case={'id':identity,'title':question[:75],'database':context,'dataset':dataset,'question':question,'origin':'archive','provenance':{'archive':'Saved main result','source':source},'prediction':prediction}
  if native is not None:case['saved_native_trace']=native;case['provenance']['trace_source']=str(Path(source).with_name('native_full.json'))
  if r:native_count+=1
  if not prediction.get('sql'):failure_count+=1
  dump(D/path,case);meta={k:case[k]for k in ['id','title','database','dataset','question','origin']}|{'path':path,'trace_available':bool(r),'saved_status':prediction.get('status')or prediction.get('decision')or'archived'};db_cases.setdefault(context,[]).append(meta);allcases.append(meta)
 entries=[]
 for context in sorted(set(db_cases)|{e['id']for e in old_groups[dataset]['databases']}):
  entry,db=ensure_schema(dataset,context);entry={**entry,'cases':db_cases.get(context,[]),'question_count':len(db_cases.get(context,[]))};db['cases']=entry['cases'];dump(D/entry['path'],db);entries.append(entry)
 groups.append({'id':dataset,'label':dataset,'question_count':expected,'databases':entries})
 c={'dataset':dataset,'fixed_questions':expected,'indexed_questions':len(ids),'native_traces':native_count,'saved_empty_sql':failure_count,'database_schema_entries':len(entries),'prediction_source':str(pred_path)if pred_path else str(BEAVER/'runs/native_sr_opt_v1/B3/*/*/prediction.json')if dataset=='BEAVER'else str(SPIDER/'questions/*/v17.json'),'fixed_population_source':str(question_path or pred_path.parent/'GENERATION_SUMMARY.json'),'ids_sha256':hashlib.sha256(json.dumps(sorted(ids)).encode()).hexdigest()};coverage.append(c);print(json.dumps(c),flush=True)
 dump(D/'data/full-result-coverage.json',coverage)
cat.update({'datasets':groups,'cases':allcases,'databases':groups[0]['databases'],'total_questions':len(allcases),'coverage':'Complete fixed saved main populations'})
dump(D/'data/catalog.json',cat);dump(ROOT/'FULL_RESULTS_RECEIPT.json',{'datasets':coverage,'total_questions':len(allcases),'new_model_requests':0,'SQL_execution':0,'scoring':0,'trace_delivery':'one question JSON per selected ID; native record preserved'})
print('COMPLETE',len(allcases),'questions',sum(len(g['databases'])for g in groups),'schema entries',flush=True)
