from pathlib import Path
import json,hashlib,shutil,subprocess,os,sys,time
R=Path(r'C:\Users\aarav\Desktop\secure-launch');W=Path(r'C:\Users\aarav\Desktop\agent skill library\.handoff-work\secure-launch-evals')
E=W/'patch-0.1.1/SL-01';T=W/'trials/SL-01-0.1.1';phase=sys.argv[1]
cli=r'C:\Users\aarav\AppData\Local\OpenAI\Codex\bin\faa963e871dd422c\codex.exe'
E.mkdir(parents=True,exist_ok=True)
if (E/(phase+'.jsonl')).exists():raise SystemExit('Phase already attempted; refusing repeat.')
if phase=='bootstrap':
 if T.exists():raise SystemExit('Trial already exists.')
 shutil.copytree(R/'evals/fixture/express-saas',T)
 shutil.copytree(R/'secure-launch',T/'.candidate/secure-launch',ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
 subprocess.run(['powershell','-NoProfile','-Command',f"New-Item -ItemType Junction -Path '{T / 'node_modules'}' -Target '{W / 'deps/node_modules'}' | Out-Null"],check=True,capture_output=True)
 h=hashlib.sha256()
 for p in sorted((T/'.candidate/secure-launch').rglob('*')):
  if p.is_file():h.update(p.relative_to(T/'.candidate').as_posix().encode());h.update(p.read_bytes())
 meta={'case':'SL-01','run':2,'version':'0.1.1','candidate_sha256':h.hexdigest(),'requested_model':'gpt-5.6-terra','requested_effort':'medium','trial_directory':str(T)}
 prompt='Session initialization only. Do not inspect files, use tools, perform an evaluation, or change anything. Reply READY. The controller will inspect session permission metadata before supplying the task.'
else:
 meta=json.loads((E/'metadata.json').read_text())
 if meta.get('sandbox_policy',{}).get('type')!='workspace-write':raise SystemExit('Workspace-write not confirmed; evaluation blocked.')
 prompt=(E/(phase+'-prompt.txt')).read_text(encoding='utf-8')
common=['--ignore-user-config','-m','gpt-5.6-terra','-c','model_reasoning_effort="medium"','-c','approval_policy="never"','-c','agents.enabled=false','-c','sandbox_workspace_write.network_access=false','-c','web_search="disabled"','--skip-git-repo-check','--json','-c','windows.sandbox="unelevated"','-c','sandbox_mode="workspace-write"','-c',f'projects.{json.dumps(str(T))}.trust_level="trusted"']
cmd=[cli,'exec',*common,'-s','workspace-write','-C',str(T),'-o',str(E/(phase+'-final.md'))]
cmd+=['-'] if phase=='bootstrap' else ['resume',meta['thread_id'],'-']
(E/(phase+'-command.json')).write_text(json.dumps(cmd,indent=2),encoding='utf-8')
(E/(phase+'-prompt.txt')).write_text(prompt,encoding='utf-8')
env={k:v for k,v in os.environ.items() if not any(x in k.upper() for x in ['API_KEY','API_TOKEN','SECRET','PASSWORD','ACCESS_TOKEN','AUTH_TOKEN'])};env.update(PYTHONUTF8='1',NEXT_TELEMETRY_DISABLED='1',CI='1')
start=time.monotonic()
with (E/(phase+'.jsonl')).open('w',encoding='utf-8') as out,(E/(phase+'-stderr.txt')).open('w',encoding='utf-8') as err:
 p=subprocess.Popen(cmd,cwd=T,env=env,stdin=subprocess.PIPE,stdout=out,stderr=err,text=True,encoding='utf-8')
 try:p.communicate(prompt,timeout=420);code=p.returncode
 except subprocess.TimeoutExpired:p.kill();p.wait();code='timeout'
meta[phase+'_exit']=code;meta[phase+'_seconds']=round(time.monotonic()-start,2)
for line in (E/(phase+'.jsonl')).read_text(encoding='utf-8').splitlines():
 try:event=json.loads(line)
 except ValueError:continue
 if event.get('type')=='thread.started':meta['thread_id']=event['thread_id']
 if event.get('type')=='turn.completed':meta[phase+'_usage']=event.get('usage')
paths=list(Path(r'C:\Users\aarav\.codex\sessions').rglob('*'+meta.get('thread_id','NO_THREAD')+'.jsonl'))
if paths:
 for line in paths[0].read_text(encoding='utf-8').splitlines():
  obj=json.loads(line)
  if obj.get('type')=='turn_context':
   payload=obj['payload'];meta.update(confirmed_model=payload.get('model'),confirmed_effort=payload.get('effort'),sandbox_policy=payload.get('sandbox_policy'),metadata_source=str(paths[0]),metadata_fields='turn_context.payload.{model,effort,sandbox_policy}')
(E/'metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print(json.dumps(meta,indent=2))
