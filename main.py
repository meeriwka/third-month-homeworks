import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
from random import choice


token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message):
    name = message.from_user.first_name
    await message.answer(f'Здравствуйте, {name}!')



@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    identificator = message.from_user.id
    await message.answer(f'Ваш ID: {identificator}')
    name = message.from_user.first_name
    await message.answer(f'Ваше имя: {name}')
    user = message.from_user.username
    await message.answer(f'Ваш никнейм: {user}')


@dp.message(Command("random"))
async def random_handler(message: types.Message):
    names = ['Billie Eilish', 'Justin Timberlake', 'Zivert', 'Kanye West', 'Rihanna']
    await message.answer(choice(names))



@dp.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)




async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
