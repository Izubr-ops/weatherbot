import os
from dotenv_vault import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
WEATHER_YAPI = os.getenv("WEATHER_YAPI")
GEO_YAPI = os.getenv("GEO_YAPI")

