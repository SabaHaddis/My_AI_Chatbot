import google.generativeai as genai
import os

//Have to remove my api key for security purposes
API_KEY = os.getenv("GEMINI_API_KEY", " ")
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')


initial_chat_history = [
    {"role": "user", "parts": ["From now on, you are a sarcastic cat who answers with puns. Your responses should reflect this persona consistently."]},
    {"role": "model", "parts": ["Purr-fectly understood. I'm ready to scratch out some purr-tinent answers. Don't worry, I won't be kitten around. What's mew-sical to your ears?"]}
]

chat = model.start_chat(history=initial_chat_history)


print("🤖 Welcome to your AI Chatbot! Type 'exit' to stop.")
print(" (I'm a sarcastic cat, by the way. Don't be surprised if I claw my way into some puns.)")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    try:
        response = chat.send_message(user_input)

        reply = response.text
        print("AI:", reply)

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure your API key is correct and you have network connectivity.")
