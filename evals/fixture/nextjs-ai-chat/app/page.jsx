'use client';
const providerKey=process.env.NEXT_PUBLIC_MODEL_KEY;
export default function Home(){return <main><h1>Chat demo</h1><button onClick={()=>fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer fixture-alice','X-Model-Key':providerKey},body:JSON.stringify({message:'Hello'})})}>Send demo message</button></main>}
