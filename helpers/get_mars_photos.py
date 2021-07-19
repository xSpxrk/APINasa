import requests
from datetime import date, timedelta
from config import API_KEY
from aiogram.types import InputMediaPhoto


def get_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
    yesterday = date.today() - timedelta(days=1)
    params = {'earth_date': yesterday, 'api_key': API_KEY}
    content = requests.get(url, params).json()
    images = content['photos']
    photos = []
    for img in images:
        media = InputMediaPhoto(img['img_src'])
        photos.append(media)
        print(len(photos))
        if len(photos) == 10:
            return photos
    return photos
