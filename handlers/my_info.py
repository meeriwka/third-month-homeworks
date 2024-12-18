from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()




@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    identificator = message.from_user.id
    await message.answer(f'Ваш ID: {identificator}')
    name = message.from_user.first_name
    await message.answer(f'Ваше имя: {name}')
    user = message.from_user.username
    await message.answer(f'Ваш никнейм: {user}')
