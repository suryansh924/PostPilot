from fastapi import FastAPI
from app.routers import auth, content, storage, webhooks

app = FastAPI(title="PostPilot API")

app.include_router(auth.router, prefix="/auth")
app.include_router(content.router, prefix="/contents")
app.include_router(storage.router, prefix="/storage")
app.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])
