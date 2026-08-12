import hashlib
import hmac
import json

from fastapi import APIRouter, HTTPException, Header, Request
from dishka.integrations.fastapi import FromDishka, inject

from src.services.deployment import DeploymentService
from src.core.config import settings


router = APIRouter(prefix="/webhooks")


@router.post("/github")
@inject
async def github_webhook(
    request: Request,
    service: FromDishka[DeploymentService],
    x_hub_signature_256: str | None = Header(default=None),
):
    body = await request.body()

    if not x_hub_signature_256:
        raise HTTPException(status_code=401)

    expected = "sha256=" + hmac.new(
        settings.github_webhook_secret.encode(),
        body,
        hashlib.sha256,
    ).hexdigest()

    if not hmac.compare_digest(expected, x_hub_signature_256):
        raise HTTPException(status_code=401)

    payload = json.loads(body)

    if payload.get("ref") != "refs/heads/main":
        return {"status": "ignored"}
    await service.handle_push(payload)
    return {"status": "ok"}
