from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User

"""
C Create
R Read
U Update
D Delete
"""
""" GET ALL USERS """
async def orm_get_users(session: AsyncSession):
    result = await session.execute(select(User))
    return result.scalars().all()


""" GET USER BY ID """
async def orm_get_user(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()


""" GET USER BY TELEGRAM ID """
async def orm_get_user_by_telegram_id(session: AsyncSession, telegram_id: int):
    result = await session.execute(
        select(User).where(User.telegram_id == telegram_id)
    )
    return result.scalar_one_or_none()


""" ADD USER """
async def orm_add_user(session: AsyncSession, telegram_id: int, username: str):
    new_user = User(
        telegram_id=telegram_id,
        username=username
    )

    try:
        session.add(new_user)
        await session.commit()
        return new_user

    except IntegrityError:
        await session.rollback()
        return None