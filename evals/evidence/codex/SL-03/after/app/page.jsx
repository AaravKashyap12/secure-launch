'use client';
export default function Home(){return <main><h1>Chat demo</h1><button onClick={()=>fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json','Authorization':'Bearer fixture-alice'},body:JSON.stringify({message:'Hello'})})}>Send demo message</button></main>}
