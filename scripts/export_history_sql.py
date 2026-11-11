#!/usr/bin/env python3
"""Project genuine state/table-input history records and native evidence links only."""
import gzip,hashlib,json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist';R=ROOT.parent/'SchemaRecovery-section16-20261026';A=R/'handoff_live/ontology_appendix_20261107/SchemaRecovery_MainTable_Ontology_Appendix_20261107'
def load(p):
 p=Path(p)
 with(gzip.open(p,'rt')if p.suffix=='.gz'else p.open())as f:return[json.loads(l)for l in f if l.strip()]if'.jsonl'in p.name else json.load(f)
def dump(p,v):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,ensure_ascii=False,separators=(',',':')))
def signature(db,identity,sql):return hashlib.sha256(json.dumps([db,identity,sql],ensure_ascii=False).encode()).hexdigest()
manifest=load(A/'SOURCE_MANIFEST.json');cat=load(D/'data/catalog.json');report=[];metadata_keys={'dialect','source','source_name','source_kind','origin','provenance','synthetic','is_synthetic','is_real','data_origin','confidence','generated_by'}
for group in cat['datasets']:
 ds=group['id'];source_ds='BIRD-Dev-and-Mini'if ds in{'BIRD-Dev','BIRD-Mini'}else ds
 table_path=next((Path(x['source_path'])for x in manifest if x['dataset']==source_ds and x['role']=='table_inputs'),None)
 state_path=next((Path(x['source_path'])for x in manifest if x['dataset']==source_ds and x['role']=='semantic_state'),None)
 tables=load(table_path)if table_path else[];state=load(state_path)if state_path else{}
 total=0;db_counts=[]
 for entry in group['databases']:
  db=load(D/entry['path']);context=db['database'];o=db['ontology'];items={}
  def add(row,origin,table=None):
   identity=row.get('history_id');sql=row.get('sql')
   if not identity or not isinstance(sql,str)or not sql.strip():return
   # These call sites are exclusively native history containers, never schema/KB/query results.
   raw_sql=sql;key=signature(context,str(identity),raw_sql);refs={str(identity)}
   if row.get('evidence_id'):refs.add(str(row['evidence_id']))
   record=items.setdefault(key,{'key':key,'database':context,'history_id':str(identity),'sql':raw_sql,'evidence_ids':[],'metadata':[],'native_sources':[],'explicit_physical_identifiers':[]})
   record['evidence_ids']=sorted(set(record['evidence_ids'])|refs)
   meta={k:row[k]for k in metadata_keys if k in row}
   if meta and meta not in record['metadata']:record['metadata'].append(meta)
   if origin not in record['native_sources']:record['native_sources'].append(origin)
   if table:
    record['explicit_physical_identifiers']=sorted(set(record['explicit_physical_identifiers'])|{table+'.'+str(c)for c in row.get('physical_columns',[])})
  for key,row in state.get('records',{}).items():
   if row.get('schema_context')==context:add({'evidence_id':'sql_log::'+key,**row},'native semantic state.records')
  for table in tables:
   if table.get('schema_context')!=context:continue
   for row in table.get('target_disjoint_workload',[]):add(row,'native table_inputs.target_disjoint_workload',table['physical_table'])
  # The source export retains native state IDs; union their evidence references for exact duplicates.
  for row in o['sources']:
   if row.get('source_kind')=='saved_historical_sql'or row.get('extractor_version')is not None:
    key=signature(context,str(row.get('history_id','')),row.get('sql',''))
    if key in items:add(row,'saved native history contribution')
  object_index=defaultdict(set);edge_index=defaultdict(set)
  for obj in o['objects']:
   for ref in obj.get('evidence_ids',[]):object_index[str(ref)].add(obj['id'])
  for i,edge in enumerate(o['edges']):
   for ref in edge.get('provenance_ids',[]):edge_index[str(ref)].add(i)
  by_id={obj['id']:obj for obj in o['objects']}
  known_physical={t['physical_table']+'.'+c['physical_column']for t in o['tables']for c in t['columns']}
  for record in items.values():
   ids=set().union(*(object_index.get(ref,set())for ref in record['evidence_ids']))
   supported=[by_id[identity]for identity in sorted(ids)]
   record['supported_object_ids']=sorted(ids)
   record['supported_physical_identifiers']=sorted(set(record['explicit_physical_identifiers'])|{p for obj in supported if obj.get('kind')=='column'for p in obj.get('physical_identifiers',[])})
   record['unbound_source_identifiers']=sorted(set(record['supported_physical_identifiers'])-known_physical)
   record['supported_physical_identifiers']=sorted(set(record['supported_physical_identifiers'])&known_physical)
   record['supported_edge_indices']=sorted(set().union(*(edge_index.get(ref,set())for ref in record['evidence_ids'])))
   record['supported_business_ids']=[obj['id']for obj in supported if obj.get('kind')in{'metric','binding','predicate','program'}]
  records=sorted(items.values(),key=lambda row:(row['history_id'],row['key']))
  history_path='history-sql/'+ds+'/'+Path(entry['path']).stem+'.json';dump(D/history_path,{'dataset':ds,'database':context,'count':len(records),'deduplication':'database + original history_id + exact SQL content','records':records})
  db['history_sql_path']=history_path;db['history_sql_count']=len(records);entry['history_sql_count']=len(records);dump(D/entry['path'],db)
  total+=len(records);db_counts.append({'database':context,'history_sql_count':len(records)})
 report.append({'dataset':ds,'history_sql_total':total,'databases':db_counts,'native_table_inputs':str(table_path)if table_path else None,'native_state':str(state_path)if state_path else None});print(ds,total,flush=True)
dump(D/'data/catalog.json',cat);dump(D/'data/history-sql-coverage.json',report);dump(ROOT/'HISTORY_SQL_RECEIPT.json',{'datasets':report,'total_history_records':sum(r['history_sql_total']for r in report),'source_rule':'native table_inputs.target_disjoint_workload and semantic state.records only','new_model_requests':0,'SQL_execution':0,'query_results_or_Gold_used':False})
