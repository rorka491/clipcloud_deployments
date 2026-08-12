from dishka import make_async_container
from src.dependency.service import ServiceProvider
from src.dependency.general import GeneralProvider

from src.dependency.sqlalchemy import SQLAlchemyProvider
from src.dependency.repositories import RepositoryProvider
from dishka.integrations.aiogram import AiogramProvider

container = make_async_container(
    GeneralProvider(),
    AiogramProvider(),
    RepositoryProvider(),
    SQLAlchemyProvider(),
    ServiceProvider()
)