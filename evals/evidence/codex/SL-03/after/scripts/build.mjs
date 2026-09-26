import {spawnSync} from 'node:child_process';
// This fixture has no provider credential or model call in its build path.
const env={...process.env,NEXT_TELEMETRY_DISABLED:'1'};
delete env.NEXT_PUBLIC_MODEL_KEY;
const result=spawnSync(process.execPath,['node_modules/next/dist/bin/next','build','--webpack'],{env,stdio:'inherit'});
process.exit(result.status??1);
