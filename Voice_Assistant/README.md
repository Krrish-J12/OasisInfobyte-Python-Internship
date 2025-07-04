# 🗣️ Voice Assistant with GUI (Python)

A Python-based desktop voice assistant that listens to voice commands, performs tasks, and responds audibly with a friendly GUI for microphone selection.

---

## 🔧 Features

- 🎤 Microphone selector via GUI
- 🗣️ Recognizes voice commands and speaks responses
- 🔍 Performs actions like:
  - Opening YouTube/Google
  - Playing music on YouTube (manual click needed)
  - Searching the web
  - Wikipedia summaries
  - Telling time and date
- ⏯️ Voice-controlled pause/resume
- 🖼️ Custom background with responsive Tkinter GUI

---

## 🛠 Technologies Used

- `Tkinter` – GUI framework
- `speech_recognition` – For converting speech to text
- `gTTS` – Text-to-speech (Google Text-to-Speech)
- `sounddevice`, `scipy` – Recording audio
- `pywhatkit` – YouTube and Google search integration
- `wikipedia`, `playsound`, `Pillow` – For extra functionalities

---

## 📁 Project Structure

voice_assistant/
│
├── voice_assistant.py # Main assistant code
├── background.jpg # Background image for GUI


---

## ⚙️ Setup Instructions

### 1. Install Dependencies
Make sure you're using Python 3.10+ and then run:

```bash
pip install sounddevice scipy speechrecognition gTTS playsound pywhatkit wikipedia pillow
```

## Optional: Use a virtual environment to isolate dependencies.

## How to Run
1. Ensure microphone works
2. Install all required libraries
3. Run `voice_assistant.py`

## Ensure background.jpg is in the same directory as voice_assistant.py.