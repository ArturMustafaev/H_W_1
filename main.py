from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
import logging
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Привет мой хозяин {message.from_user.full_name}")

@dp.message_handler(commands=['mem'])
async def mem(call: types.CallbackQuery):
    photo_1 = open("media/mem_1.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo_1)

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Какой самый лучший ЯП?"
    answers = ['Java', 'Pthon', 'Fortran', 'C++', 'JavaScript']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_3(call: types.CallbackQuery):

    question = "Ответы:"
    answers = [
        'Стажер',
        'Хомяк',
        'Собака',
        'Кот',
        'Я не знаю'
    ]
    photo = open("media/cat.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
