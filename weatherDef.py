import requests

from Token import WEATHER_YAPI
from geocoder import coords

city_info = {"Tokyo": {"lat" : 35.681671, "lon" : 139.753835, "name" : "Токио"},
             "New York": {"lat" : 40.714705, "lon" : -74.003246, "name" : "Нью-йорк"},
             "Moscow": {"lat" : 55.755696, "lon" : 37.617306, "name" : "Москва"}}

def weather(place):
    if place in city_info:
        lon = city_info[place]["lon"]
        lat = city_info[place]["lat"]
        name = city_info[place]["name"]
    else:
        lon, lat = coords(place)
        name = place
    lang = "en_US"
    limit = 1
    hours = False
    extra = False
    url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&[lang={lang}]"
    r = requests.get(url, headers={"X-Yandex-API-Key": WEATHER_YAPI})
    response = r.json()
    today = response["forecast"]
    todayShortWEth = today["parts"][0]
    weather = f'Погода в {name}:\n' \
              f'Дата {today["date"]}\n'\
              f'Восход {today["sunrise"]}\n'\
              f'Закат {today["sunset"]}\n'\
              f'Минимальная температура {todayShortWEth["temp_min"]}\n'\
              f'максимальная температура {todayShortWEth["temp_max"]}\n'\
              f'Ощущается как {todayShortWEth["feels_like"]}\n'\
              f'за окном {todayShortWEth["condition"]}\n'
    return weather



