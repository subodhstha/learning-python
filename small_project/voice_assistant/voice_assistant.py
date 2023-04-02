import speech_recognition as sr
import pyttsx3
import pywhatkit
import time
import pyautogui
import datetime
import wikipedia
import pyjokes
import webbrowser
import smtplib
import wolframalpha
from twilio.rest import Client
import os
from urllib.request import urlopen
import winshell
import json


assname = "Wick! John Wick"

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        talk("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        talk("Good Afternoon Sir !")  

    else:
        talk("Good Evening Sir !") 
    talk("I am your Assistant")
    talk(assname)
    talk('How can I help you?')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()

def run_john():
    command = take_command().lower()
    if 'hey' or 'hello' in command:
        wish()
        
    elif 'how are you' in command:
        talk('I am fine.')
        talk('What about you.')
        
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        time.sleep(5)
        pyautogui.press('space')
        
    elif 'time' in command:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time1)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'open youtube' in command:
            talk("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

    elif 'send mail' in command:
        try:
            talk("What should I say?")
            content = take_command()
            to = input()   
            sendEmail(to, content)
            talk("Email has been sent !")
        except Exception as e:
            print(e)
            talk("I am not able to send this email")
        
    elif 'open google' in command:
            talk("Here you go to Google\n")
            webbrowser.open("google.com")
            
    elif "what's your name" in command or "What is your name" in command:
        talk("My friends call me")
        talk(assname)
        print("My friends call me", assname)
            
    elif "who made you" in command or "who created you" in command:
        talk("I have been created by useless person.")
            
    elif "calculate" in command:
        app_id = "Wolframalpha api id"
        client = wolframalpha.Client(app_id)
        indx = command.lower().split().index('calculate')
        command = command.split()[indx + 1:]
        res = client.command(' '.join(command))
        answer = next(res.results).text
        print("The answer is " + answer)
        talk("The answer is " + answer)
            
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")
    
    elif 'search' in command:
        command = command.replace("search", "")
        webbrowser.open(command)
    
    elif 'news' in command:
        try:
            jsonObj = urlopen('''https://newsapi.org/v2/everything?q=bitcoin&from=2023-03-01&sortBy=publishedAt&apiKey=API_KEY''')
            data = json.load(jsonObj)
            i = 1
            talk('here are some top news from the times of india')
             
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                talk(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:
            print(str(e))
        
    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        talk("Recycle Bin Recycled")
        
    elif "where is" in command:
        command = command.replace("where is", "")
        location = command
        talk("User asked to Locate")
        talk(location)
        webbrowser.open("https://www.google.com/maps" + location + "")
    else:
        talk('Please say again.')
    
if __name__ == '__main__':
    clear = lambda: os.system('cls')

    clear()
    while True:
        run_john()
