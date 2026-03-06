from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
router_contact = Router()

@router_contact.message(Command('contact'))
async def contact(message: Message):
    await message.answer("fndhsfjkdshkfjds")