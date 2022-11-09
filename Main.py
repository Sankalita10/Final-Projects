

from time import time
import pyttsx3
import pywhatkit 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
from GoogleNews import GoogleNews
from requests import get
import pyjokes








def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()


        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')
googlenews = GoogleNews()
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Sofia . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'play' in query:
                a='Ok lets rock..'
                engine.say(a)
                engine.runAndWait()
                pywhatkit.playonyt(query)

        elif 'ip address' in query:
           ip= get("https://api.ipify.org").text
           speak(f"your ipaddress is {ip}")


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open Whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening Wwhatsapp")

        

        

        
        

        elif 'open movies' in query:
            movie_dir = 'G:\English Movie'
          
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[0]))
            speak("opening Movies...")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)
            speak("opening code...")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opening whatsapp..")

        elif 'open google' in query:
            speak("Mam, What you want to search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'joke' in query:
            joke= pyjokes.get_joke()
            speak(joke)

        elif 'Shut down the system' in query:
            os.system("shutdown /s /t s")

        
        
            
            

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening Youtube..")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")
            speak("opening gmail...")

        elif 'headlines' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Today news')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')

        elif 'tech' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Tech')
            googlenews.result()
            a=googlenews.gettext()
            
            print(*a[1:5],sep=',')
            speak("result")

        elif 'politics' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Politics')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')

        elif 'sports' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('Sports')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')

        elif 'cricket' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('cricket')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
        

        elif 'football' in query:
            engine.say('Getting news for you ')
            engine.runAndWait()
            googlenews.get_news('football')
            googlenews.result()
            a=googlenews.gettext()
            print(*a[1:5],sep=',')
            
        elif 'Thank you' in query:
            speak("Welcome mam, I am happy to help you")

        
            
            
            
        