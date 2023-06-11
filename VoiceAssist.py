import threading
from vosk import Model, KaldiRecognizer
from Abilaty import *
import  pyaudio
"""
Befehle:
1:Search ...
2:Open YouTube/or other Website if specified
3:Start/OpenFile

"""

class Jarvis:
    def __init__(self,testing):
        self.testthread = threading.Thread(target = testing.Threaded,args=())
        model = Model(r"E:\VoiceSamp\vosk-model-small-en-us-0.15")
        self.rcognizer = KaldiRecognizer(model, 16000)
        mic = pyaudio.PyAudio()
        self.stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()
        self.ready = False
        
    def voiceRecognition(self):
        while True:
            self.data = self.stream.read(4096)

            if self.rcognizer.AcceptWaveform(self.data):
                text = self.rcognizer.Result()
                self.shortText = text[14:-3]
                self.StreamAudio()


    def StreamAudio(self):
        if self.shortText == "jarvis" and self.ready == False:
            print("Hello Sir")
            self.ready = True
        elif self.ready == True:

            if self.shortText == "forget it":
                print("np Sir")
                self.ready = False
            else:
                self.ready = False
                if self.shortText == "ability one":
                    Abilatie_One()
                elif self.shortText[:4] == "open" or self.shortText[:5] == "start":
                    if self.shortText[:4] == "open":
                        if self.shortText[5:] == "you tube":
                            OpenWebsite("https://www.youtube.com")
                        elif self.shortText[5:] == "spotify":
                            StartFile("C:\\Users\\net\\AppData\\Roaming\\Spotify\\Spotify.exe")
                        elif self.shortText[5:] == "a para":
                            StartFile("C:\\Users\\net\\AppData\\Local\\Programs\\Opera\\launcher.exe")
                        elif self.shortText[5:] == "riot":
                            StartFile("D:\\Riot\\Riot Games\\Riot Client\\RiotClientServices.exe")
                        elif self.shortText[5:] == "camera":
                            self.testthread.start()
                elif self.shortText[:5] == "start":
                    print(shortText)
                    if self.shortText[6:] == "you tube":
                        OpenWebsite("https://www.youtube.com")
                    elif self.shortText[6:] == "spotify":
                        StartFile("C:\\Users\\net\\AppData\\Roaming\\Spotify\\Spotify.exe")
                    elif self.shortText[6:] == "a para":
                        StartFile("C:\\Users\\net\\AppData\\Local\\Programs\\Opera\\launcher.exe")
                    elif self.shortText[6:] == "riot":
                        StartFile("D:\\Riot\\Riot Games\\Riot Client\\RiotClientServices.exe")




                elif self.shortText[:6] == "search":
                    SearchWebsite(shortText[7:])
                else:
                    print("no valid input recieved. Please try again")
                    self.ready = True

