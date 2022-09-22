from fastapi import FastAPI
from app.routers import user

APP_TITLE = "login_system"
APP_VERSION = "1.0.0"

app = FastAPI(
    title= APP_TITLE,
    version= APP_VERSION
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user.router, prefix="/user", tags=["User"])