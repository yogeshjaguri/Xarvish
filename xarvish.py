import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
       speak("Good Afternoon!")   

    else:
        speak("Good Evening!")   

    speak("I am xarvish. how may i help you")    


def takeCommand():
    #it takes microphone input from the Users and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print ("user said {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None" 

    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("yourmail@gmail.com", "yourpassword")
    server.sendmail("yourmail@gmail.com", to, content)
    server.close()




if __name__=="__main__":
    wishMe()
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\Music' #yourpath
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            vspath = "path" #path (target)
            os.startfile(vspath)

        elif 'email to yogi' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "email@gmail.com"
                sendEmail(to, content)
                speak("email has been sent.")
            except Exception as e:
                print(e)
                speak("sorry, i am not able to send email")



