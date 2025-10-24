import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')

newsapi = ""

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give 100 word responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if c.lower() == "open google":
          wb.open("https://google.com")
    elif c.lower() == "open youtube":
          wb.open("https://youtube.com")
    elif c.lower() == "open spotify":
          wb.open("https://spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)

    elif "news" in c.lower():
         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
         if r.status_code == 200:
              data = r.json()
              articles = data.get('articles', [])

              for article in articles:
                   speak(article['title'])
    
    else:
         #Let openAI handle the request
        output = aiProcess(c)
        speak(output) 

                   


if __name__ == "__main__":
        speak("Initializing jarvis . . . ")
        while True:
            #Listen for the word "Jarvis"
            r = sr.Recognizer()

            print("Recognizing...")
            try:
                with sr.Microphone() as source:
                    print("Listening ...")    
                    audio = r.listen(source)
               
                # using google speech recognition
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yeah")
                    
                
                
                #listen for command
                    with sr.Microphone() as source:
                        print("jarvis active ...")    
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)

                        processCommand(command)

            except sr.WaitTimeoutError:
                    print("Listening timeout")

            except Exception as e:
                    print("Error {0}".format(e))