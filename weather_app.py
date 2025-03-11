# ! Comments are for me to understand parts of what my code does if I look back on it in the future. Also to explain what the code does! :)

print("This application will give you the current weather forecast for your city.")
input("\nPress Enter to continue\n")

# Hardcoded weather data for predefined cities
# Format: { "Country": { "City": { "temperature": X, "condition": "Y", "wind_speed": Z, "humidity": W } } }
WEATHER_DATA = {
    "USA": {
        "New York": {"temperature": 18, "condition": "Sunny", "wind_speed": 10, "humidity": 60},
        "Los Angeles": {"temperature": 25, "condition": "Clear", "wind_speed": 5, "humidity": 50},
    },
    "Canada": {
        "Toronto": {"temperature": 12, "condition": "Cloudy", "wind_speed": 15, "humidity": 70},
        "Vancouver": {"temperature": 14, "condition": "Rainy", "wind_speed": 20, "humidity": 80},
    },
    "UK": {
        "London": {"temperature": 10, "condition": "Rainy", "wind_speed": 12, "humidity": 85},
        "Manchester": {"temperature": 9, "condition": "Cloudy", "wind_speed": 10, "humidity": 75},
    },
    "Australia": {
        "Sydney": {"temperature": 22, "condition": "Sunny", "wind_speed": 8, "humidity": 55},
        "Melbourne": {"temperature": 18, "condition": "Windy", "wind_speed": 25, "humidity": 65},
    },
}

# Function to display a welcome message
def display_welcome():
    print("Welcome to the Weather Forecast Application!")
    print("You can choose from the following countries and cities:\n")

# Function to display available countries and cities
def display_countries_and_cities():
    for country, cities in WEATHER_DATA.items():
        print(f"Country: {country}")
        print("Cities:", ", ".join(cities.keys()))
        print()

# Function to get a valid country from the user
def get_country_input():
    while True:
        country = input("Enter the name of the country: ").title()
        if country in WEATHER_DATA:
            return country
        print("Country not found. Please choose from the list above.")

# Function to get a valid city from the user
def get_city_input(country):
    while True:
        city = input(f"Enter the name of a city in {country}: ").title()
        if city in WEATHER_DATA[country]:
            return city
        print("City not found. Please choose from the list above.")

# Function to fetch weather data from hardcoded data
def fetch_weather_data(country, city):
    return WEATHER_DATA[country][city]

# Function to display weather data
def display_weather(city, weather_data):
    print(f"\nWeather forecast for {city}:")
    print(f"Current Temperature: {weather_data['temperature']}°C")
    print(f"Condition: {weather_data['condition']}")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")
    print(f"Humidity: {weather_data['humidity']}%")

# Function to thank the user
def thank_user():
    print("\nThank you for using the Weather Forecast Application. Have a great day!")

# Main function to run the program
def main():
    display_welcome()
    display_countries_and_cities()

    while True:
        # Get country and city from the user
        country = get_country_input()
        city = get_city_input(country)

        # Fetch and display weather data
        weather_data = fetch_weather_data(country, city)
        display_weather(city, weather_data)

        # Ask the user if they want to check another city
        retry = input("\nWould you like to check the weather for another city? (yes/no): ").lower()
        if retry != 'yes':
            break

    thank_user()

# Run the program
if __name__ == "__main__":
    main()