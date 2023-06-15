import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm File to URL!\nSend a File")


@dp.message_handler(content_types=['document'])
async def send_welcome(message: types.Message):
    file_id = message.document.file_id
    get = await bot.get_file(file_id)
    path = get.file_path
    await message.answer(f"https://api.telegram.org/file/bot{API_TOKEN}/{path}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)