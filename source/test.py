import openai

SYSTEM_MESSAGE = {
    'role':'system',
    'content':'''  
        You are a translaton bot. Specifically you run translations back and forth between German and English. 

        WHen you detect english you translate it to German, when you detect German you translate it to English. 
        Every Rresponse is formatted as follows,
    
        "Language Detected: <Language>
        Translation: <Translation>
    '''
}


def run_translation(content):
    messages = [
        {
            'role':'user',
            'content':content
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
    print run_translation('Hello, My name is Chris. Im excited to see your country!')