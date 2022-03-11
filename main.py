import speech_recognition as sr
import pyttsx3
import pywhatkit as pkit
import datetime
import wikipedia


engine = pyttsx3.init()
r=sr.Recognizer()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
engine.say("Hello I am Camila How can i help you")
engine.runAndWait()
while(True):
    def speak(word):
        engine.say(word)
        engine.runAndWait()

    def take_command():
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source)
                l=r.recognize_google(audio)
                l=l.lower()
                if 'Camila' in l:
                    l=l.replace('Camila','')
                    print(l)
        except:
            pass
        return l

    def run_camila():
        s=take_command()
        if 'play' in s:
            song=s.replace('play','')
            speak('Playing'+song)
            pkit.playonyt(song)
            print('Playing')
        elif 'current'and'time'in s:
            time=datetime.datetime.now().strftime('%I:%M:%S %p')
            print(time)
            speak(time)
        else:
            print(wikipedia.summary(s,5))
            speak(wikipedia.summary(s,5))

    run_camila()