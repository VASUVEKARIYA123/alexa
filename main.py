import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

engine.say('I am your alexa')

engine.say('What can i do for you')

def talk(text):
    engine.say(text)
    engine.runAndWait()

engine.runAndWait()


def take_command():
    try : 
        with sr.Microphone() as source:
            print()
            print("Listening...")
            print()

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            # for recognize alexa in command 
            if 'alexa' in command :
                command = command.replace('alexa','')
                print(command)

    except:

        pass
    return command

def run_alexa():

    command = take_command()

    if 'play' in command:

        song = command.replace('play','')
        talk('playing...' + song)
        pywhatkit.playonyt(song)
        print(song)
    
    elif 'how are you' in command:
        talk('i am fine.')

    elif 'time' in command:

        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('currunt time is ' + time)

    elif 'who is' in command:

        person = command.replace('who is ','')
        info = wikipedia.summary(person,2)
        print(info)
        talk(info)

    elif 'date with you' in command:

        talk('sorry , I have a headacha')

    elif 'are you single' in command:

        talk('i am in a relationship with vasu vekariya')

    elif 'joke' in command : 

        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    
    else:
        talk('Please say the command again.')
    

while True : 
    run_alexa()

 