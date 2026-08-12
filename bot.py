import asyncio
from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from src.dependency.container import container
from src.bot.routers import router
from dishka.integrations.aiogram import setup_dishka
from src.core.config import settings


dp = Dispatcher()
dp.include_router(router)
setup_dishka(
    container=container,
    router=dp,
    auto_inject=True,
)

async def setup_bot(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(
                command="start",
                description="Начать работу",
            ),
        ]
    )

async def main():
    bot = await container.get(Bot)
    try:
        await setup_bot(bot)
        await dp.start_polling(bot)
    finally:
        await container.close()

if __name__ == "__main__":
    asyncio.run(main())
