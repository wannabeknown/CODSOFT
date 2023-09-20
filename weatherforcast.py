import requests

def get_weather_data(location):
    api_key = 'YOUR_API_KEY'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return data
        else:
            print("Error: Unable to fetch weather data. Please check your input.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather_data(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        weather_description = weather_data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {weather_description}")
    else:
        print("No weather data available.")
def main():
    print("Welcome to the Weather Forecast Application!")
    location = input("Enter a city name or zip code: ")

    weather_data = get_weather_data(location)

    display_weather_data(weather_data)
if __name__ == "__main__":
    main()