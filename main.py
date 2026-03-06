import asyncio

from aiogram import Bot, Dispatcher, types
from config import Config, load_config
from base_commands import router
from echo import router_echo
from base_command_help import router_help
from base_commands_about import router_about
from base_commands_contact import router_contact

async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router)
    dp.include_router(router_help)
    dp.include_router(router_about)
    dp.include_router(router_contact)

    dp.include_router(router_echo)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())