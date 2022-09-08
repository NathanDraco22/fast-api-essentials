from fastapi import FastAPI

# there are some events that are fire when fastapi is about starting o finishing
# you can set in the FastApi constructor or adding through decorator
async def app_start_up():
    print ("me muestro cuando el servidor se inicia")

async def app_shut_down():
    print ("me muestro cuando el servidor finaliza")

app = FastAPI(
    title= "FastApi Essentials",
    on_startup  = [app_start_up], # adding a callback list when app is starting
    on_shutdown = [app_shut_down] # adding a callback list qhen app is finishing
)

@app.on_event("startup") # fire when is starting up
async def on_start_up(): # could async o simple def
    print("App started")

@app.on_event("shutdown") # fire when app is about to close
async def on_shut_down(): # could async or simpe def
    print( "App Closed")

# all of these callback will fires when is nearly to start or finish