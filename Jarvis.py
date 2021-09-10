import pyttsx3
import speech_recognition as sr
import datetime
# import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print voices
#to find which voices are present in our pc
# print(voices[1].id)


engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning dear. Have a great day")
    elif hour>=12 and hour<18:
        speak("Good afternoon dear. Have a great day ")
    else:
        speak("Good Evening dear.")
    speak("I am Jarvis. Plz tell how may i help you?")

def takecommand():
    #it takes microphone input from the user and returns the string output 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query =r.recognize_google(audio, language='en-in')
        print(f"User said : {query}")

    except Exception as e:
        # print(e)
        print("Say that again plz....")
        return "None"
    return query
    
if __name__ == "__main__":
   
    wishme()
    while True:
        query = takecommand().lower
        if "open youtube" in query:
            webbrowser.open('https://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        