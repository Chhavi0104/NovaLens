import pyttsx3

tts = pyttsx3.init()

def speak_text(original_text):
    text = original_text.strip()
    if not text:
        print("No text detected")
        tts.say("No text detected")
        tts.runAndWait()

    else:
        print(text)
        tts.say(text)
        tts.runAndWait()