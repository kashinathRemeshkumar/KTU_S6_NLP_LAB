responses = {
    "hi": "Hello!",
    "hello": "Hey there!",
    "hey": "Hi!",
    "how are you": "I'm fine! How about you?",
    "what is your name": "I AM GROOT",
    "bye": "Goodbye!",
    "goodbye": "Goodbye!"
}

print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    
    if user_input in responses:
        print("Chatbot:", responses[user_input])
    else:
        print("Chatbot: I don't understand.")
    
    if user_input in {"bye", "goodbye"}:
        break
