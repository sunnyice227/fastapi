import asyncio

from fastapi import FastAPI

app = FastAPI()

async def some_library():
    await asyncio.sleep(10)
    return "等待十秒"


@app.get('/')
async def read_results():
    asyncio.create_task(some_library())
    #results = await some_library()
    return "1212"