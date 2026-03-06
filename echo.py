from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_echo = Router()

@router_echo.message()
async def echo(message: Message):
    await message.delete()