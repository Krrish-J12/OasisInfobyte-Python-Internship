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
- `python-dotenv` – To securely load environment variables

---

## 📁 Project Structure

weather_app/
│
├── weather_app.py # Main GUI weather application
├── .env # 🔒 Contains your real API key (NOT committed)
├── .env.example # 📄 Sample environment file (safe to share)
├── .gitignore # 🚫 Git ignore file to protect sensitive data
└── README.md # 📘 Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```
### 2. Install Required Libraries
```bash
pip install requests pillow python-dotenv
```
### 3. Setup Your Environment File
# Copy the example .env.example file and rename it to .env:
  cp .env.example .env

# Open the .env file and add your actual OpenWeatherMap API key:
  WEATHER_API_KEY=your_actual_api_key_here
  📝 You can get your API key from OpenWeatherMap

### ▶️ How to Run
```bash
python weather_app.py
```
# Then:

  -Enter a city name
  -Click "Get Weather"
  -Use the Toggle Unit button to switch between Celsius and Fahrenheit

# 🚫 Security Note
  This project uses a .env file to store sensitive API keys.
Make sure you do not commit .env to any public repository.
Your .gitignore should include:
```bash
.env
```

# 📄 License
  This project is licensed under the MIT License

---

✅ Now your README is complete, professional, secure, and internship-ready.

Let me know if you'd like help generating a `.zip` of the entire folder or uploading this project to GitHub with correct structure.
