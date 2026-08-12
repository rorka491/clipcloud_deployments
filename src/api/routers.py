from fastapi import APIRouter
from src.api.webhooks import router as webhook_router

router = APIRouter()

router.include_router(webhook_router)