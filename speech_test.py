from assistant.speech import BillieSpeech

speech = BillieSpeech()

while True:

    text = speech.listen()

    if text:

        if text.lower() == "exit":

            break