import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create a prompt
response = client.chat.completions.create(
    model="gemini-2.0-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ]
)

print(response.choices[0].message.content)