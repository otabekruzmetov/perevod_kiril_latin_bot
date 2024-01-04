import logging
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin, to_cyrillic

API_TOKEN = ""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom\nKrill Lotin botimizga xush kelibsiz\nMatningizni yuboring.")



@dp.message_handler()
async def echo(message: types.Message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    await message.answer(javob(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)