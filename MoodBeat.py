import webbrowser
#import speech_recognition as sr
#from gtts import gTTS
#import time
#import playsound
#import numpy as np
#import scipy as sp
from urllib.request import urlopen # open files from URL -- no saving required
#import soundfile as sf
import io

from pytube import YouTube
import os

##def speak(text):
##    tts = gTTS(text=text, Lang='en')
##    filename = 'voice.mp3'
##    tts.save(filename)
##    playsound.playsound(filename)
##
##def get_audio():
##    r = sr.Recognizer()
##    with sr.Microphone() as source:
##        audio = r.listen(source)
##        said = " "
##
##        try:
##            said = r.recognize_google(audio)
##            print(said)
##        except Exception as e:
##            print("Exception: " + str(e))
##    return said
##
##speak("hello")
##get_audio()
##text = get_audio()
##if "hello" in text:
##    speak("How are you feeling today Heonmin?")
##elif "sad" in text:
##    speak("I will play music for you")

print("Mood Selection = forget, tears, move on, done, miss, wish, wait")
Mood_Input = input("Enter your mood: ")

input1_url = 'https://www.youtube.com/watch?v=bBsK1tuXF6E' # I'm letting go
input2_url = 'https://www.youtube.com/watch?v=YwRWIin3I6U' # Memories remain in the parting than the encounter
input3_url = 'https://www.youtube.com/watch?v=HuK2N29s0mE' # Wish I Was Better
input4_url = 'https://www.youtube.com/watch?v=ATE6kDsmuOE' # If We Never Met
input5_url = 'https://www.youtube.com/watch?v=nsHc_3G9oKQ' # She's not you
input6_url = 'https://www.youtube.com/watch?v=tFhznXWp--8' # Street Lights


chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

def download_file():
    print("Would you like to save audio file?")
    choice = str(input())
    if(choice == 'Y'):
        # check for destination to save file
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
  
        # download the file
        out_file = video.download(output_path=destination)
  
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

# url input from user
#for Mood_Input in range():
if(Mood_Input == "forget"):
    yt1 = YouTube(input1_url)
    # extract only audio
    video = yt1.streams.filter(only_audio=True).first()
    download_file()
    # Play on Youtube
    webbrowser.get('chrome').open_new_tab(input1_url)
elif(Mood_Input == "miss"):
    yt2 = YouTube(input6_url)
    # extract only audio
    video = yt2.streams.filter(only_audio=True).first()
    download_file()
    # Play on Youtube
    webbrowser.get('chrome').open_new_tab(input6_url)
elif(Mood_Input == "wish"):
    yt3 = YouTube(input3_url)
    # extract only audio
    video = yt3.streams.filter(only_audio=True).first()
    download_file()
    # Play on Youtube
    webbrowser.get('chrome').open_new_tab(input3_url)
elif(Mood_Input == "move on"):
    yt4 = YouTube(input4_url)
    # extract only audio
    video = yt4.streams.filter(only_audio=True).first()
    download_file()
    # Play on Youtube
    webbrowser.get('chrome').open_new_tab(input4_url)
elif(Mood_Input == "done"):
    yt5 = YouTube(input5_url)
    # extract only audio
    video = yt5.streams.filter(only_audio=True).first()
    download_file()
    # Play on Youtube
    webbrowser.get('chrome').open_new_tab(input5_url)

  
# result of success
#print(yt.title + " has been successfully downloaded.")





           

