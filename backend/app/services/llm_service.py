import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class InterviewLLM:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        # Updated model
        self.model = "llama-3.1-8b-instant"

    def generate_response(self, messages):

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.3,
            max_tokens=100
        )

        return response.choices[0].message.content