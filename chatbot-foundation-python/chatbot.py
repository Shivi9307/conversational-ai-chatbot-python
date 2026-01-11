def chatbot_response(user_input):
    responses = {
        "hi": "Hello! How can I help you?",
        "hello": "Hi there!",
        "bye": "Goodbye! Have a nice day.",
        "help": "I can answer basic questions.",
        "can you explain about you":"I am a firt chatbot which developed by Shivani Thakur"
    }
    user_input = user_input.lower()
    return responses.get(user_input, "Sorry, I didn't understand that.")

while True:
    user =  input("You: ")
    if user.lower() == "exit": 
        break
    print("Bot: ", chatbot_response(user))