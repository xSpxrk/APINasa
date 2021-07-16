from aiogram import Bot, Dispatcher, types
from config import BOT_TOKEN
import logging

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)