const users=new Map([['Bearer fixture-alice','alice'],['Bearer fixture-bob','bob']]);
const MAX_REQUESTS_PER_WINDOW=5;
const REQUEST_WINDOW_MS=60_000;
const MAX_BODY_BYTES=4_096;
const MAX_MESSAGE_CHARS=1_000;
const requestWindows=new Map();

function takeRequestSlot(user){
  const now=Date.now();
  const window=requestWindows.get(user);
  if(!window||now-window.startedAt>=REQUEST_WINDOW_MS){
    requestWindows.set(user,{startedAt:now,count:1});
    return {allowed:true};
  }
  if(window.count>=MAX_REQUESTS_PER_WINDOW){
    return {allowed:false,retryAfter:Math.max(1,Math.ceil((REQUEST_WINDOW_MS-(now-window.startedAt))/1_000))};
  }
  window.count+=1;
  return {allowed:true};
}

async function readJsonBody(request){
  const declaredLength=Number(request.headers.get('content-length'));
  if(Number.isFinite(declaredLength)&&declaredLength>MAX_BODY_BYTES)return {error:'Request body is too large',status:413};
  const reader=request.body?.getReader();
  if(!reader)return {error:'Request body is required',status:400};
  const chunks=[];
  let size=0;
  try{
    while(true){
      const {done,value}=await reader.read();
      if(done)break;
      size+=value.byteLength;
      if(size>MAX_BODY_BYTES){
        await reader.cancel();
        return {error:'Request body is too large',status:413};
      }
      chunks.push(value);
    }
  }finally{reader.releaseLock();}
  const bytes=new Uint8Array(size);
  let offset=0;
  for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.byteLength;}
  try{return {value:JSON.parse(new TextDecoder().decode(bytes))};}
  catch{return {error:'Request body must be valid JSON',status:400};}
}

export async function POST(request){
  const user=users.get(request.headers.get('authorization'));
  if(!user)return Response.json({error:'Sign in required'},{status:401});
  const slot=takeRequestSlot(user);
  if(!slot.allowed)return Response.json({error:'Too many chat requests'},{status:429,headers:{'Retry-After':String(slot.retryAfter)}});
  const body=await readJsonBody(request);
  if(body.error)return Response.json({error:body.error},{status:body.status});
  if(!body.value||Array.isArray(body.value)||typeof body.value.message!=='string'||body.value.message.length>MAX_MESSAGE_CHARS){
    return Response.json({error:'Message must be a string of at most 1000 characters'},{status:400});
  }
  return Response.json({answer:`Mock reply for ${user}`,received:true});
}
