from fastapi import Header, Response
from fastapi import FastAPI, Depends
from src.events.my_events import * 

app : FastAPI = FastAPI(
    version= '0.0.1', 
    title= "FastApi Essentials",
    on_startup = [on_start, on_start_two],
    on_shutdown= [on_shut_down , on_shut_down_two],
)

app = FastAPI()

async def my_dependencies( 
    x_token : str|None = Header( default= None ),
    resp : Response = Response(),
):
    resp.headers["x-algo"] = "HOLA SOY UN HEADER"
    print(f"From dependencies: {x_token} ")
    return True

@app.get("/")
async def home( result = Depends(my_dependencies), x_token : str|None = Header(default= None) ):
    print(f"From Get Callback : {x_token}")
    return {
        "ok" : True
    }