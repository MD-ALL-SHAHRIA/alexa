import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass

    return command

def run_alexa():
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        print('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry, I am in another relationship')
    elif 'open website' in command:
        website = command.replace('open website', '')
        talk('Opening ' + website)
        pywhatkit.search(website)
    elif 'calculate' in command:
        calculation = command.replace('calculate', '')
        result = eval(calculation)
        talk('The result is ' + str(result))
    elif 'introduce yourself' in command:
        talk('hi! I am your voice assistant. How can I help you today?')
    else:
        talk('I did not get it, but I am going to search it for you')
        pywhatkit.search(command)

while True:
    run_alexa()
