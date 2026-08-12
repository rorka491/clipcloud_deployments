from sqlalchemy import select

from src.repositories.base import SQLAlchemyRepository
from src.models.subscriber import Subscriber


class SubscriberRepository(SQLAlchemyRepository[Subscriber]):
    model = Subscriber

    async def get_by_chat_id(self, chat_id: int) -> Subscriber | None:
        stmt = select(self.model).where(
            self.model.chat_id == chat_id,
        )
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()

    async def get_active(self) -> list[Subscriber]:
        stmt = select(self.model).where(self.model.is_active.is_(True))
        result = await self.session.execute(stmt)
        return list(result.scalars().all())