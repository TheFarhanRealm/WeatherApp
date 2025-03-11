# ! Comments are for me to understand parts of what my code does if I look back on it in the future. Also to explain what the code does! :)
print("This application will give you the current weather forecast for your city.")

input("\nPress Enter to continue\n")

import os  
import requests
from dotenv import load_dotenv  


load_dotenv()


API_KEY = os.getenv("API_KEY")


if not API_KEY:
    raise ValueError("Error: API key is missing. Make sure it's set in the .env file.")


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def display_welcome():
    print("Welcome to the Weather Forecast Application!")


def get_city_input():
    while True:
        city = input("Enter the name of the city to get the weather forecast: ").title()  #Capitalize the city name properly
        if city.strip():  #makes sure the city name is not empty
            return city
        print("City name cannot be empty. Please try again.")

#Function to fetch weather data from OpenWeather API
def fetch_weather_data(city):
    params = {
        'q': city,  # City name
        'appid': API_KEY,
        'units': 'metric',  #Gets temperature in Celsius
        'lang': 'en'
    }

    #Send GET request to OpenWeather API.
    print(f"Fetching weather data for {city}...")  #Debugging part: check the city being used
    response = requests.get(BASE_URL, params=params)

    #Checks to see if the response was successful. 200 means successful
    if response.status_code == 200:
        data = response.json()

        #Check if the city exists in the response. status code 200 and "cod" should be 200
        if data.get("cod") == 200:
            weather_info = {
                'temperature': data['main']['temp'],
                'condition': data['weather'][0]['description'].title(),
                'wind_speed': data['wind']['speed'],
                'humidity': data['main']['humidity']
            }
            return weather_info
        else:
            print(f"Error: {data.get('message', 'Unknown error occurred.')}")
            return None
    else:
        #Handle errors with the response
        handle_api_error(response.status_code, response.text)
        return None

#Function to handle API errors
def handle_api_error(status_code, response_text):
    if status_code == 401:
        print("Error: Unauthorized. Please check your API key.")
    elif status_code == 404:
        print("Error: City not found. Please check the city name and try again.")
    else:
        print(f"Error occurred while fetching data: {status_code}")
        print("Response:", response_text)  #This will print out my error message from the API

#Function to display weather data
def display_weather(city, weather_data):
    if weather_data:
        print(f"\nWeather forecast for {city}:")
        print(f"Current Temperature: {weather_data['temperature']}°C")
        print(f"Condition: {weather_data['condition']}")
        print(f"Wind Speed: {weather_data['wind_speed']} km/h")
        print(f"Humidity: {weather_data['humidity']}%")
    else:
        print("Could not fetch weather data. Please try again later.")

def thank_user():
    print("\nThank you for using the Weather Forecast Application. Have a great day!")

#Function to fetch and display weather data
def fetch_and_display_weather(city):
    weather_data = fetch_weather_data(city)
    display_weather(city, weather_data)
    return weather_data is not None

#Main function to run the program.
def main():
    display_welcome()
    while True:
        city = get_city_input()
        fetch_and_display_weather(city)

        #Ask the user if they want to check another city
        retry = input("\nWould you like to check the weather for another city? (yes/no): ").lower()
        if retry != 'yes':
            break

    thank_user()

# __name__ is a special variable in Python that determines if the script is being run directly or imported as a module.
if __name__ == "__main__":
    main()