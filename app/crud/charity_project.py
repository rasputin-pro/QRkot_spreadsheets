from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


class CRUDCharityProject(CRUDBase):

    @staticmethod
    async def update(
            db_obj: CharityProject,
            obj_in: CharityProjectUpdate,
            session: AsyncSession,
    ) -> CharityProject:
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    @staticmethod
    async def remove(
            db_obj: CharityProject,
            session: AsyncSession,
    ) -> CharityProject:
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    @staticmethod
    async def get_charity_project_id_by_name(
            charity_project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_charity_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == charity_project_name
            )
        )
        return db_charity_project_id.scalars().first()


charity_project_crud = CRUDCharityProject(CharityProject)
