from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dishka.integrations.aiogram import FromDishka

from src.repositories.subscriber import SubscriberRepository

router = Router()

@router.message(CommandStart())
async def cmd_start(
    message: Message,
    repository: FromDishka[SubscriberRepository],
):
    subscriber = await repository.get_by_chat_id(message.chat.id)
    if not subscriber:
        await repository.create(
            chat_id=message.chat.id,
            username=message.from_user.username if message.from_user else None,
        )

        await message.answer("Привет! Ты подписан на уведомления.")