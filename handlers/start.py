from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup

from handlers.review_dialogue import review_router

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ]

        ]

    )
    await message.answer(f'Здравствуйте, {name}!', reply_markup=kb)

# @start_router.callback_query(F.data == "review")
# async def start_review(callback: types.callback_query):
#     await callback.answer()
#     await callback.message.answer("Оставить отзыв")