from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access your API key like this
# api_key = os.getenv("OPENAI_API_KEY")
api_key = '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'
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

flask_app = Flask(__name__)

@flask_app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        translation = run_translation(user_input)
        return render_template('index.html', user_input=user_input, translation=translation)
    return render_template('index.html')

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

    return response['choices'][0]['message']

if __name__ == '__main__':
    app.run(debug=True)
