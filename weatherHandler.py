import requests

def get_weather(city_name, api_key):
    if city_name is None or city_name == '':
        return "Ошибка запроса!"

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',
        'lang': 'en'
    }

    try:
        response = requests.get(url, params=params)

        response.raise_for_status()
        data = response.json()

        currentWeather = data["weather"][0]["main"]
        currentDescription = data['weather'][0]['description']
        currentTemperature = data["main"]["temp"]
        currentFeelsLike = data["main"]["feels_like"]
        currentWindSpeed = data["wind"]["speed"]
        currentCloudiness = data["clouds"]["all"]

        return (f"В городе {city_name} сейчас {currentWeather}."
                f"{currentDescription}"
                f"Температура: {currentTemperature}."
                f"Ощущается как: {currentFeelsLike}."
                f"Скорость ветра: {currentWindSpeed}."
                f"Облачность: {currentCloudiness}")

    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        return f"Ошибка HTTP запроса!"
    except Exception as err:
        print(f"Произошла ошибка: {err}")
        return f"Произошла ошибка!"