import test from 'node:test';import assert from 'node:assert/strict';import {app} from './app.mjs';
test('health endpoint',async()=>{const s=app.listen(0,'127.0.0.1');await new Promise(r=>s.once('listening',r));try{const r=await fetch(`http://127.0.0.1:${s.address().port}/health`);assert.equal(r.status,200)}finally{await new Promise(r=>s.close(r))}});
