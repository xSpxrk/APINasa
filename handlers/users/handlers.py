import requests

from keyboards.default.menu import default
from loader import dp
from aiogram import types
from loader_templates import load_greeting_template
from config import BOT_NAME, API_KEY, ADMIN_USERNAME
from DataBase.db_requests import add_user, is_user_exist, get_users_id
from aiogram.dispatcher.filters import Text
from keyboards.inline.donki import donki
from helpers.get_mars_photos import get_photos


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
    await message.answer(load_greeting_template(username, BOT_NAME), reply_markup=default)


@dp.message_handler(commands=['notify'])
async def notify_everyone(message: types.Message):
    """
    This is command to send users message
    """

    def is_admin(username):
        return username == ADMIN_USERNAME

    if is_admin(message.from_user.username):
        id_users = get_users_id()
        notification = message.get_args()
        for id_user in id_users:
            await message.bot.send_message(id_user, notification)
    else:
        await message.reply('You are not admin')


def get_apod():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    title = content['title']
    image = content['url']
    return [image, title]


@dp.message_handler(Text(equals='Get Astronomy Picture of the Day'))
async def send_apod(message: types.Message):
    apod = get_apod()
    image = apod[0]
    title = apod[1]

    await message.bot.send_photo(chat_id=message.from_user.id, photo=image, caption=title)


@dp.message_handler(Text(equals='Get last The Space Weather Database Of Notifications, Knowledge, Information'))
async def send_donki(message: types.Message):
    await message.answer(text='The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a '
                              'comprehensive on-line tool for space weather forecasters, scientists, and the general '
                              'space science community. DONKI provides chronicles the daily interpretations of space '
                              'weather observations, analysis, models, forecasts, and notifications provided by the '
                              'Space Weather Research Center (SWRC), comprehensive knowledge-base search '
                              'functionality to support anomaly resolution and space science research, intelligent '
                              'linkages, relationships, cause-and-effects between space weather activities and '
                              'comprehensive webservice API access to information stored in DONKI.',
                         reply_markup=donki)


@dp.callback_query_handler(text='cancel')
async def get_back(call: types.CallbackQuery):
    await call.message.delete()


@dp.message_handler(Text(equals="Get yesterday's mars photos"))
async def send_mp(message: types.Message):
    await message.bot.send_media_group(message.from_user.id, get_photos(), disable_notification=True)


