const users=new Map([['Bearer fixture-alice','alice'],['Bearer fixture-bob','bob']]);
export async function POST(request){
  const user=users.get(request.headers.get('authorization'));
  if(!user)return Response.json({error:'Sign in required'},{status:401});
  const payload=await request.json();
  return Response.json({answer:`Mock reply for ${user}`,received:typeof payload.message==='string'});
}
