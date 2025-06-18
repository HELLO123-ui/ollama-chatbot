import ollama

def chat():
    print("🤖 Lightweight Chatbot - Powered by Ollama (phi3:mini)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        response = ollama.chat(
            model="phi3:mini",
            messages=[{"role": "user", "content": user_input}]
        )

        print("AI:", response['message']['content'])

chat()
