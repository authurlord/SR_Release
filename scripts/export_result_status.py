#!/usr/bin/env python3
"""Join saved official scoring metadata to the existing archive index; never score SQL."""
import gzip,hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist';M=ROOT.parent/'SchemaRecovery';R=ROOT.parent/'SchemaRecovery-section16-20261026';F=ROOT.parent/'SchemaRecovery-r05-anchor-20261016';DEV=ROOT.parent/'SchemaRecovery-maintenance-20261008/results/v16_iteration_20261009/bird_dev1534_v15_v16_20261009';SP=R/'results/exp_multibench_20261104/spider2_v17_opt_20261108';BE=R/'results/sr_beaver_opt_20261105/evaluator_only/native_v17_first1_phase3_v1_runtime_recovered_v1'
def load(p):
 p=Path(p)
 with(gzip.open(p,'rt')if p.suffix=='.gz'else p.open())as f:return[json.loads(l)for l in f if l.strip()]if'.jsonl'in p.name else json.load(f)
def save(p,v):Path(p).write_text(json.dumps(v,ensure_ascii=False,separators=(',',':')))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def sqlhash(s):return hashlib.sha256(str(s or'').encode()).hexdigest()
def byid(p):return{row['example_id']:row for row in load(p)}
paired={'BIRD-History':(F/'repro/v17_r05/scores/paired_scores.jsonl.gz','v17_r05_recovered'),'BIRD-Dev':(DEV/'scores/paired_scores.jsonl','v15'),'BIRD-Mini':(M/'results/performance_first_dual_evidence_20260821_v1/full/bird_schema_priority_main_300/scores/paired_scores.jsonl','main')}
rows={ds:byid(path)for ds,(path,_)in paired.items()};source_paths={ds:str(path)for ds,(path,_)in paired.items()};frozen={}
for ds,folder in [('KaggleDBQA','kaggledbqa'),('FIBEN','fiben')]:
 base=M/'results/v15_crossbench_20261007'/folder/'full';manifest=load(base/'FROZEN_RESULTS.json')['sha256'];pred=base/'main/graph_evo_semantic_program_main_v1.jsonl';score=base/'scores.jsonl';frozen[ds]=sha(pred)==manifest['main/graph_evo_semantic_program_main_v1.jsonl']and sha(score)==manifest['scores.jsonl'];rows[ds]=byid(score);rows[ds+'_pred']=byid(pred);source_paths[ds]=str(score)
p=M/'results/v15_crossbench_20261007/evoschema/full/scores/PER_EXAMPLE_SCORES.jsonl';rows['EvoSchema']=byid(p);source_paths['EvoSchema']=str(p)
p=SP/'evaluation/v17/official_summary.json';rows['Spider2-Lite']=load(p)['scores'];source_paths['Spider2-Lite']=str(p)
rows['BEAVER']={r['example_id']:r for r in(load(p)for p in(BE/'receipts').glob('*.json'))};source_paths['BEAVER']=str(BE/'receipts/*.json')
cat=load(D/'data/catalog.json');report=[]
for group in cat['datasets']:
 ds=group['id'];counts=Counter();reasons=Counter()
 for entry in group['databases']:
  db=load(D/entry['path']);updated=[]
  for meta in db['cases']:
   case=load(D/meta['path']);pred=case['prediction'];eid=meta['id'];row=rows.get(ds,{}).get(eid);value=None;reason='official_score_missing';field=None
   if row is not None:
    if ds in paired:
     method=row.get('methods',{}).get(paired[ds][1],{});field='official_ex';value=method.get(field);reason='saved_official_score'if sqlhash(method.get('sql'))==sqlhash(pred.get('sql'))else'SQL_not_matched'
     if row.get('gold_error')is not None:value=None;reason='unscorable_saved_evaluation'
    elif ds in frozen:
     field='success';value=row.get(field);reason='saved_official_score'if frozen[ds]and sqlhash(rows[ds+'_pred'].get(eid,{}).get('sql'))==sqlhash(pred.get('sql'))else'prediction_artifact_not_matched'
     if row.get('scorable')is False:value=None;reason='unscorable_saved_evaluation'
    elif ds=='EvoSchema':
     method=row.get('predictions',{}).get('v15',{});field='ex';value=method.get(field);reason='saved_official_score'if sqlhash(method.get('sql'))==sqlhash(pred.get('sql'))else'SQL_not_matched'
    elif ds=='Spider2-Lite':
     field='score';value=row.get(field);reason='saved_official_score'if sqlhash(row.get('sql'))==sqlhash(pred.get('sql'))else'SQL_not_matched'
    elif ds=='BEAVER':
     source=Path(case['provenance']['source']);score=Path(row['score_path']);bound=source.exists()and score.exists()and sha(source)==row['prediction_sha256']and sha(score)==row['score_sha256']and sqlhash(load(source).get('sql'))==sqlhash(pred.get('sql'))
     result=load(score)if bound else{};field='EX';value=result.get(field);reason='saved_official_score'if bound else'prediction_artifact_not_matched'
   if reason!='saved_official_score'or type(value)not in(bool,int,float)or value not in(0,1):status='unknown';score_value=None
   else:status='success'if value==1 else'failure';score_value=int(value)
   enriched={**meta,'result_status':status,'official_score':score_value,'evaluation_reason':reason};updated.append(enriched);counts[status]+=1;reasons[reason]+=1
  db['cases']=updated;entry['cases']=updated;entry['result_counts']=dict(Counter(m['result_status']for m in updated));save(D/entry['path'],db)
 group['result_counts']={key:counts[key]for key in['success','failure','unknown']};report.append({'dataset':ds,'count':sum(counts.values()),**group['result_counts'],'score_source':source_paths.get(ds),'binding_reasons':dict(reasons)});print(report[-1],flush=True)
cat['databases']=cat['datasets'][0]['databases'];cat['cases']=[case for g in cat['datasets']for e in g['databases']for case in e['cases']];cat['official_score_sources']=source_paths;cat['result_counts']=dict(Counter(c['result_status']for c in cat['cases']));save(D/'data/catalog.json',cat);save(D/'data/result-status-coverage.json',report);save(ROOT/'RESULT_FILTER_RECEIPT.json',{'datasets':report,'total':4394,'default_filter':'success','status_source':'saved official per-question score fields only','binding':'Exact SQL text hash or frozen prediction artifact/hash receipt','unknown_policy':'Missing/mismatched/unscorable saved evaluations remain unscored','new_model_requests':0,'SQL_execution':0,'rescoring':0})
