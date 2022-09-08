from fastapi import FastAPI
from pydantic import BaseModel # Remember from Pydantic

app : FastAPI = FastAPI()

class NestedDate(BaseModel):
    data : str

class BasicResponse(BaseModel):
    msg : str
    other : NestedDate

@app.post("/custom")
async def response(body : BasicResponse):
    return body

# above you can see a two class extends from Pydantic BaseModel
# you can validate a body from post request.
# also Pydantic BaseModel can be uses for nested data validation.
# Sending a Pydantic BaseModel is automatic convert to json response.