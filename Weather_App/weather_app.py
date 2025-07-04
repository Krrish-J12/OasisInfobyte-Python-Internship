import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# Your OpenWeatherMap API key
api_key = "ea80cc886b6f2536c9718427ea40b8ec"
current_unit = "metric"

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x450")
root.config(bg="#DFF6FF")

# GUI elements created first
title_label = tk.Label(root, text="Weather App", font=("Arial", 24), bg="#DFF6FF")
title_label.pack(pady=20)

city_entry = tk.Entry(root, font=("Arial", 14), width=20, bg="#ffffff")
city_entry.pack(pady=10)

icon_label = tk.Label(root, bg="#f0f0f0")  # ✅ THIS must be created before get_weather()
icon_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0")
result_label.pack(pady=10)

# Fetch weather
def get_weather():
    global current_unit
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={current_unit}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"].title()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        temp_unit = "°C" if current_unit == "metric" else "°F"
        wind_unit = "m/s" if current_unit == "metric" else "mph"

        result = f"Weather: {weather}\nTemperature: {temperature}{temp_unit}\nHumidity: {humidity}%\nWind Speed: {wind_speed} {wind_unit}"
        result_label.config(text=result)

        # Fetch weather icon
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_response = requests.get(icon_url)
        icon_img = Image.open(BytesIO(icon_response.content)).resize((100, 100), Image.Resampling.LANCZOS)
        icon_photo = ImageTk.PhotoImage(icon_img)
        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo # type: ignore
    else:
        result_label.config(text="Error fetching data.")

# Toggle unit
def toggle_unit():
    global current_unit
    current_unit = "imperial" if current_unit == "metric" else "metric"
    toggle_btn.config(text=f"Switch to {'Celsius' if current_unit == 'imperial' else 'Fahrenheit'}")
    get_weather()

# Buttons
get_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 14), bg="#4caf50", fg="#ffffff")
get_btn.pack(pady=10)

toggle_btn = tk.Button(root, text="Toggle Unit", command=toggle_unit, font=("Arial", 14), bg="#2196f3", fg="#ffffff")
toggle_btn.pack(pady=10)

# Start GUI
root.mainloop()
