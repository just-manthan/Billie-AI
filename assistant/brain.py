import ollama

class BillieBrain:
    def __init__(self, model="llama3.2"):
        self.model = model

    def chat(self, message):
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role" : "user",
                    "content" : message
                }
            ]
        )

        return response["message"]["content"]