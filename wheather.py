import requests  # Import the requests library to make HTTP requests

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = "YOUR_API_KEY"

# Function to get and print the weather data for a specified city
def get_weather(city_name):
    try:
        # Construct the API URL with the city name, API key, and units in metric (Celsius)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        
        # Send a GET request to the OpenWeatherMap API and store the response
        response = requests.get(url)
        # Convert the response data from JSON format to a Python dictionary
        data = response.json()

        # Extract the temperature, humidity, and weather description from the data
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        # Print the weather details to the console
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")  # Display the temperature in Celsius
        print(f"Humidity: {humidity}%")  # Display the humidity percentage
        print(f"Conditions: {weather_description}")  # Display the weather conditions

    # Handle exceptions that may occur during the API request
    except Exception as e:
        print(f"Error fetching weather data: {e}")  # Print an error message

# Main function that prompts the user for a city name and gets the weather data
def main():
    # Ask the user to enter the name of a city
    city_name = input("Enter a city name: ")
    # Call the get_weather function with the entered city name
    get_weather(city_name)

# Check if the script is run directly and not imported as a module
if __name__ == "__main__":
    # If the script is run directly, execute the main function
    main()
