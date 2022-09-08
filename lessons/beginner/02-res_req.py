from fastapi import FastAPI, Request,Response 

app : FastAPI = FastAPI()

@app.get("/custom")
async def response(res : Response, req : Request):
    print(req.headers)
    res.status_code = 404
    return "SOY UN ALGO CUSTOM"

# You can access to basic object from a http.
# response you can set headers to will send.
# request to get info from client request.
# you can access or set headers.

