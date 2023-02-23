# IMPORTS 
import numpy as np
import scipy as sp
import scipy.signal as sps
import matplotlib.pyplot as plt
import soundfile as sf
import webbrowser
import piano_gui
import IPython # playback reconstructed wav file
import io
import os
#import speech_recognition as sr
#import time
#import playsound
from urllib.request import urlopen # open files from URL -- no saving required
from pytube import YouTube
#from gtts import gTTS


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
input7_url = 'https://www.youtube.com/watch?v=NDWJWILEA7o' # 13
input8_url = 'https://www.youtube.com/watch?v=7maJOI3QMu0' # river flows in you
input9_url = 'https://www.youtube.com/watch?v=1T0e-Fee_ug' # Chaconne 2
input10_url = 'https://www.youtube.com/watch?v=AsqDPqII6-Q' # Reforget

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
        new_file = base + '.wav'
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








def signal_process():
    # parameters
    compression_percent = 1   

    print("Running with compression_percent = %d"%compression_percent)

    # load data as np array
 #   data_raw, sampleRateHz = sf.read(io.BytesIO(urlopen(input1_url).read()))
    data_raw, sampleRateHz = sf.read(io.BytesIO('yaeow - Im Letting Go (Lyrics).wav'))
    data = np.array(data_raw) # data as a numpy array
    L = len(data)
    print("length of input data record is %d samples"%L)
    print("min/max values are: %+.3f/%+.3f"%(np.min(data),np.max(data)))

    # compute FFT and FFT frequencies

    N = (2**np.ceil(np.log2(L))).astype(int) # find next largest power of 2, cast to int
    # note: without the "cast" `astype()`, the fft function barfs
    print("Using N = %d"%N)

    S = sp.fft.fft(data,N) 
    # S contains the full FFT, with coefficients every (2*pi*k/N) for k = 0,...,N
    S_freq = sp.fft.fftfreq(N,(1.0/sampleRateHz))

    # plot original FFT 
    f = plt.figure(figsize=[20,5])
    plt.subplots_adjust(top=2.5) 

    ax2 = f.add_subplot(2,1,1)
    ax2.stem(sp.fft.fftshift(S_freq),sp.fft.fftshift(np.absolute(S)),use_line_collection=True)
    ax2.set(title="input signal FFT (magnitude)")

    # find largest FFT values, from the half FFT 

    # temporarily store half FFT
    S_half = S[0:(N//2)]
    # sort by magnitude in descending order
    S_half_sort_index = np.argsort(np.absolute(S_half)) 
    S_half_sort_index = np.flip(S_half_sort_index)

    # compute N_to_keep
    N_to_keep = (np.ceil(compression_percent/100*L//2)).astype(int)
    print("N_to_keep = %d"%N_to_keep)

    # signal reconstructed from the single largest FFT value
    S_reconstruct = np.zeros(S.size,dtype=np.complex64)
    sort_index_max = S_half_sort_index[0:N_to_keep]
    S_reconstruct[sort_index_max] = S_half[sort_index_max]

    # now reconstruct the other half of the FFT values using conjugate symmetry
    for i in range(N//2):
      S_reconstruct[N-1-i] = np.conjugate(S_reconstruct[i+1])

    # plot FFT showing saved values only  
    ax3 = f.add_subplot(2,1,2)
    ax3.stem(sp.fft.fftshift(S_freq),sp.fft.fftshift(np.absolute(S_reconstruct)),use_line_collection=True)
    ax3.set_xlabel("digital frequency (Hz)")

    ax3.set(title="reconstructed signal FFT (magnitude)")

    plt.show()

    #reconstruct the original signal from the partial FFT 
    # note: for boilerplate code cell below, labeled "playback reconstructed wav file",
    # make sure the reconstructed audio file is "reconstructed.wav"

    # use inverse FFT to get back a time-domain signal
    data_reconstructed = sp.fft.ifft(S_reconstruct)
    data_reconstructed_real = np.real( data_reconstructed[0:len(data)] )

    sig_reconstructed = sp.fft.ifft(S_reconstruct)
    sig_reconstructed_real = np.real( sig_reconstructed )
# In theory this should give us a purely real result back, 
# but due to numerical effects there is a small residual imaginary component.  
# Therefore, wrap the call in `np.real()`
#total_power = np.sum(np.power(np.absolute(data_reconstructed),2.0)) # DEBUG
#total_power_real = np.sum(np.power(np.absolute(data_reconstructed_real),2.0)) # DEBUG
#if compression_percent > 0: # DEBUG
#  assert( (total_power-total_power_real) < 0.10*total_power ) # DEBUG / sanity check
  # if the above assertion fails, then the argument to `ifft()` was NOT conjugate symmetric

    print("length of reconstructed data record is %d samples"%len(data_reconstructed_real))
    print("min/max values are: %+.3f/%+.3f"%(np.min(data_reconstructed_real),np.max(data_reconstructed_real)))

    # write out audio as 16bit PCM WAV
    sf.write('reconstructed.wav', data_reconstructed_real, sampleRateHz, subtype='PCM_16')
    IPython.display.Audio('reconstructed.wav') 

           

