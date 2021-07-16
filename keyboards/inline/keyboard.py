from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup()

get_apod = InlineKeyboardButton(text='Get Astronomy Picture of the Day', callback_data='get_apod')
choice.insert(get_apod)
