
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def  start_keyboard():
    builder = InlineKeyboardBuilder()

    builder.add(
        InlineKeyboardButton(text="➕ Добавить  доход", callback_data="add"),
        InlineKeyboardButton(text="➖ Добавить расход" , callback_data="minus"),
        InlineKeyboardButton(text="📊 Баланс",callback_data="balance"),
        InlineKeyboardButton(text="📜 История",callback_data="history"),
        InlineKeyboardButton(text="🤖 О боте", callback_data="about_bot"),
        InlineKeyboardButton(text="ℹ Помощь",callback_data="help")
    )
    builder.adjust(2,1)
    return builder.as_markup()

def return_menu():
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="⬅ Назад",callback_data="return_menu"),
    )
    return builder.as_markup()