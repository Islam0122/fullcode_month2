import asyncio

from aiogram import Bot, Dispatcher
from config import Config, load_config
from handlers.base_commands_start import router_start
from keyboards.menu import p

async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router_start)


    await bot.set_my_commands(commands=p)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())