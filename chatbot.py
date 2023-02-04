import speech_recognition as sr
import pyttsx3

def chatbot():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    
    responses = {
        "what's your name?": "My name is Bot.",
        "what can you do?": "I can chat with you and answer your questions.",
        "default": "I'm not sure what you're asking."
    }

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Hi, I'm a chatbot. How can I help you today?")
        engine.say("Hi, I'm a chatbot. How can I help you today?")
        engine.runAndWait()
        while True:
            audio = recognizer.listen(source)
            message = recognizer.recognize_google(audio)
            if message in responses:
                response = responses[message]
                print("You: " + message)
                print("Bot: " + response)
                engine.say(response)
                engine.runAndWait()
            else:
                response = responses["default"]
                print("You: " + message)
                print("Bot: " + response)
                engine.say(response)
                engine.runAndWait()

if __name__ == "__main__":
    chatbot()
