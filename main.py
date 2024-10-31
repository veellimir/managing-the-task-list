from fastapi import FastAPI

main_app = FastAPI()

@main_app.get("/")
async def read_root():
    return {"Hello": "World"}