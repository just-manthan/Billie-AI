import speech_recognition as sr


class BillieSpeech:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\n Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            print(f"\n You: {text}")

            return text

        except sr.UnknownValueError:

            print("\n Sorry, I couldn't understand.")

            return None

        except sr.RequestError:

            print("\n Speech service unavailable.")

            return None