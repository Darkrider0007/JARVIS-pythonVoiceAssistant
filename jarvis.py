import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from googlesearch import search
#import pywhatkit as kt 



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>3  and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir.. How may I help you")

def Greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>3  and hour <12:
        speak("Have a Good day Sir!")
    elif hour>=12 and hour<18:
        speak("Good Bye Sir!")
    else:
        speak("Good Night Sir!")



def takecommand():
    # It takes microphone input from the user and returns string output from
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Recongening...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,contant):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("mymailid","my-Password")
    server.sendmail('send to mailid',to,contant)
    server.close()



if __name__ == '__main__':
    WishMe()
    while True:
        query = takecommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'hello jarvis' in query:
            speak('Hello sir,.. how may I help you?')
   
        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com/watch')

        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir="C:\\music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\HP\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'email to Rohan' in query:
            try:
                speak("What should I say?")
                contant = takecommand()
                to = "goperohan041@gmail.com"
                sendEmail(to, contant)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry, sir I am not able to send this email")


   

        elif 'quit' in query:
            speak("Thanks for choosing me.")
            Greetme()
            exit()
        elif 'exit' in query:
            speak("Thanks for choosing me.")
            Greetme()
            exit()
        elif 'close' in query:
            speak("Thanks for choosing me.")
            Greetme()
            exit()