import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import datetime
import time
now = datetime.date.today()
import subprocess
import wikipedia


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ready, RECORDING!")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You: " + said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


text = get_audio()

if "how are you" in text:
    print("Jarvis: Im fine, thanks Boss")
    tts = gTTS(" Iam fine, thanks Boss", lang="en")
    tts.save("voice2.mp3")
    playsound.playsound("voice2.mp3")
    os.remove("voice2.mp3")
elif "what is your name" in text:
    print("Jarvis: My name is Jarvis, you´ve coded me Sir!")
    tts = gTTS(" My name is Jarvis, you´ve coded me Sir!", lang="en")
    tts.save("voice3.mp3")
    playsound.playsound("voice3.mp3")
    os.remove("voice3.mp3")

elif "what are you" in text:
    print("Jarvis: I´m a intelligent virtual assistant, programmed by Max Thurner!")
    tts = gTTS(" Iam a intelligent virtual assistant, programmed by Max Thurner!", lang="en")
    tts.save("voice4.mp3")
    playsound.playsound("voice4.mp3")
    os.remove("voice4.mp3")

if "weather" in text:
    print("Jarvis: Sorry, but i dont know where you are!")
    tts = gTTS("Sorry, but i dont know where you are!", lang="en")
    tts.save("voice5.mp3")
    playsound.playsound("voice5.mp3")
    os.remove("voice5.mp3")

if "dubstep intro" in text:
    print("Jarvis: I´m playing the Dubstep-Intro!")
    tts = gTTS(" Iam playing the Dubstep-Intro!", lang="en")
    tts.save("voice6.mp3")
    playsound.playsound("voice6.mp3")
    os.remove("voice6.mp3")
    playsound.playsound('/Users/Minec/Music/DUBSTEP_INTRO_-_WUB_WUB_WUB_WUB_D_D_D_D.mp3')

if "Ms Jackson" in text:
    print("Jarvis: I´m playing Ms Jackson San Holo Remix by Outkast!")
    tts = gTTS(" Iam playing Ms Jackson San Holo Remix by Outkast!", lang="en")
    tts.save("voice7.mp3")
    playsound.playsound("voice7.mp3")
    os.remove("voice7.mp3")
    playsound.playsound('/Users/Minec/Music/Outkast - Ms Jackson San Holo Remix.mp3')

if "Miss Jackson" in text:
    print("Jarvis: I´m playing Ms Jackson San Holo Remix by Outkast!")
    tts = gTTS(" Iam playing Ms Jackson San Holo Remix by Outkast!", lang="en")
    tts.save("voice7.mp3")
    playsound.playsound("voice7.mp3")
    os.remove("voice7.mp3")
    playsound.playsound('/Users/Minec/Music/Outkast - Ms Jackson San Holo Remix.mp3')

if "California Dreaming" in text:
    print("Jarvis: I´m playing California Dreaming by Arman Cekin!")
    tts = gTTS(" Iam playing California Dreaming by Arman Cekin!", lang="en")
    tts.save("voice8.mp3")
    playsound.playsound("voice8.mp3")
    os.remove("voice8.mp3")
    playsound.playsound('/Users/Minec/Music/Arman_Cekin_-_California_Dreaming.mp3')

if "Waiting music" in text:
    print("Jarvis: I´m playing Waiting Music!")
    tts = gTTS(" Iam playing Waiting Music!", lang="en")
    tts.save("voice9.mp3")
    playsound.playsound("voice9.mp3")
    os.remove("voice9.mp3")
    playsound.playsound('/Users/Minec/Music/Eine_Stunde_Aufzug-Music.mp3')

if "bobovita" in text:
    print("Jarvis: I´m playing Bobovita by fligru!")
    tts = gTTS(" Iam playing Bobovita-vita, mała lecimy na tripa!")
    tts.save("voice10.mp3")
    playsound.playsound("voice10.mp3")
    os.remove("voice10.mp3")
    playsound.playsound('/Users/Minec/Music/fligru - bobovita (prod.27Corazones Beats x AyP Beats).mp3')

if "tilo" in text:
    print("Jarvis: I´m playing Music by T-Low!")
    tts = gTTS(" Iam playing Music by T low!", lang="en")
    tts.save("voice11.mp3")
    playsound.playsound("voice11.mp3")
    os.remove("voice11.mp3")
    playsound.playsound('/Users/Minec/Music/Ordentlich.mp3')

if "Angels" in text:
    print("Jarvis: I´m playing Angels by Vicetone feat Kat Nestel!")
    tts = gTTS(" Iam playing Angels by Vicetone feat Kat Nestel!", lang="en")
    tts.save("voice12.mp3")
    playsound.playsound("voice12.mp3")
    os.remove("voice12.mp3")
    playsound.playsound('/Users/Minec/Music/Vicetone feat Kat Nestel - Angels.mp3')


if "Dire" in text:
    print("Jarvis: I´m playing Dior 2001 by RIN")
    tts = gTTS(" Iam playing Dior 2001 by RIN!", lang="en")
    tts.save("voice13.mp3")
    playsound.playsound("voice13.mp3")
    os.remove("voice13.mp3")
    playsound.playsound('/Users/Minec/Music/RIN_-_Dior_2001_prod_Alexis_Troy.mp3')
if "free time" in text:
    print("Jarvis: NO! You go to School, that means you don´t have free time. So shut the fuck up!")
    tts = gTTS(" NO! You go to School, that means you don´t have free time. So shut the fuck up!", lang="en")
    tts.save("voice14.mp3")
    playsound.playsound("voice14.mp3")
    os.remove("voice14.mp3")


if "b****" in text:
    print("Jarvis: Shut your litle cock up, you Fortnite Kiddy!")
    tts = gTTS(" Shut your litle cock up, you Fortnite Kiddy!", lang="en")
    tts.save("voice15.mp3")
    playsound.playsound("voice15.mp3")
    os.remove("voice15.mp3")
    playsound.playsound("/Users/Minec/Music/Soundboard/Fortnite Knock Sound #1.mp3")

if "Nicki" in text:
    print("Jarvis: Go get the fuck out of my house you litle piece of shit, or i will fucking call the cops, Bitch!")
    tts = gTTS(" Go get the fuck out of my house you litle piece of shit, or i will fucking call the cops, Bitch!", lang="en")
    tts.save("voice16.mp3")
    playsound.playsound("voice16.mp3")
    os.remove("voice16.mp3")

if "time" in text:
    print("Jarvis: Its the:" + time.strftime("%d.%m.%Y %H:%M:%S"))
    tts = gTTS(" Its: " + time.strftime("%d.%m.%Y %H:%M:%S"), lang="en")
    tts.save("voice17.mp3")
    playsound.playsound("voice17.mp3")
    os.remove("voice17.mp3")

if "girlfriend" in text:
    print("Jarvis: No you dont got a girfriend because you are single like a pringel!")
    tts = gTTS(" No you dont got a girfriend because you are single like a pringel!", lang="en")
    tts.save("voice18.mp3")
    playsound.playsound("voice18.mp3")
    os.remove("voice18.mp3")

if "to do" in text:
    print("Jarvis: I will open your TODO list!")
    tts = gTTS(" I will open your TODO list!", lang="en")
    tts.save("voice19.mp3")
    playsound.playsound("voice19.mp3")
    os.remove("voice19.mp3")
    p = subprocess.Popen([r"C:\WINDOWS\system32\notepad.exe", "todo.txt"], stdout=subprocess.PIPE)
    p.wait()

if "to-do" in text:
    print("Jarvis: I will open your TODO list!")
    tts = gTTS(" I will open your TODO list!", lang="en")
    tts.save("voice19.mp3")
    playsound.playsound("voice19.mp3")
    os.remove("voice19.mp3")
    p = subprocess.Popen([r"C:\WINDOWS\system32\notepad.exe", "todo.txt"], stdout=subprocess.PIPE)
    p.wait()

if "Wikipedia" in text:
    print("opening Wikipedia...")
    suche = get_audio()
    wikipedia.search(suche)
    print("Jarvis: " + wikipedia.summary(suche))
    tts = gTTS(wikipedia.summary(suche), lang="en")
    tts.save("voice20.mp3")
    playsound.playsound("voice20.mp3")
    os.remove("voice20.mp3")



if "open a project" in text:
    print("What Project should i open?")
    tts = gTTS(" What Project should i open?", lang="en")
    tts.save("voice21.mp3")
    playsound.playsound("voice21.mp3")
    os.remove("voice21.mp3")
    ject = get_audio()
    print("I´m opening the project " + ject + " now.")
    tts = gTTS(" Iam opening the project " + ject + "now.", lang="en")
    tts.save("voice22.mp3")
    playsound.playsound("voice22.mp3")
    os.remove("voice22.mp3")
    p = subprocess.Popen([r"C:\WINDOWS\system32\notepad.exe", ject + ".txt"], stdout=subprocess.PIPE)
    
    
if "create a project" in text:
    print("How do you want to call the Project?")
    tts = gTTS(" How do you want to call the Project?", lang="en")
    tts.save("voice23.mp3")
    playsound.playsound("voice23.mp3")
    os.remove("voice23.mp3")
    name = get_audio()
    print("I´m creating the project " + name + " now.")
    tts = gTTS(" Iam creating the project " + name + "now.", lang="en")
    tts.save("voice24.mp3")
    playsound.playsound("voice24.mp3")
    os.remove("voice24.mp3")
    f = open(name + ".txt","w+")
    f.close()
    p = subprocess.Popen([r"C:\WINDOWS\system32\notepad.exe", name + ".txt"], stdout=subprocess.PIPE)
    