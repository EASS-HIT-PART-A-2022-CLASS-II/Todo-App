from fastapi import FastAPI
from app.backend.routers import router

app = FastAPI()

#Include router
app.include_router(router)



