import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    message = response.choices[0].message.content
    return message


while True:
    user_input = input("Ich: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    prompt = f"User: {user_input}\nGPT: "
    response = generate_response(prompt)
    print("GPT:", response)
