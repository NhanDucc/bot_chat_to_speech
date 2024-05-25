import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    # listen
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.record(mic, duration = 5)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    # understand
    # Thay AI vô đây
    if you == '':
        robot_brain = "I can't hear you, try again"
    elif 'name' in you:
        robot_brain = "My name is Robot"
    elif 'hello' in you:
        robot_brain = "Hello"
    elif 'today' in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif 'time' in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes")
    elif 'bye' in you:
        robot_brain = "Goodbye"
        print('Robot: ' + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine, thank you"
    
    print('Robot: ' + robot_brain)
    # speak
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
