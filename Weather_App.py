
import requests

API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("===== Basic Weather App =====")

city = input("Enter city name: ").strip()

if not city:
    print("Error: City name cannot be empty.")
else:
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        if response.status_code == 200:
            data = response.json()

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n===== Current Weather =====")
            print(f"City: {data['name']}")
            print(f"Temperature: {temperature_c:.1f} °C")
            print(f"Temperature: {temperature_f:.1f} °F")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition.title()}")
            print(f"Wind Speed: {wind_speed} m/s")

        elif response.status_code == 404:
            print("Error: City not found. Check the city name.")

        elif response.status_code == 401:
            print("Error: Invalid API key or key not activated.")

        else:
            print(f"Weather API error: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Check your internet connection.")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    except (KeyError, IndexError, TypeError, ValueError):
        print("Error: Unexpected weather data received.")
