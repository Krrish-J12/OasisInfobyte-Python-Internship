import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# ✅ Your OpenWeatherMap API key
api_key = "62a716e103618d44a2099a06053ca904"
current_unit = "metric"

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x450")
root.config(bg="#DFF6FF")

# Title
tk.Label(root, text="Weather App", font=("Arial", 24), bg="#DFF6FF").pack(pady=20)

# City input
city_entry = tk.Entry(root, font=("Arial", 14), width=20, bg="#ffffff")
city_entry.pack(pady=10)

# Weather icon placeholder
icon_label = tk.Label(root, bg="#DFF6FF")
icon_label.pack(pady=10)

# Weather result
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#DFF6FF")
result_label.pack(pady=10)

# Function: Get Weather
def get_weather():
    global current_unit
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={current_unit}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            temp_unit = "°C" if current_unit == "metric" else "°F"
            wind_unit = "m/s" if current_unit == "metric" else "mph"

            result = f"Weather: {weather}\nTemperature: {temperature}{temp_unit}\nHumidity: {humidity}%\nWind: {wind_speed} {wind_unit}"
            result_label.config(text=result)

            # Fetch icon
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_img = Image.open(BytesIO(requests.get(icon_url).content)).resize((100, 100))
            icon_photo = ImageTk.PhotoImage(icon_img)
            icon_label.config(image=icon_photo)
            icon_label.image = icon_photo # type: ignore
        else:
            result_label.config(text="City not found or API error.")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Function: Toggle unit
def toggle_unit():
    global current_unit
    current_unit = "imperial" if current_unit == "metric" else "metric"
    toggle_btn.config(text=f"Switch to {'Celsius' if current_unit == 'imperial' else 'Fahrenheit'}")
    get_weather()

# Buttons
tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14), bg="#4caf50", fg="white").pack(pady=10)
toggle_btn = tk.Button(root, text="Toggle Unit", command=toggle_unit, font=("Arial", 14), bg="#2196f3", fg="white")
toggle_btn.pack(pady=10)

# Start GUI
root.mainloop()
