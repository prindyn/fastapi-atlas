from fastapi import FastAPI
from routes import router

app = FastAPI(title="FastAPI + MongoDB Atlas")

app.include_router(router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with MongoDB Atlas"}