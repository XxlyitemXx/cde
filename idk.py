import pyttsx3
import speech_recognition as sr
import datetime
import os
import face_rec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commands():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        #
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-EN')

        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

# ฟังก์ชั่นนี้ต้องการให้ผู้ใช้ตามเวลาของวัน


def wishings():
    # รับชั่วโมงปัจจุบัน
    hour = int(datetime.datetime.now().hour)
    # ถ้าชั่วโมงอยู่ระหว่าง 0 ถึง 12, ให้พูดว่า Good Morning
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    # ถ้าชั่วโมงอยู่ระหว่าง 12 ถึง 18, ให้พูดว่า Good Afternoon
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    # มิฉะนั้น, ให้พูดว่า Good Evening
    else:
        speak("Good Evening!")

    # สุดท้ายนี้ขอให้ผู้ใช้ พูดว่า สวัสดี และ ชื่อของผู้ใช้
    speak("I am Jarvis Sir. Please tell me how may I help you")


if __name__ == "__main__":

    while True:
        wishings()  # ให้เรียกใช้ฟังก์ชั่น wishings
        # รับคำสั่งจากฟังก์ชั่น commands และเปลี่ยนเป็นตัวพิมพ์เล็กทั้งหมด
        query = commands().lower()
        if 'time' in query:

            # ใช้เมธอด now() เพื่อรับเวลาปัจจุบันมาและเมธอด strftime() เพื่อทำให้เวลาอยู่ในรูปแแบบข้อความ
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # ใช้ฟังก์ชัน speak() เพื่อพูดเวลา
            speak(f"Sir, the time is {strTime}")

        elif 'open browser' in query:
            # ใช้ฟังก์ชัน speak() เพื่อพูดว่า กำลังเปิด Firefox
            speak("Opening Browser")
            # ใช้ฟังก์ชัน webbrowser.open() เพื่อเปิด Firefox
            os.startfile(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
