from sqlalchemy import select, delete, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from .model import UserStat

""" CRUD """
"""create"""
async def create_user_stats(session: AsyncSession, telegram_id: int, fullname,score):
    new_stat = UserStat(telegram_id=telegram_id, fullname=fullname, score=score)
    session.add(new_stat)
    await session.commit()

""" READ"""
async def read_user_stats(session: AsyncSession):
    res = await session.execute(select(UserStat))
    return res.scalars().all()

""" UPDATE """
async def update_user_stats(session: AsyncSession, telegram_id: int, fullname,score):
    res = update(UserStat).where(UserStat.telegram_id==telegram_id).values(fullname=fullname, score=score)
    await session.execute(res)
    await session.commit()

"""DELETE"""
async def delete_user_stats(session: AsyncSession, telegram_id: int):
    res = delete(UserStat).where(UserStat.telegram_id == telegram_id)
    res =  await session.execute(res)
    await session.commit()
