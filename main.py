import asyncio
import os
from dotenv import load_dotenv
from  aiogram import Bot,Dispatcher
from aiogram.types import Message,FSInputFile
from aiogram.filters import Command

load_dotenv()

Token = os.getenv("Token")

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: Message):
    await message.answer_photo(
        photo=FSInputFile("img2.png"),
        caption="👋 Добро пожаловать в Finance Bot!\n\n"
        "Этот бот поможет учитывать доходы и расходы.",
    )
@dp.message(Command('help'))
async def help_command(message: Message):
    await message.answer_photo(
        photo=FSInputFile("./img2.png"),
        caption="Я помогу вам рассчитать ваши расходы "

    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
