import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature (C)": data["main"]["temp"],
            "Weather": data["weather"][0]["description"].title(),
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
        return weather
    else:
        return {"Error": "City not found or invalid API key."}

if __name__ == "__main__":
    print("=== Weather App ===")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    result = get_weather(city, api_key)
    
    for key, value in result.items():
        print(f"{key}: {value}")
