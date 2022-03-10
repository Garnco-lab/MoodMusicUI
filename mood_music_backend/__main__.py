import pyttsx3 as tts
import speech_recognition
from multiprocessing import Process, Queue
from neuralintents import GenericAssistant

# introduces a recognition software
import pickMusic

recognition = speech_recognition.Recognizer()

# introduces the computer speaker
computerSpeaker = tts.init()
computerSpeaker.setProperty("rate", 150)


def recognize_happy():
    print("happy")
    with open("music-value.txt", "w") as f:
        f.write("1.00")
    pickMusic.wrapper()


def recognize_sad():
    print("sad")
    with open("music-value.txt", "w") as f:
        f.write("0.10")
    pickMusic.wrapper()


def recognize_angry():
    print("angry")
    with open("music-value.txt", "w") as f:
        f.write("0.50")
    pickMusic.wrapper()


def recognize_stop():
    print("stop")
    pickMusic.stop()


mappings = {
    "sad": recognize_sad,
    "happy": recognize_happy,
    "angry": recognize_angry,
    "stop": recognize_stop
}

# The main virtual assistant
virtualAssistant = GenericAssistant("intents.json", intent_methods=mappings)
# trains model automatically from the library
virtualAssistant.train_model()

while True:
    with open('C:\\Users\\Steven\\MoodMusic\\music-value.txt') as f:
        reader = float(f.read())
        print(reader)
    with open('C:\\Users\\Steven\\MoodMusic\\open_program.txt') as g:
        read_words = str(g.read())
        if read_words == "quit":
            quit()
    print(read_words)
    try:
        with speech_recognition.Microphone() as mic:
            recognition.adjust_for_ambient_noise(mic, duration=0.2)
            voice_audio = recognition.listen(mic)

            messenger = recognition.recognize_google(voice_audio)
            messenger = messenger.lower()
        virtualAssistant.request(messenger)
        # re-instantiate voice
    except speech_recognition.UnknownValueError:
        recognition = speech_recognition.Recognizer()
