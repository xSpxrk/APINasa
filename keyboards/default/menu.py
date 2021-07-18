from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

default = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

apod = KeyboardButton(text='Get Astronomy Picture of the Day')
donki = KeyboardButton(text='Get last The Space Weather Database Of Notifications, Knowledge, Information')
default.insert(apod)
default.insert(donki)

