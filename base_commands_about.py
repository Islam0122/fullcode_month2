from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
router_about= Router()





@router_about.message(Command('about'))
async def about(message: Message):
    await message.answer("fsdjfhjsdhjfksd")