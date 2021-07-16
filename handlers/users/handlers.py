from loader import dp
from aiogram import types
from loader_templates import load_greeting_template
from config import BOT_NAME
from DataBase.db_requests import add_user, is_user_exist


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user
    id = user['id']
    username = user['username']
    is_bot = user['is_bot']
    first_name = user['first_name']
    last_name = user['last_name']
    if not is_user_exist(id):
        add_user(id, username, is_bot, first_name, last_name)
    await message.answer(load_greeting_template(username, BOT_NAME))
