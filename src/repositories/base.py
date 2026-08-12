from src.models.base import Base
from sqlalchemy.ext.asyncio import AsyncSession

class SQLAlchemyRepository[M: Base]:
    model: type[M]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, **kwargs) -> M:
        obj = self.model(**kwargs)
        return await self.save(obj)

    async def save(self, obj: M) -> M:
        self.session.add(obj)
        await self.session.flush()
        return obj

    async def get(self, id: int) -> M | None:
        return await self.session.get(self.model, id)

    async def delete(self, obj: M) -> None:
        await self.session.delete(obj)

    async def exists(self, id: int) -> bool:
        return await self.get(id) is not None