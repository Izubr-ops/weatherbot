import requests
from Token import GEO_YAPI

def coords(city):
    url = f"https://geocode-maps.yandex.ru/1.x/?format=json&apikey={GEO_YAPI}&geocode={city}"
    r = requests.get(url)
    responce = r.json()["response"]
    lat, lon = responce["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split()

    return lat, lon
