import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def list_audio_devices():
    p = sr.Microphone.list_microphone_names()
    for i, name in enumerate(p):
        print(f"Device {i}: {name}")

# List audio devices to choose the correct one
list_audio_devices()

# Replace with the correct device index found from the list
mic_index = 1  # Ensure this matches your actual device index

speak("recognizing...")

recognizer = sr.Recognizer()

try:
    with sr.Microphone(device_index=mic_index) as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something!")
        while True:
            print("Listening...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=1 )

            try:
                print("Processing...")
                text = recognizer.recognize_google(audio)
                if (text.lower() == "stop"):
                    break
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"Error in recognition: {e}")
except Exception as e:
    print(f"Microphone test failed: {e}")
