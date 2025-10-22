import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import musicLibrary
import requests


recognizer = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')

newsapi = "045a45b18fb042f8b3ee20f1c877684a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

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
         

                   


if __name__ == "__main__":
        speak("Initializing Jarvis . . . ")
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
                        print("Jarvis active ...")    
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)

                        processCommand(command)

            except sr.WaitTimeoutError:
                    print("Listening timeout")

            except Exception as e:
                    print("Error {0}".format(e))