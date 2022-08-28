from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API COM FASTAPI",
    description="Simples APi com mongoDB"
)

app.include_router(user)