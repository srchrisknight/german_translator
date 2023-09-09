import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access your API key like this
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

SYSTEM_MESSAGE = {
    'role': 'system',
    'content': '''
        You are a translation bot. Specifically, you run translations back and forth between German and English.

        When you detect English, you translate it to German, and when you detect German, you translate it to English.
        Every response is formatted as follows,

        "Language Detected: <Language>
        Translation: <Translation>
    '''
}

def run_translation(content):
    messages = [
        {
            'role': 'user',
            'content': content
        }
    ]

    messages.append(SYSTEM_MESSAGE)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=512  # limiting the tokens as we only want the question, no greetings or sign-offs
    )

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    while True:
        user_input = input("Enter a sentence to translate (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        translation = run_translation(user_input)
        print(translation)
