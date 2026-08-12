from aiogram import Bot
from src.models.subscriber import Subscriber


class TelegramNotifier:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def notify_all(
        self,
        subscribers: list[Subscriber],
        text: str,
    ):
        for subscriber in subscribers:
            await self.bot.send_message(
                chat_id=subscriber.chat_id,
                text=text,
            )