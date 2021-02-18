from tkinter import Tk, Label
import playsound
import _thread
import time
import json


# Play the alarm in a thread
def playAlarm():
    # Make fullscreen and red
    root.attributes('-fullscreen', True)
    root.config(background = 'red')
    labelTime.config(background = 'red')

    playsound.playsound('Alarm.mp3')

    # Remove fullscreen and set back to black
    root.attributes('-fullscreen', False)
    root.config(background = 'black')
    labelTime.config(background = 'black')

root = Tk()

root.overrideredirect(True)
root.overrideredirect(False)

root.title('Clock')
root.config(background = 'black')

labelTime = Label(root, font = ('calibri', 40, 'bold'), background = 'black', foreground = 'white') 
labelTime.pack(anchor = 'center')

# Read settings.json
def checkAlarm(time):
    f = open("settings.json", "r")
    alarms = json.loads(f.read())['alarms']
    if time in alarms.keys():
        _thread.start_new_thread( playAlarm, () )

# Run in loop at 1s 
def updateTime():
    string = time.strftime('%H:%M:%S')
    labelTime.config(text = string)
    checkAlarm(string)
    labelTime.after(1000, updateTime)
    
updateTime()
root.mainloop()
