# import pyttsx3 as pt
# sagun = pt.init()

# voices = sagun.getProperty('voices')
# print("Number of voices:", len(voices))

# for i, voice in enumerate(voices):
#     print("Voice", i)
#     print("ID:", voice.id)
#     print("Name:", voice.name)
#     print()
# rate = sagun.getProperty('rate')
# print(rate)
# sagun.setProperty('rate',150)

# sagun.setProperty('voice',voice[1].id)
# print("Speaking 1")
# sagun.say("Durgesh Nai!!! kya kar raha hai ")
# sagun.runAndWait()

# print("Speaking 2") 
# sagun.say("Myself Sagun Kumar Bhagat")
# sagun.runAndWait()

# print("Speaking 3")
# sagun.say("My speed is "+str(rate))
# sagun.runAndWait()
# sagun.stop()

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Voices:", len(voices))

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

print("Starting speech...")

engine.say("Hello world")
engine.say("This is Sagun")
engine.say("This is the third sentence")

print("Running engine...")

engine.runAndWait()

print("Speech finished")