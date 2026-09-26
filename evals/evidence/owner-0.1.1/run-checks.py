from pathlib import Path
import subprocess,json,os,sys
R=Path(r'C:\Users\aarav\Desktop\secure-launch'); W=Path(r'C:\Users\aarav\Desktop\agent skill library\.handoff-work\secure-launch-evals')
E=W/'patch-0.1.1';E.mkdir(exist_ok=True)
if (E/'owner-checks.json').exists():raise SystemExit('Checks already started; refusing repeat.')
checks=[]
def run(name,cmd,cwd):
 checks.append({'name':name,'command':subprocess.list2cmdline(cmd),'cwd':str(cwd),'exit':'RUNNING'})
 (E/'owner-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
 p=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True,encoding='utf-8',errors='replace',env={**os.environ,'NEXT_TELEMETRY_DISABLED':'1','CI':'1'},timeout=180)
 checks[-1].update(exit=p.returncode,output=p.stdout+p.stderr)
 (E/'owner-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
 print(name,'exit',p.returncode);print(p.stdout+p.stderr)
 return p.returncode
run('scanner-check',[sys.executable,'-X','utf8',str(R/'evals/scanner-check.py')],R)
code=run('SL-03 owner Next build',['node','scripts/build.mjs'],W/'trials/SL-03')
if code==0:
 files=[p for p in (W/'trials/SL-03/.next/static').rglob('*') if p.is_file()]
 matches=[p.relative_to(W/'trials/SL-03').as_posix() for p in files if any(v in p.read_bytes() for v in [b'SYNTHETIC_BROWSER_MARKER_DO_NOT_USE_AS_A_KEY',b'NEXT_PUBLIC_MODEL_KEY',b'X-Model-Key'])]
 check={'name':'SL-03 owner client bundle grep','command':'Python: scan .next/static bytes for synthetic canary, NEXT_PUBLIC_MODEL_KEY and X-Model-Key; assert nonempty file set and zero matches','cwd':str(W/'trials/SL-03'),'exit':0 if files and not matches else 1,'output':f'scanned_files={len(files)}; matching_files={len(matches)}; paths={matches}'}
 checks.append(check);print(check['output'])
run('SL-04 owner Node tests',['node','--test','test.mjs'],W/'trials/SL-04')
(E/'owner-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
