from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile,CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession
from db.orm_query_users import orm_add_user
from text.messages import START_TEXT,ABOUT_TEXT,HELP_TEXT
from keyboards.inline_keyboard import start_keyboard,return_menu
router_start = Router()

@router_start.message(Command('start'))
async def start(message: Message,session: AsyncSession):
    await orm_add_user(session,message.from_user.id, message.from_user.username)
    await message.answer_photo(
        photo=FSInputFile("photo/img.png"),
        caption=START_TEXT,
        reply_markup=start_keyboard()
    )

@router_start.callback_query(F.data == "return_menu")
async def return_menu_command(callback:CallbackQuery):
    await callback.message.edit_caption(
        caption=START_TEXT,
        reply_markup=start_keyboard()
    )

@router_start.message(Command('about_bot'))
async def about_bot(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/img.png"),
        caption=ABOUT_TEXT,
        reply_markup=return_menu()
    )

@router_start.callback_query(F.data == "about_bot")
async def about_bot(callback:CallbackQuery):
    await callback.message.edit_caption(
        caption=ABOUT_TEXT,
        reply_markup=return_menu()
    )

@router_start.message(Command('help'))
async def help(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/img.png"),
        caption=HELP_TEXT,
        reply_markup=return_menu()
    )

@router_start.callback_query(F.data == "help")
async def help(callback: CallbackQuery):
    await callback.message.edit_caption(
        caption=HELP_TEXT,
        reply_markup=return_menu()
    )
