from assistant.brain import BillieBrain

def main():
    print("=" * 50)
    print("Welcome to Billie AI by Just Manthan")
    print("=" * 50)

    brain =BillieBrain()

    while True:
        user_input = input("\n You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n Peace out!")
            break

        response = brain.chat(user_input)
        print(f"\n Billie: {response}")

if __name__=="__main__":
    main()