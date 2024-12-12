from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile

picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    photo = FSInputFile("images/Riri.jpg")
    await message.answer_photo(
        photo = photo,
        caption = "maybe u like Riri"
    )