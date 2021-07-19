from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

default = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

apod = KeyboardButton(text='Get Astronomy Picture of the Day')

donki = KeyboardButton(text='Get last The Space Weather Database Of Notifications, Knowledge, Information')

mars_photos = KeyboardButton(text="Get yesterday's mars photos")

default.insert(apod)
default.insert(donki)
default.insert(mars_photos)

