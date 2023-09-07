import speech_recognition
import personalTasks
import gpt4all
import pyttsx3 as tts


def generateRespons(text):
    with model.chat_session():
        response = model.generate(prompt=text, temp=1)
        return response
def VoiceRecognition():
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.7)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f"user:{text}")
                if (text == stopProgramm):  # stop programm
                    break
                elif (text in personalTasks.preDetemendCommands):  # perform commands
                    personalTasks.Tasks(text)
                elif (text == sleepWord and sendMessage == True):  # stop conversation
                    sendMessage = False
                elif (text == wakeWord and sendMessage == False):  # wake word
                    print("Hello Sir")
                    sendMessage = True
                elif (sendMessage == True):
                    answer = generateRespons(text)
                    print(f"AI:{answer}")
                    assistant.say(answer)
                    assistant.runAndWait()



        except:
            recognizer = speech_recognition.Recognizer()
            continue

model = gpt4all.GPT4All(model_name="orca-mini-3b.ggmlv3.q4_0.bin")
recognizer = speech_recognition.Recognizer()
assistant = tts.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
sendMessage = False
wakeWord = "jarvis"#lower case
sleepWord = "never mind"#lower case
stopProgramm = "stop"#lower case
print("ready")
VoiceRecognition()


