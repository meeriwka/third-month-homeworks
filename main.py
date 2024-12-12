import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from handlers.random import random_router
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.my_info import myinfo_router
from handlers.other_messages import echo_router



token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()




async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_router)
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
