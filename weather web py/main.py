import requests


def get_weather(city_or_zip, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_or_zip,
        'appid': api_key,
        'units': 'metric'  
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status() 
        data = response.json()

       
        if "name" in data and "main" in data and "weather" in data:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
            }
        else:
            print("Unexpected response structure:", data)
            return None

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print("City not found. Please check your input.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Error occurred: {err}")
    return None

def main():
    api_key = '07c7ffbd9a99cd7d11ff3dbc75ae7001'  
    city_or_zip = input("Enter city name or ZIP code: ")
    weather_data = get_weather(city_or_zip, api_key)
    
    if weather_data:
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Weather: {weather_data['description'].capitalize()}")
    else:
        print("Could not fetch weather data. Please check your input or try again later.")

if __name__ == "__main__":
    main()