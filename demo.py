import os
import fakeopenai as openai
# openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke with 1000 words."},
    ]
)


assistant_reply = response['choices'][0]['message']['choices'][0]['message']['content']
print("Assistant:", assistant_reply)