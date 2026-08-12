


from aiogram import Bot
from dishka import Provider, Scope, provide

from src.repositories.subscriber import SubscriberRepository
from src.services.deployment import DeploymentService
from src.services.notify import TelegramNotifier


class ServiceProvider(Provider):

    @provide(scope=Scope.APP)
    def telegram_notifier(self, bot: Bot) -> TelegramNotifier:
        return TelegramNotifier(bot)

    @provide(scope=Scope.REQUEST)
    def deployment_service(self, repository: SubscriberRepository, notifier: TelegramNotifier) -> DeploymentService:
        return DeploymentService(repository=repository, notifier=notifier)