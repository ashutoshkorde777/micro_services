# main.py
from fastapi import FastAPI
from app.routes.subscription_routes import router as subscription_router

app = FastAPI()

app.include_router(subscription_router)

@app.get("/")
def read_root():
    return {"message": "Subscription Service is running"}