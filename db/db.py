from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker

# Middleware для автоматической передачи сессии базы данных в handlers

class DataBaseSession(BaseMiddleware):
    # Конструктор принимает session_pool (фабрику создания сессий SQLAlchemy)
    def __init__(self, session_pool: async_sessionmaker):
        self.session_pool = session_pool

    # Основной метод middleware, который вызывается при каждом обновлении Telegram
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],  # следующий handler
        event: TelegramObject,  # событие Telegram (Message, CallbackQuery и т.д.)
        data: Dict[str, Any],   # словарь данных, передаваемый между middleware и handler
    ) -> Any:

        # Создаем новую асинхронную сессию базы данных
        async with self.session_pool() as session:

            # Добавляем session в data, чтобы можно было использовать в handler
            data['session'] = session
            return await handler(event, data)