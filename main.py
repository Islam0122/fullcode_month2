import asyncio
from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers.base_commands_start import router_start
from handlers.income_command import router_income
from handlers.expense_command import router_expense
from keyboards.menu import commands

async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router_start)
    dp.include_router(router_income)
    dp.include_router(router_expense)

    await bot.set_my_commands(commands=commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())