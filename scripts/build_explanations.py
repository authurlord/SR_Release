#!/usr/bin/env python3
"""Build per-dataset/database bilingual schema guides from saved native records."""
import html,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist'
def load(p):return json.loads(p.read_text())
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,separators=(',',':')))
def safe(s):return re.sub('[^A-Za-z0-9_-]','-',s)
def esc(v):return html.escape(str(v if v is not None else ''))
cat=load(D/'data/catalog.json');count=0;index=[]
for dataset in cat['datasets']:
 for entry in dataset['databases']:
  path=D/entry['path'];db=load(path);o=db['ontology'];name=db['database'];rec={r['prediction']['physical_table']:r['prediction'] for r in o['recovery']}
  sources={s['evidence_id']:s for s in o['sources']};column_objects={p:x for x in o['objects'] if x.get('kind')=='column' for p in x.get('physical_identifiers',[])}
  aliases={}
  query_sql=[load(D/case['path'])['prediction'].get('sql') or '' for case in db['cases']]
  for text in [source['sql'] for source in o['sources']]+query_sql:
   for table,alias in re.findall(r'(?:FROM|JOIN)\s+["`]?([\w]+)["`]?\s+(?:AS\s+)?([A-Za-z]\w*)',text,flags=re.I):
    if alias.upper() not in {'WHERE','JOIN','INNER','LEFT','RIGHT','GROUP','ORDER','ON','UNION','LIMIT','AS','HAVING'}:aliases.setdefault(table,set()).add(alias)
  db['sql_table_aliases']={t:sorted(a) for t,a in aliases.items()}
  documents={}
  for lang in ['en','zh']:
   zh=lang=='zh';head=f"{dataset['label']} / {name} — "+('Schema 与业务口径解释' if zh else 'Schema and business semantics')
   introduction=(f"该数据库的存档目录包含 {len(o['tables'])} 张表、{sum(len(t['columns']) for t in o['tables'])} 个物理列、{len(o['edges'])} 条关系，以及 {len(o['sources'])} 条来源记录。恢复名称取自已保存的原生恢复记录和语义对象；SQL 表别名取自当前数据库的来源 SQL。" if zh else f"The saved catalogue for this database contains {len(o['tables'])} tables, {sum(len(t['columns']) for t in o['tables'])} physical columns, {len(o['edges'])} relationships and {len(o['sources'])} source records. Recovered names come from saved native recovery records and semantic objects; SQL table aliases come from this database's source SQL.")
   chunks=[f'<h2>{esc(head)}</h2><p>{esc(introduction)}</p>'];md=['# '+head,'',introduction,'']
   for table in o['tables']:
    physical=table['physical_table'];pred=rec.get(physical,{});table_aliases=pred.get('table_aliases',[]);sqlaliases=sorted(aliases.get(physical,[]));purpose=pred.get('purpose') or ('该表的存档未记录额外业务说明。' if zh else 'No additional table purpose is recorded in this archive.')
    chunks.append(f'<details class="sr-native-block"><summary>{esc(physical)} · {len(table["columns"])} '+('列' if zh else 'columns')+'</summary>')
    chunks.append('<p>'+esc(purpose)+'</p><p><b>'+('恢复表名' if zh else 'Recovered table names')+':</b> '+esc(' / '.join(table_aliases) or '—')+'</p><p><b>'+('来源 SQL 中的表别名/缩写' if zh else 'Aliases / abbreviations in source SQL')+':</b> '+esc(', '.join(sqlaliases) or '—')+'</p>')
    md+=['## '+physical,'',purpose,'',('恢复表名' if zh else 'Recovered table names')+': '+(' / '.join(table_aliases) or '—'),('SQL表别名' if zh else 'SQL table aliases')+': '+(', '.join(sqlaliases) or '—'),'','| Physical | '+('恢复名称' if zh else 'Recovered names')+' | Type | '+('来源' if zh else 'Sources')+' |','|---|---|---|---|']
    rec_cols={c['physical_column']:c for c in pred.get('columns',[])}
    chunks.append('<table class="sr-table"><thead><tr><th>Physical</th><th>'+('恢复名称' if zh else 'Recovered names')+'</th><th>Type</th><th>'+('来源' if zh else 'Sources')+'</th></tr></thead><tbody>')
    for column in table['columns']:
     p=physical+'.'+column['physical_column'];obj=column_objects.get(p,{});r=rec_cols.get(column['physical_column'],{});names=list(dict.fromkeys(obj.get('aliases',[])+r.get('aliases',[])));source_ids=[sources.get(e,{}).get('history_id',e) for e in obj.get('evidence_ids',[])];source_ids=source_ids or column.get('history_ids',[]);meaning=' / '.join(names) or ('保留物理名称；存档没有恢复别名' if zh else 'Physical name retained; no saved recovered alias');typ=column.get('declared_type','unknown')
     chunks.append('<tr><td>'+esc(p)+'</td><td>'+esc(meaning)+'</td><td>'+esc(typ)+'</td><td>'+esc(', '.join(source_ids[:8]) or '—')+'</td></tr>');md.append('| '+p+' | '+meaning.replace('|','\\|')+' | '+str(typ)+' | '+(', '.join(source_ids[:8]) or '—')+' |')
    chunks.append('</tbody></table></details>');md.append('')
   title='表关系与连接依据' if zh else 'Relationships and join evidence';chunks.append('<h3>'+title+'</h3>');md+=['## '+title,'']
   for edge in o['edges']:
    line=f"{edge['left']} ↔ {edge['right']}";evidence=', '.join(edge.get('evidence_types',[]));chunks.append('<details class="sr-json"><summary>'+esc(line)+'</summary><p>'+esc(evidence)+'</p><p>'+esc(', '.join(edge.get('provenance_ids',[])))+'</p></details>');md.append('- '+line+'; '+evidence)
   if not o['edges']:chunks.append('<p>'+('该存档未提供已绑定关系。' if zh else 'No bound relationship is stored in this archive.')+'</p>')
   title='业务口径、总体与粒度' if zh else 'Business definitions, population and grain';chunks.append('<h3>'+title+'</h3>');md+=['','## '+title,'']
   for obj in o['objects']:
    if obj.get('kind') not in {'metric','binding','predicate','program'}:continue
    label=obj.get('aliases',[None])[0] if obj.get('aliases') else obj.get('expression',obj['id']);definition={'kind':obj['kind'],'formula':obj.get('expression'),'grain':obj.get('grain',[]),'population_scope':obj.get('row_context'),'upstream_scopes':obj.get('upstream_scopes',[]),'execution_contract':obj.get('execution_contract'),'source_history_ids':[sources.get(e,{}).get('history_id',e) for e in obj.get('evidence_ids',[])]}
    chunks.append('<details class="sr-json"><summary>'+esc(str(label)[:150])+'</summary><pre class="sr-code">'+esc(json.dumps(definition,ensure_ascii=False,indent=2))+'</pre></details>');md+=['### '+str(label).replace('\n',' ')[:150],'','```json',json.dumps(definition,ensure_ascii=False,indent=2),'```','']
   title='增量维护事件' if zh else 'Incremental maintenance events';chunks.append('<h3>'+title+'</h3>');md+=['','## '+title,'']
   for event in db.get('maintenance',[]):
    line=event['title']+' · '+event['source'];chunks.append('<p>'+esc(line)+'</p>');md.append('- '+line)
    for c in event['column_changes']:
     line=', '.join(c['physical_identifiers'])+': '+' / '.join(c['before'])+' → '+' / '.join(c['after']);chunks.append('<p class="sr-mono">'+esc(line)+'</p>');md.append('  - '+line)
   if not db.get('maintenance'):chunks.append('<p>'+('当前存档包含构建结果；可在本地API导入SQL变化后生成增量维护收据。' if zh else 'This archive contains construction artifacts. A SQL change imported through the local API generates an incremental maintenance receipt.')+'</p>')
   base='explanations/'+safe(dataset['id'])+'/'+safe(name);markdown=base+'.'+lang+'.md';(D/markdown).parent.mkdir(parents=True,exist_ok=True);(D/markdown).write_text('\n'.join(md)+'\n');documents[lang]={'title':head,'html':'\n'.join(chunks),'markdown':markdown}
  base='explanations/'+safe(dataset['id'])+'/'+safe(name);dump(D/(base+'.json'),{'dataset':dataset['id'],'database':name,'source':'saved native schema/recovery/semantic records','documents':documents});db['explanations']=base+'.json';dump(path,db);entry['explanations']=base+'.json';count+=1;index.append({'dataset':dataset['id'],'database':name,'path':base+'.json'})
dump(D/'data/catalog.json',cat);dump(D/'explanations/index.json',index);print(json.dumps({'database_guides':count,'languages':2,'markdown_documents':count*2}))
