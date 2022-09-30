from fastapi import FastAPI
from app.routers import login, user
from app.setting import settings


APP_TITLE = "login_system"
APP_VERSION = "1.0.0"

if settings.develop:
    app = FastAPI(title=APP_TITLE, version=APP_VERSION)
else:
    app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/", summary="Hello Page")
def read_root():
    return {"Hello": "World"}


app.include_router(login.router, prefix="/login", tags=["Account"])
app.include_router(user.router, prefix="/user", tags=["User"])
