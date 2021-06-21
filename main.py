import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from logging import shutdown
import time
import pyautogui
from pynput.keyboard import Key, Controller
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id) # Select Voice 0 = Male, 1 = Female (Default Voices) 

# Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Turn Wi-Fi on and off, Have to run the code as administrator
def enableWiFi():
    os.system("netsh interface set interface Wi-Fi enabled")
def disableWiFi():
    os.system("netsh interface set interface Wi-Fi disabled")
    time.sleep(50)
    os.system("netsh interface set interface Wi-Fi enabled")

# Volume Control Function
def volumeControlIncrease():
    keyboard = Controller()
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)
    keyboard.press(Key.media_volume_up)
    keyboard.release(Key.media_volume_up)

def volumeControlDecrease():
    keyboard = Controller()
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)
    keyboard.press(Key.media_volume_down)
    keyboard.release(Key.media_volume_down)

def volumeFull():
    for i in range(50):
        keyboard = Controller()
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

def volume50():
    keyboard = Controller()
    for i in range(50): # Sets volume to 0%
        keyboard = Controller()
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
    for i in range(25): # Sets volume to 50%
        keyboard = Controller()
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

# Who are you, type Function
def typeMe():
    pyautogui.write('Insert your text here', interval=0.08) # Insert your text, select interval between keys pressed 
    time.sleep(2)
    os.system("TASKKILL /F /IM notepad.exe")

# WishMe Function (Program wishes user)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir/mam [your name]!")
        print("Good Morning sir/mam [your name]!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir/mam [your name]!")
        print("Good Afternoon sir/mam [your name]!")
    
    else:
        speak("Good Evening sir/mam [your name]!")
        print("Good Evening sir/mam [your name]!")

    speak("I am [assistant name] your slave. Memory 100 terabyte, RAM 128 gigabyte. Please tell me how may I help you")

# WhatToDo Function (Program tells the user what to do when)
def whatToDo():
    hour = int(datetime.datetime.now().hour)
    if hour >= 18 and hour < 22:
        print("[assistant name]: [Text here]") # Type what you need to do now/Timetable/Routine
        speak("[Text here]") # Insert same text as above

    elif hour >= 6 and hour < 7:
        print("[assistant name]: [Text here]")
        speak("[Text here]")
    
    elif hour >= 15 and hour < 17:
        print("[assistant name]: [Text here]")
        speak("[Text here]")

# TakeCommand Function (Takes user command through voice input)
def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("[assistant name]: Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"[your name]: {query}\n") # Insert your name inside []

    except Exception as e:
        # print(e)
        print("[assistant name]: Say that again please...")
        return "None"

    return query

# Loop for program to run
if __name__ == "__main__":
    wishMe()
    # Constant listening loop for taking command
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks (Jokes, Alarms, Reminders, Etc...)
        if 'wikipedia' in query:
            print("[assistant name]: Searching Wikipedia...")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(f"[assistant name]: {results}\n")
            speak(results)
        
        elif 'wish me' in query:
            wishMe()

        elif 'who am i' in query:
            print("[assistant name]: [Insert your text, eg.: You are a great artist, reader, musician, etc...]")
            speak("[Insert your text, eg.: You are a great artist, reader, musician, etc...]")

        elif 'open gmail' in query:
            speak("Opening Gmail")
            print("Opening Gmail...")
            url = "[your Gmail url]" # Get your Gmail url from browser
            chrome_path = 'C:/[chrome.exe path] %s' # Find chrome.exe path in your computer and insert here
            webbrowser.get(chrome_path).open(url)
        
        elif 'open task manager' in query:
            # keyboard = Controller()
            pyautogui.hotkey('ctrl', 'shift', 'esc')
        elif 'close task manager' in query:
            os.system("TASKKILL /F /IM taskmgr.exe")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            print("[assistant name]: Opening YouTube...")
            url = "youtube.com"
            chrome_path = 'C:/[chrome.exe path] %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            speak("Opening Google")
            print("[assistant name]: Opening Google...")
            url = "google.com"
            chrome_path = 'C:/[chrome.exe path] %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open whatsapp' in query:
            speak("Opening Whatsapp")
            print("[assistant name]: Opening Whatsapp...")
            url = "web.whatsapp.com"
            chrome_path = 'C:/[chrome.exe path] %s'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query:
            print("Playing [song name]")
            music_dir = "[music folder path]"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"[assistant name]: Sir/mam the time is {strTime}\n")
            speak(f"sir/mam the time is {strTime}")

        elif 'quit' in query:
            print("Alex: Quitting sir. Thanks for your time!")
            speak("Quitting sir. Thanks for your time")
            exit()

        elif 'who is my father' in query:
            speak("Your father is the great [father name]")

        elif 'who is my mother' in query:
            speak("Your mother is the great [mother name]")
        
        elif 'what should i do now' in query:
            whatToDo()

        elif 'who are you' in query:
            speak("I am [assistant name] your slave. Memory 100 terabyte, RAM 128 gigabyte. Please tell me how may I help you")
            print("I am [assistant name] your slave. Memory 100 terabyte, RAM 128 gigabyte. Please tell me how may I help you")
            typeMe()

        elif 'joke' in query:
            jokeByAssistant = pyjokes.get_joke()
            # print(f"Alex: {pyjokes.get_joke()}")
            print(f"[assistant name]: {jokeByAssistant}")
            speak(jokeByAssistant)

        elif 'shutdown' in query:
            speak("Shutting Down")
            print("[assistant name]: Shutting Down...")
            os.system("shutdown /s /t 4 ")
            speak("in 3")
            time.sleep(0.5)
            speak("2")
            time.sleep(0.5)
            speak("1")
            time.sleep(1)
            speak("Good bye sir/mam")
            exit()

        elif 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")
        elif 'close code' in query:
            os.system("TASKKILL /F /IM code.exe")

        elif 'turn on wi-fi' in query:
            enableWiFi()
        elif 'turn off wi-fi' in query:
            disableWiFi()

        elif 'type the following' in query:
            query = query.replace("type the following", "")
            os.startfile("C:\\windows\\system32\\notepad.exe")
            time.sleep(0.5)
            pyautogui.write(query)
            time.sleep(10)
            os.system("TASKKILL /F /IM notepad.exe")

        elif 'what are you doing' in query:
            speak("I am in direct chat with google assistant/siri/alexa")

        elif 'volume up' in query:
            volumeControlIncrease()
        elif 'volume full' in query:
            volumeFull()        
        elif 'volume down' in query:
            volumeControlDecrease()      
        elif 'volume 50' in query:
            volume50()
           
          
# End of code
# By, AdityaCODER1
