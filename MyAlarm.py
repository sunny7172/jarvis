import datetime
import winsound
import playsound
import pyttsx3




engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# printa(voices[4].id)
engine.setProperty('voice', voices[4].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def alarm(Timing):
            alttime = str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
        
            alttime = alttime[11:-3]
            print(alttime)
            Horeal =alttime[:2]
            Horeal = int(Horeal)
            Minreal = alttime[3:5]
            Minreal = int(Minreal)
            print(f"Done, alarm is set for {Timing}")
            
            while True:
                if Horeal==datetime.datetime.now().hour:
                    if Minreal==datetime.datetime.now().minute:
                        speak("Sir the time is up")
                        
                        
                    elif Minreal<datetime.datetime.now().minute:
                        break
                        
        
if __name__ == '__main__':
    pass