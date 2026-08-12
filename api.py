from fastapi import FastAPI
from src.api.routers import router
from src.dependency.container import container

from dishka.integrations.fastapi import setup_dishka

app = FastAPI()
app.include_router(router)
setup_dishka(container, app)



