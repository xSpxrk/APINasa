from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helpers.get_donki import *

donki = InlineKeyboardMarkup(row_width=1)

cme = InlineKeyboardButton(text='Coronal Mass Ejection Analysis Information', url=get_cme())

ips = InlineKeyboardButton(text='Interplanetary Shock', url=get_ips())

flr = InlineKeyboardButton(text='Solar Flare', url=get_flr())

sep = InlineKeyboardButton(text='Solar Energetic Particle', url=get_sep())

rbe = InlineKeyboardButton(text='Radiation Belt Enhancement ', url=get_rbe())

hss = InlineKeyboardButton(text='Hight Speed Stream', url=get_hss())

cancel = InlineKeyboardButton(text='Cancel', callback_data='cancel')


donki.insert(cme)
donki.insert(ips)
donki.insert(flr)
donki.insert(sep)
donki.insert(rbe)
donki.insert(hss)
donki.insert(cancel)
