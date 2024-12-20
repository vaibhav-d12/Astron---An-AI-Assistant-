import os
import eel 

from Engine.features import *
from Engine.command import *
from Engine.auth import recoganize


def start():
    
    eel.init("Frontend")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome to the AI Assistant. How can i help you")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html',mode=None,host='localhost',block=True)