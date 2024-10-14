from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
import os
from serviсes.db_commands import register_user
# Загрузка переменных окружения
load_dotenv()

# Инициализация бота и диспетчера
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Hello! This bot is for expensing your costs)")

    if message.from_user.is_bot: return

    await register_user(message)

# Запуск long polling
if __name__ == "__main__":
    dp.run_polling(bot)
