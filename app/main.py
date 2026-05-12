from fastapi import FastAPI
from app.routes import test

app = FastAPI(title="Synapse API")

app.include_router(test.router)

@app.get("/")
def root():
    return {"message": "Synapse Backend Running"}