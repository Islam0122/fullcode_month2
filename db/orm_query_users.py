from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
import asyncio
from .model import User, Question

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

async  def add_question(session: AsyncSession, question, option_a, option_b, option_c, option_d,correct):
    new_question = Question(
        question=question,
        option_a=option_a,
        option_b=option_b,
        option_c=option_c,
        option_d=option_d,
        correct=correct
    )
    session.add(new_question)
    await session.commit()
    return new_question

