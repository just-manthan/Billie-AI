from assistant.brain import BillieBrain
from assistant.speech import BillieSpeech
from assistant.commands import BillieCommands

def main():
    print("=" * 50)
    print("Welcome to Billie AI by Just Manthan")
    print("=" * 50)

    brain = BillieBrain()
    speech = BillieSpeech()
    commands = BillieCommands()

    print("\nChoose how you want to use Billie:")
    print("1 - Keyboard")
    print("2 - Voice")

    mode = input("\nChoose mode: ").strip()

    # Keyboard Mode
    if mode == "1":

        print("\nKeyboard mode activated ⌨️")

        while True:

            user_input = input("\nYou: ").strip()

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nPeace out!")
                break

            if not user_input:
                continue

            response = commands.execute(user_input)

            if response is None:
                response = commands.execute(user_input)

            if response is None:
                response = brain.chat(user_input)

            print(f"\nBillie: {response}")

    # Voice Mode
    elif mode == "2":

        print("\nVoice mode activated 🎤")

        while True:

            user_input = speech.listen()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nPeace out!")
                break

            response = commands.execute(user_input)

            if response is None:
                response = brain.chat(user_input)

            print(f"\nBillie: {response}")

    else:

        print("\nInvalid option. Please restart Billie and choose 1 or 2.")


if __name__ == "__main__":
    main()