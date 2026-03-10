from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def cancel_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="❌ Отменить"))
    return builder.as_markup(resize_keyboard=True)

def confirm_kb():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="✅ Подтвердить"),
        KeyboardButton(text="❌ Отменить")
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)