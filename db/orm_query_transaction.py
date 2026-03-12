from sqlalchemy import select, delete, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Transaction


""" ADD TRANSACTION """
async def orm_add_transaction(
        session: AsyncSession,
        user_id: int,
        type: str,
        amount: int,
        category: str | None = None,
        description: str | None = None
):
    new_transaction = Transaction(
        user_id=user_id,
        type=type,
        amount=amount,
        category=category,
        description=description
    )

    session.add(new_transaction)
    await session.commit()
    return new_transaction


""" GET ALL USER TRANSACTIONS """
async def orm_get_transactions(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(Transaction).where(Transaction.user_id == user_id)
    )
    return result.scalars().all()


""" GET ONE TRANSACTION """
async def orm_get_transaction(session: AsyncSession, transaction_id: int):
    result = await session.execute(
        select(Transaction).where(Transaction.id == transaction_id)
    )
    return result.scalar_one_or_none()


""" GET LAST TRANSACTIONS """
async def orm_get_last_transactions(
        session: AsyncSession,
        user_id: int,
        limit: int = 5
):
    result = await session.execute(
        select(Transaction)
        .where(Transaction.user_id == user_id)
        .order_by(Transaction.id.desc())
        .limit(limit)
    )
    return result.scalars().all()


""" UPDATE TRANSACTION """
async def orm_update_transaction(
        session: AsyncSession,
        transaction_id: int,
        amount: int | None = None,
        category: str | None = None,
        description: str | None = None
):

    values = {}

    if amount is not None:
        values["amount"] = amount

    if category is not None:
        values["category"] = category

    if description is not None:
        values["description"] = description

    await session.execute(
        update(Transaction)
        .where(Transaction.id == transaction_id)
        .values(**values)
    )

    await session.commit()


""" DELETE TRANSACTION """
async def orm_delete_transaction(session: AsyncSession, transaction_id: int):
    await session.execute(
        delete(Transaction).where(Transaction.id == transaction_id)
    )
    await session.commit()


""" GET USER BALANCE """
async def orm_get_balance(session: AsyncSession, user_id: int):

    result = await session.execute(
        select(func.sum(Transaction.amount))
        .where(Transaction.user_id == user_id)
        .where(Transaction.type == "income")
    )

    income = result.scalar() or 0

    result = await session.execute(
        select(func.sum(Transaction.amount))
        .where(Transaction.user_id == user_id)
        .where(Transaction.type == "expense")
    )

    expense = result.scalar() or 0

    return income - expense