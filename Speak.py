import pyttsx3                                          # pip install pyttsx3

# .............Speak............. #
# ............................... #


def speak_hindi(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
    # print(voices)
    # print(voices[4].id)
    engine.setProperty('rate', 200)
    # print("")
    print(f"AI : {Text}")
    # print("")
    engine.say(Text)
    # engine.save_to_file('')
    engine.runAndWait()

def speak_english(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[5].id)
    # print(voices)
    # print(voices[5].id)
    engine.setProperty('rate', 200)
    # print("")
    print(f"AI : {Text}")
    # print("")
    engine.say(Text)
    # engine.save_to_file('')
    engine.runAndWait()

# speakenglish('welcome back neeraj')
# speakhindi('नमस्ते हेलो नीरज')
