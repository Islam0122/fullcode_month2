from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardRemove)

start_keyboard =  ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="/start"),
     KeyboardButton(text="/help"),
    KeyboardButton(text="/about")],
    [KeyboardButton(text="/contact")],
    [KeyboardButton(text="/help")],
])
