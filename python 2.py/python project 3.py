import tkinter as tk
import requests

# OpenWeatherMap API endpoint and your API key (replace with your API key)
API_KEY = "74d49e859324a459cace3b65937c3e53"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather():
    # Get the city name from the entry widget
    city_name = city_entry.get()

    # Construct the URL for the weather API call
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}"

    # Fetch the data
    response = requests.get(complete_url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract the necessary information
        main = data["main"]
        wind = data["wind"]
        weather_description = data["weather"][0]["description"]

        # Temperature in Kelvin; convert it to Celsius or Fahrenheit
        temperature_k = main["temp"]
        temperature_c = temperature_k - 273.15
        temperature_f = (temperature_c * 9/5) + 32

        humidity = main["humidity"]
        wind_speed = wind["speed"]

        # Display the weather information in a label widget
        weather_info_label.config(text=f"Temperature (C): {round(temperature_c, 2)}\nTemperature (F): {round(temperature_f, 2)}\nWeather: {weather_description}\nHumidity (%): {humidity}\nWind Speed (m/s): {wind_speed}")

    else:
        # Display an error message if the API call fails
        error_label.config(text="Could not fetch weather data. Please check the city name and try again.")

# Create the main window
window = tk.Tk()

# Apply the CSS
window.title("Weather App")
window.geometry("400x500")
window.configure(bg='#ea9999')

# Create the city name entry widget
city_label = tk.Label(window, text="Enter city name:", bg='#ea9999', font=('Arial', 14))
city_label.pack()
city_entry = tk.Entry(window, bg='#f0f0f0', font=('Arial', 14))
city_entry.pack()

# Create the "Get Weather" button
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather, bg='#007bff', fg='#fff', font=('Arial', 14))
get_weather_button.pack()

# Create the label widget to display the weather information
weather_info_label = tk.Label(window, text="", bg='#ea9999', font=('Arial', 14))
weather_info_label.pack()

# Create the error label widget
error_label = tk.Label(window, text="", bg='#ea9999', font=('Arial', 14))
error_label.pack()



# Start the main loop
window.mainloop()