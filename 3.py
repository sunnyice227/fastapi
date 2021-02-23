from fastapi import FastAPI
import asyncio

app = FastAPI()


async def log_to_data_base():
    await asyncio.sleep(10)
    print("log in database")


@app.get("/")
async def main():
    asyncio.create_task(log_to_data_base())
    # 创建一个新的可以调度的协程，负责向数据库写入数据
    return "返回数据"
