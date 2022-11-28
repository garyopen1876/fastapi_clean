from fastapi import FastAPI
from app.routers import login, user
from app.setting import settings
from app.utils.log import Logger

APP_TITLE = "login_system"
APP_VERSION = "1.0.0"

if settings.develop:
    app = FastAPI(title=APP_TITLE, version=APP_VERSION)
else:
    app = FastAPI(docs_url=None, redoc_url=None)


logger = Logger(level = "uvicorn")

@app.get("/", summary="Hello Page")
def read_root():
    logger.info("Hello World")
    return {"Hello": "World"}


app.include_router(login.router, prefix="/login", tags=["Account"])
app.include_router(user.router, prefix="/user", tags=["User"])
