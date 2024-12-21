
from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


review_router = Router()

class RestaurantReview(StatesGroup):
    name = State()
    instagram_username = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@review_router.callback_query(F.data == "review")
async def start_review(callback: types.callback_query, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Ваше имя?")
    await state.set_state(RestaurantReview.name)

@review_router.message(RestaurantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer("Ваш инстаграм?")
    await state.set_state(RestaurantReview.instagram_username)

@review_router.message(RestaurantReview.instagram_username)
async def process_inst(message: types.Message, state: FSMContext):
    await state.update_data(instagram_username=message.text)
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="плохо",callback_data='плохо')],
            [
                types.InlineKeyboardButton(text="удовлетворительно",callback_data='удов')
            ],
            [
                types.InlineKeyboardButton(text="хорошо",callback_data='хорошо')
            ],
            [
                types.InlineKeyboardButton(text="отлично", callback_data='отл')
            ]
        ]
    )
    await message.answer("Ваша оценка качеству еды", reply_markup = kb)
    await state.set_state(RestaurantReview.food_rating)

@review_router.callback_query(RestaurantReview.food_rating)
async def process_foodrating(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.update_data(food_rating = callback.data)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="плохо")],
            [
                types.KeyboardButton(text="удовлетворительно")
            ],
            [
                types.KeyboardButton(text="хорошо")
            ],
            [
                types.KeyboardButton(text="отлично")
            ]
        ]
    )
    if callback.data in ("плохо", "удовлетворительно", "хорошо", "отлично"):

        await callback.message.answer("Ваша оценка по чистоте заведения от 1 до 5?", reply_markup = kb)
        await state.set_state(RestaurantReview.cleanliness_rating)

@review_router.message(RestaurantReview.cleanliness_rating)
async def process_cleanliness(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating = message.text)
    kb = types.ReplyKeyboardRemove()
    if message.text in ("плохо", "удовлетворительно", "хорошо", "отлично"):

        await message.answer("Ваши комментарии или жалобы", reply_markup = kb)
        await state.set_state(RestaurantReview.extra_comments)

@review_router.message(RestaurantReview.extra_comments)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments = message.text)
    basa = await state.get_data()
    print(basa)
    await state.clear()
    await message.answer('Thank u')
