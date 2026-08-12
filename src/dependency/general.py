from aiogram import Bot
from dishka import Provider, Scope, provide
from src.core.config import settings


class GeneralProvider(Provider):
    
    @provide(scope=Scope.APP)
    def bot(self) -> Bot:
        return Bot(token=settings.bot_access_token)
