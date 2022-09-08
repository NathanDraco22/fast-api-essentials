async def on_start():
    print("I'm the start up event")
async def on_start_two():
    print("I'm the other start up event")

async def on_shut_down():
    print("i'm shut down event")

async def on_shut_down_two():
    print("i'm the other shut down event")