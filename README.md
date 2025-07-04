# OasisInfobyte-Python-Internship Projects
Python Internship Projects - Chat Application, Weather App, and Voice Assistant.

[![GitHub repo stars](https://img.shields.io/github/stars/Krrish-J12/OasisInfobyte-Python-Internship?style=social)](https://github.com/Krrish-J12/OasisInfobyte-Python-Internship)

Welcome to my portfolio repository showcasing **three key projects** developed during my Oasis Infobyte Python internship:

---

## 📂 Projects Overview

### 1. Chat Application
A real-time multi-client chat system built using Python's `socket` library, threading, and terminal UI enhancements.
- **Technologies**: Python, `socket`, `threading`, `colorama`
- **Features**: User nicknames, multi-client broadcasting, message handling

🔗 [View README](./Chat_Application/README.md)

---

### 2. Weather Application
A GUI desktop tool to fetch current weather using OpenWeatherMap API.
- **Technologies**: Python, `requests`, `tkinter`, `PIL`
- **Features**: City input, weather display, unit toggle, icon support

🔗 [View README](./Weather_App/README.md)

---

### 3. Voice Assistant
A voice-controlled assistant that:
- Listens via selected microphone
- Executes commands: open websites, fetch time/date, search, play YouTube songs
- **Technologies**: `sounddevice`, `speech_recognition`, `gTTS`, `pywhatkit`, `tkinter`

🔗 [View README](./Voice_Assistant/README.md)

---

## 📋 Final Summary
✔️ Consolidated summary of skills learned is in [Final_Summary.md](./Final_Summary.md)

---

## 🛠️ Setup & Installation

```bash
git clone https://github.com/Krrish-J12/OasisInfobyte-Python-Internship.git
cd OasisInfobyte-Python-Internship

# Setup virtual environment
python -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows PowerShell

# Install dependencies per project
pip install -r Chat_Application/requirements.txt
pip install -r Weather_App/requirements.txt
pip install -r Voice_Assistant/requirements.txt
