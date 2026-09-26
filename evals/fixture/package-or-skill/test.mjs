import test from 'node:test';import assert from 'node:assert/strict';import {normalize} from './index.mjs';test('normalizes whitespace',()=>assert.equal(normalize(' hello '),'hello'));
