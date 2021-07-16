import requests

from keyboards.inline.keyboard import choice
from loader import dp
from aiogram import types
from loader_templates import load_greeting_template
from config import BOT_NAME, API_KEY
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
    await message.answer(load_greeting_template(username, BOT_NAME), reply_markup=choice)


def get_apod():
    url = 'https://api.nasa.gov/planetary/apod'
    api_key = API_KEY
    params = {'api_key': api_key}
    content = requests.get(url, params).json()
    title = content['title']
    image = content['url']
    print(image)
    return [image, title]


@dp.callback_query_handler(text_contains='get_apod')
async def send_apod(call: types.CallbackQuery):
    apod = get_apod()
    image = apod[0]
    title = apod[1]
    await call.message.delete()
    await call.bot.send_photo(chat_id=call.from_user.id, photo=image, caption=title)

