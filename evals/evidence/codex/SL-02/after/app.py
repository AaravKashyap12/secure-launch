from fastapi import FastAPI, Header, HTTPException, Request
app=FastAPI()
IDENTITIES={'Bearer fixture-alice':{'user':'alice','tenant':'a'},'Bearer fixture-bob':{'user':'bob','tenant':'b'}}
RECORDS={'a-note':{'id':'a-note','tenant':'a','body':'Synthetic A note'},'b-note':{'id':'b-note','tenant':'b','body':'Synthetic B note'}}

@app.middleware('http')
async def baseline_headers(request:Request,call_next):
    response=await call_next(request)
    response.headers['X-Content-Type-Options']='nosniff'
    response.headers['X-Frame-Options']='DENY'
    response.headers['Referrer-Policy']='no-referrer'
    return response

@app.get('/health')
def health():return {'ok':True}
@app.get('/records/{record_id}')
def record(record_id:str,authorization:str=Header(default='')):
    subject=IDENTITIES.get(authorization)
    if not subject:raise HTTPException(status_code=401)
    found=RECORDS.get(record_id)
    if not found:raise HTTPException(status_code=404)
    if found['tenant']!=subject['tenant']:raise HTTPException(status_code=403)
    return found
