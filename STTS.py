import speech_recognition as sr
import pyttsx3
a = 1
while a == 1:
 listener = sr.Recognizer()
 try:
  with sr.Microphone() as source:
        print("...")
        voice = listener.listen(source)
        #switch between two modules by commenting one out
        #command = listener.recognize_sphinx(voice)
        command = listener.recognize_google(voice)
        print(command)
        speech = pyttsx3.init()
        speech.say(command)
        speech.runAndWait()
 except:
  pass