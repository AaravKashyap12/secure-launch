import {spawnSync} from 'node:child_process';
// A noncredential canary for this local demo; never contact a model provider.
const env={...process.env,NEXT_TELEMETRY_DISABLED:'1',NEXT_PUBLIC_MODEL_KEY:'SYNTHETIC_BROWSER_MARKER_DO_NOT_USE_AS_A_KEY'};
const result=spawnSync(process.execPath,['node_modules/next/dist/bin/next','build','--webpack'],{env,stdio:'inherit'});
process.exit(result.status??1);
