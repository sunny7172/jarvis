import qrcode as qr
import pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# printa(voices[1].id)
engine.setProperty('voice',voices[4].id)

def speak(audio):
    print(f"AI: {audio}")
    engine.say(audio)
    engine.runAndWait()
def qrcode():
    try:
        speak("Ok sir for that plese enter link")
        f = input("Plese enter link: ")
        img = qr.make(f)
        name = input("enter file name: ")
        if ".png" in name:
            name = name.replace(".png","")
        if "png" in name:
            name = name.replace("png", "")
        img.save(f"{name}.png")

    except Exception as e:
         print("Some error occupied")
