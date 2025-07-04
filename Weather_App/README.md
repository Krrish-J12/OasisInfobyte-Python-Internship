# 🌦️ Weather Application

A user-friendly GUI-based Python application that provides real-time weather updates using the OpenWeatherMap API.

---

## 🔧 Features

- Enter any city name and get current weather details
- Displays:
  - Weather condition (e.g., Clear, Rainy)
  - Temperature
  - Humidity
  - Wind Speed
  - Weather icon
- Toggle between **Celsius** and **Fahrenheit**
- Clean and modern Tkinter GUI

---

## 🛠 Technologies Used

- `Tkinter` – Python GUI library
- `requests` – For API calls
- `Pillow (PIL)` – To handle weather icon images
- `OpenWeatherMap API` – For real-time weather data

---

## 📁 Project Structure

weather_app/
│
└── weather_app.py # Main GUI weather application

---

## ⚙️ Setup Instructions

### 1. Install required libraries:
```bash
pip install requests pillow
```

### Add your OpenWeatherMap API key:
## Open weather_app.py and replace this line:
api_key = "ea8ccc886b6fxxx36c9718427ea40bxxc"

# with your own API key (you can register at https://openweathermap.org/api).

## How to Run
1. Install dependencies (`requests`, `Pillow`)
2. Run `weather_app.py`
3. Enter city and fetch weather data