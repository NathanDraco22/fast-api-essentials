from fastapi import FastAPI , Header, Depends

# FAST API have a dependendies injection
#A function that is a exactly is in the decorator routes.

app = FastAPI()

#Same paramters like a decorated function in any HTTP method
async def my_dependencies( x_token : str|None = Header( default= None ) ):
    print(f"From dependencies: {x_token} ")
    return True


@app.get("/")
async def home( result = Depends(my_dependencies), x_token : str|None = Header(default= None) ):
    print(f"From Get Callback : {x_token}")
    return {
        "ok" : True
    }

# result = Depends(my_dependencies) -> this retrieve depends result
# x_token : str|None = Header(default= None) -> you still get the same parameter in your decorated def


