from openai import OpenAI
import os

#getting api key from os
#implemented an AI Chatbot using openrouter

api_key =os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY NOT FOUND")
 
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key
)
chat_history = []
personas = {
        "default": "You are a helpful AI Assistant",
        "sarcastic": "Your are a sarcastic AI who gives witty and mocking responses",
        "poet": "You are a poetic AI that responds in rhymes and verses"
}

print("Choose a persona : (defualt / sarcastic / poet)")

user_persona_input = input("Enter Persona :").strip().lower()

persona = personas.get(user_persona_input, personas["poet"])

chat_history.append({"role": "system", "content": personas["poet"]})

while True:
 
    user_input = input("Enter Your Prompt:")

    if user_input == "clear":
        chat_history = []
        chat_history.append({"role": "system", "content": personas["poet"]})

    print("chat history cleared")
    continue

    chat_history.append({"role": "user", "content": user_input})
    if user_input == "exit":
        break
 
    completion = client.chat.completions.create(
 
    model="deepseek/deepseek-r1-zero:free",
    messages=chat_history
    )
    response = completion.choices[0].message.content
    print(response)

    chat_history.append({"role": "user", "content": user_input})
