import ollama
from assistant.memory import ConversationMemory

class BillieBrain:
    def __init__(self, model="llama3.2"):
        self.model = model
        self.memory = ConversationMemory()

    def chat(self, message):
        self.memory.add_user_message(message)

        response = ollama.chat(
            model=self.model,
            messages=self.memory.get_messages()
        )

        ai_response = response["message"]["content"]

        self.memory.add_assistant_message(ai_response)

        return ai_response