from aiogram import Router, types
from aiogram.filters import Command
from random import choice

random_router = Router()


@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    names = ['Billie Eilish', 'Justin Timberlake', 'Zivert', 'Kanye West', 'Rihanna']
    await message.answer(choice(names))