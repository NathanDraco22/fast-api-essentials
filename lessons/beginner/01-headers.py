from fastapi import FastAPI
from fastapi import Header #Ever import from FAST API

app : FastAPI = FastAPI()

#Headers are declared in the callback
@app.get("/")
async def home( x_value : str | None = Header( default= None )): # A default Value NONE make a optional header
    return {
        "soy un header" : x_value 
    }
# x_value == x-value in the http request.
# Header( default= None ) -> this header is optional



