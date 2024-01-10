# openai_client.py
import openai

class OpenAI:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_paragraph(self, prompt="Generate a paragraph about a specific topic", max_tokens=100):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

