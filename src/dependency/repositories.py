from dishka import Provider, Scope, provide
from src.repositories.subscriber import SubscriberRepository
from sqlalchemy.ext.asyncio import AsyncSession


class RepositoryProvider(Provider):

    @provide(scope=Scope.REQUEST)
    def subscriber_repo(self, session: AsyncSession) -> SubscriberRepository:
        return SubscriberRepository(session=session)