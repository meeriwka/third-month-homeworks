import asyncio
import logging

from bot_config import dp, bot, db
from handlers.random import random_router
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.my_info import myinfo_router
from handlers.other_messages import echo_router
from handlers.review_dialogue import review_router

async def on_startup(bot):
    db.create_tables()

async def main():
    #регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    dp.include_router(review_router)
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
