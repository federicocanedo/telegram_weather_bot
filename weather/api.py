import os
import requests

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{WEATHER_API_URL}?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"El clima en {city} es {description} con una temperatura de {temp}°C."
    elif response.status_code == 404:
        return "Ciudad no encontrada. Por favor, verifique el nombre de la ciudad e intente nuevamente."
    else:
        return "Hubo un error al obtener los datos del clima. Por favor, intente nuevamente más tarde."
