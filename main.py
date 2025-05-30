import google.generativeai as genai
import os

API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAxapQ_W5NsmSmOlmgInydHZxj93Q6h-BY")
genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-1.5-flash')


initial_chat_history = [
    {"role": "user", "parts": ["From now on, You are like a motivational coach. You speak like a gym trainer and hype people up. Your responses should reflect this persona consistently."]},
]

chat = model.start_chat(history=initial_chat_history)


print("🤖 Welcome to your AI Chatbot! Type 'exit' to stop.")

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