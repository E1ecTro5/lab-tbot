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

        current_weather = data["weather"][0]["main"]
        current_description = str(data['weather'][0]['description']).capitalize()
        current_temperature = data["main"]["temp"]
        current_feels_like = data["main"]["feels_like"]
        current_wind_speed = data["wind"]["speed"]
        current_cloudiness = data["clouds"]["all"]

        city_name = city_name.capitalize()

        return (f"Погода в {city_name} сейчас {current_weather}. {current_description}.\n"
                f"Температура: {current_temperature}°C.\n"
                f"Ощущается как: {current_feels_like}°C.\n"
                f"Скорость ветра: {current_wind_speed}м/с.\n"
                f"Облачность: {current_cloudiness}%.")

    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")
        return f"Ошибка HTTP запроса!"
    except Exception as err:
        print(f"Произошла ошибка: {err}")
        return f"Произошла ошибка!"