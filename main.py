import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import pywhatkit
import yfinance as yf
import pyjokes


def welcome():
    speak('''Welcome.  my name is Zeebee. I am your personal assistant.   
    How can i help you?''')


# get the message from the client.
def transform():
    r1 = sr.Recognizer()
    with sr.Microphone() as source:
        r1.pause_threshold = 10
        said = r1.listen(source)
        # We can get some exception here.
        try:
            print("I'm listening")
            qu = r1.recognize_google(said, language="en")
            return qu
        except sr.RequestError:
            print("Sorry,the service is down")
            return "I am waiting for your command"
        except sr.UnknownValueError:
            print("Sorry Sir/Mrs, but i didn't understand")
            return "I am waiting for your command"
        except:
            return "I am waiting for your command"


# talk to the client
def speak(message):
    femaleAs = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    maleAS = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine = pyttsx3.init()
    engine.setProperty('voice', maleAS)
    engine.say(message)
    engine.runAndWait()


# returns the weekday name.
def query_day():
    day = datetime.date.today()
    print(day)
    weekday = day.weekday()
    table = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }

    speak(f'Today is {table[weekday]}')


# returns the time.
def query_time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"{time[0:2]} o'clock and {time[3:5]} minutes")


# the main function which activate the assitant
def assistant_main():
    welcome()
    start = True
    while (start):
        q = transform().lower()
        if 'start youtube' in q:
            speak('starting youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open google' in q:
            speak('opening google')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is it' in q:
            query_day()
            continue
        elif 'what time is it' in q:
            query_time()
            continue
        elif 'shut down' in q or 'stop' in q:
            speak('i am shutting down. Goodbye')
            break
        elif 'search in wikipedia' in q:
            speak('checking wikipedia')
            q = q.replace("wikipedia", "")
            result = wikipedia.summary(q, sentences=2)
            speak('found in wikipedia')
            speak(result)
            continue
        elif 'what is your name' in q:
            welcome()
            continue
        elif 'search web' in q:
            pywhatkit.search(q)
            speak('this is what i found')
            continue
        elif 'play' in q:
            speak(f'playing{q}')
            pywhatkit.playonyt(q)
            continue
        elif 'tell me joke' in q:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in q:
            search = q.split("of")[-1].strip()
            map1 = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                stock = map1[search]
                stock = yf.ticker(stock)
                price = stock.info["regularMarketPrice"]
                speak(f'found it, the price for{search} is {price}')
            except:
                speak(f'sorry, but i did not found data for {search}')
            continue


if __name__ == '__main__':
    welcome()
    speak("ani lo shota vodka, ani lo shota redbull")
    query_day()
    query_time()
