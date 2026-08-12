from aiogram import Bot
from dishka import Provider, Scope, provide
from src.core.config import settings
from aiogram.client.telegram import TelegramAPIServer

class GeneralProvider(Provider):

    @provide(scope=Scope.APP)
    def bot(self) -> Bot:
        custom_server = TelegramAPIServer.from_base(
            "https://quiet-bush-1418.rodion-gorshkov-456.workers.dev"
        )
        return Bot(token=settings.bot_access_token, server=custom_server)
