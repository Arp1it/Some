import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voicess = engine.getProperty('voices')
# print(voicess[1].id)
engine.setProperty('voice', voicess[0].id)

def speakk(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def whish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speakk("Good morning")

    elif hour >= 12 and hour < 18:
        speakk("Good afternoon")

    else:
        speakk("Good evening")

    speakk("i am jarvis sir. How can i help you")

def takevoice():
    # this function takes microphone input from the user and return sstring outputs

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")

        # r.pause_threshold = 1
        # r.energy_threshold = 350
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again pleasee...")
            return "None"

        return query

def sendemail(to, content):
    # First on less secure app setting on your gmail google account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    server.starttls()
    server.login('jaisa358@gmail.com', 'abc120arpit')
    sever.sendmail('jaisa358@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    whish()
    # logic for executing task

    while True:
        querry = takevoice().lower()

        if "wikipedia" in querry:
            speakk("Searching wikipedia...")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speakk('According to wekipedia...')
            speakk(results)
            
        if "open youtube"in querry:
            speakk("youtube is opening...")
            webbrowser.open("https://www.youtube.com/")

        if "open google" in querry:
            speakk("google is opening...")
            webbrowser.open("https://www.google.com/")

        if "open chrome" in querry:
            speakk("chrome is openning...")
            webbrowser.open("https://www.chrome.com/")

        if "open stack overflow" in querry:
            speakk("openning...")
            webbrowser.open("https://www.stackoverflow.com/")

        if "open" in querry:
            speakk("openning...")
            querry = querry.replace("open", "")
            querry = querry.replace(" ", "")
            webbrowser.open(f"https://www.{querry}.com/")

        if "play music" in querry:
            speakk("openning...")
            music_dir = "C:\\Users\\Windows\\Desktop\\mnusic"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs))]))

        if "the time" in querry:
            stritime = datetime.datetime.now().strftime("%H:%M:%S")
            speakk(f"Sir, The time is {stritime}")

        if "open code" in querry:
            speakk("openning...")
            vscodepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)

        if "send email" in querry:
            # First on less secure app setting on your gmail google account
            speakk("email sending...")
            try:
                speakk("what should I say")
                content = takevoice()
                to = "jaiswalakshansh614@gmail.com"
                sendemail(to, content)

            except Exception as e:
                print(e)
                print("Sorry sir email has not beeen sent")

        if "jarvis quit" in querry or "quit" in querry:
            speakk("Thanks for giving a time sir.")
            exit()