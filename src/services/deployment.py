from src.repositories.subscriber import SubscriberRepository
from src.services.notify import TelegramNotifier


class DeploymentService:
    def __init__(
        self,
        repository: SubscriberRepository,
        notifier: TelegramNotifier,
    ):
        self.repository = repository
        self.notifier = notifier

    async def handle_push(self, payload: dict):
        subscribers = await self.repository.get_active()

        commit = payload["after"]
        author = payload["head_commit"]["author"]["name"]
        message = payload["head_commit"]["message"]

        text = (
            "🚀 Новый push в main\n\n"
            f"Автор: {author}\n"
            f"Коммит: {commit[:7]}\n"
            f"Сообщение: {message}"
        )

        await self.notifier.notify_all(
            subscribers,
            text,
        )