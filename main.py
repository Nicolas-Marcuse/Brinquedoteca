from fastapi import FastAPI
from api.routes.routes import router

app = FastAPI()

app.include_router(router)