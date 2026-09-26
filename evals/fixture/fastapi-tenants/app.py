from fastapi import FastAPI, Header, HTTPException
app=FastAPI()
IDENTITIES={'Bearer fixture-alice':{'user':'alice','tenant':'a'},'Bearer fixture-bob':{'user':'bob','tenant':'b'}}
RECORDS={'a-note':{'id':'a-note','tenant':'a','body':'Synthetic A note'},'b-note':{'id':'b-note','tenant':'b','body':'Synthetic B note'}}
@app.get('/health')
def health():return {'ok':True}
@app.get('/records/{record_id}')
def record(record_id:str,authorization:str=Header(default='')):
    subject=IDENTITIES.get(authorization)
    if not subject:raise HTTPException(status_code=401)
    found=RECORDS.get(record_id)
    if not found:raise HTTPException(status_code=404)
    return found
