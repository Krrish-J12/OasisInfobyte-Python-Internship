import sounddevice as sd
from PIL import Image, ImageTk 
from scipy.io.wavfile import write
import speech_recognition as sr
from gtts import gTTS
import os
import pyautogui
import time
import webbrowser
import datetime
import wikipedia
import pywhatkit
import random
import playsound
import tkinter as tk
from threading import Thread
import numpy as np

# Function to speak text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = f"voice_{random.randint(1, 100000)}.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Function to list input devices
def list_input_devices():
    devices = sd.query_devices()
    input_devices = [(i, d['name']) for i, d in enumerate(devices) if d['max_input_channels'] > 0] # type: ignore
    return input_devices

# Function to record audio
def record_audio(filename='input.wav', duration=6, fs=44100, device_id=None):
    try:
        print("Listening...")
        sd.default.device = (device_id, None)
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        write(filename, fs, myrecording)
        return filename
    except Exception as e:
        print("Recording error:", e)
        speak("There was an error recording your voice.")
        return ""

# Function to recognize speech
def recognize_speech(filename='input.wav'):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio) # type: ignore
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
    except sr.RequestError:
        speak("Could not request results from Google.")
    return ""

# Function to process commands
def process_command(command):
    command = command.lower()
    if 'hello' in command or 'hi' in command or 'hey' in command or 'hey whatsup' in command or 'assistant' in command:
        speak("Hello! How can I help you?")
    elif 'open youtube' in command:
        webbrowser.open('https://www.youtube.com')
        speak("Opening YouTube")
    elif 'open google' in command:
        webbrowser.open('https://www.google.com')
        speak("Opening Google")
    elif 'play music' in command or 'play' in command or 'play song' in command or 'song' in command:
    # Extract the song name
        song = command
        for keyword in ['play music', 'play song', 'play', 'song']:
            song = song.replace(keyword, '')

        song = song.strip()
        print(f"Detected song to play: {song}")

        if song:
            speak(f"Playing {song} on YouTube. Please wait...")
            try:
                pywhatkit.playonyt(song) # type: ignore
                time.sleep(6)  # wait for YouTube to load
                pyautogui.press("enter")  # simulate play
                speak("Playing music.")
            except Exception as e:
                speak("Sorry, I couldn't play the song due to an error.")
                print(f"Error playing music: {e}")
        else:
            speak("Please say the song name after saying play.")

    elif 'time' in command:
        now = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {now}")
    elif 'date' in command:
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        speak(f"Today's date is {today}")
    elif 'search' in command:
        search_term = command.replace('search', '').strip()
        pywhatkit.search(search_term) # type: ignore
        speak(f"Searching for {search_term}")
    elif 'wikipedia' in command:
        topic = command.replace('wikipedia', '').strip()
        try:
            info = wikipedia.summary(topic, sentences=5)
            speak(info)
        except:
            speak("Sorry, I couldn't find anything on that topic.")
    elif 'stop' in command or 'exit' in command or 'ruk jao' in command :
        speak("Goodbye!")
        stop_assistant()
    else:
        speak("Sorry, I didn't get that.")

# Main assistant loop
def assistant_loop():
    global running, paused, selected_device_id
    while running:
        if not paused:
            filename = record_audio(device_id=selected_device_id)
            command = recognize_speech(filename)
            print("You said:", command)
            if command:
                if 'start' in command or 'hi assistant' in command:
                    paused = False
                elif 'pause' in command:
                    paused = True
                    speak("Assistant paused.")
                else:
                    process_command(command)

# Function to stop assistant
def stop_assistant():
    global running
    running = False
    speak("Assistant stopped.")
    root.quit()

# Function to start assistant after mic selection
def start_assistant():
    global selected_device_id, paused, running
    selected_name = mic_var.get()
    selected_device_id = next((i for i, name in input_devices if name == selected_name), None)
    if selected_device_id is None:
        speak("Microphone not found.")
        return
    paused = False
    running = True
    speak("Assistant started.")
    Thread(target=assistant_loop).start()

# GUI setup
input_devices = list_input_devices()
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("800x600")

# Load background image
original_bg = Image.open("background.jpg")  # Replace with your file
bg_image = ImageTk.PhotoImage(original_bg)

# Create Canvas and set background
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
bg = canvas.create_image(0, 0, image=bg_image, anchor="nw")

# Create a frame for your UI
frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.5, anchor="center")

# After background image
frame = tk.Frame(root, bg='white', bd=2)
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Select Microphone:", font=("Arial", 12), bg='White').pack(pady=10)
mic_var = tk.StringVar(value=input_devices[0][1])
mic_menu = tk.OptionMenu(frame, mic_var, *[name for _, name in input_devices])
mic_menu.config(font=("Arial", 10))
mic_menu.pack(pady=5)

tk.Button(frame, text="Start Assistant", font=("Arial", 12), bg="green", fg="white", command=start_assistant).pack(pady=10)
tk.Button(frame, text="Exit", font=("Arial", 12), bg="red", fg="white", command=stop_assistant).pack(pady=10)

# Resize function
def resize_bg(event):
    new_bg = original_bg.resize((event.width, event.height), Image.Resampling.LANCZOS)
    new_bg_image = ImageTk.PhotoImage(new_bg)
    canvas.itemconfig(bg, image=new_bg_image)
    canvas.bg_image = new_bg_image  # type: ignore # Keep a reference

root.bind("<Configure>", resize_bg)

paused = False
running = False
selected_device_id = None

root.mainloop()
