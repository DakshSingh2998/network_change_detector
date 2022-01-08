from requests import get
from playsound import playsound
import time
from gtts import gTTS
import os
import keyboard
import threading
import ctypes
import win32api

def pause():
    global befip
    global ip
    global text_val
    global obj
    while True:
        try:
            ip=get('https://api.ipify.org').text
            if befip!=ip:
                text_val='ip '+ip[0:3]
                print(text_val)
                language = 'hi'
                obj = gTTS(text=text_val,tld='co.in', lang=language, slow=False)
                playsound("starting.mp3")
                os.remove("test.mp3")
                obj.save("test.mp3")
                playsound("test.mp3")
                befip=ip
        except Exception as e:
            befip=None
            playsound("starting.mp3")
            playsound("nonet.mp3")
            print(e)
            print('No Net')
        finally:
            time.sleep(5)
            pass

befip = None
print('Started')
ip=None
text_val=None
obj=None
th = threading.Thread(target=pause)
th.start()
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

while True:
    try:
        if keyboard.is_pressed('/'):
            playsound('starting.mp3')
            playsound('test.mp3')
    except Exception as e:
        print(e)
    finally:
        time.sleep(1)


pass
