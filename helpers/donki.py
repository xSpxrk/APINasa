from config import API_KEY
import requests


def get_cme():
    url = 'https://api.nasa.gov/DONKI/CME'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    last = content[-1]['cmeAnalyses']
    link = last[0]['link']
    return link


def get_ips():
    url = 'https://api.nasa.gov/DONKI/IPS'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    link = content[-1]['link']
    return link


def get_flr():
    url = 'https://api.nasa.gov/DONKI/FLR'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    link = content[-1]['link']
    return link


def get_sep():
    url = 'https://api.nasa.gov/DONKI/SEP'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    last = content[-1]
    return last['link']


def get_rbe():
    url = 'https://api.nasa.gov/DONKI/RBE'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    last = content[-1]
    return last['link']


def get_hss():
    url = 'https://api.nasa.gov/DONKI/HSS'
    params = {'api_key': API_KEY}
    content = requests.get(url, params).json()
    last = content[-1]

    return last['link']
