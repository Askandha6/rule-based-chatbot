def chatbot():
    print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easy matching
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        
        elif "your name" in user_input:
            print("Chatbot: I’m ChatBot 1.0, your friendly assistant.")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        
        elif "help" in user_input:
            print("Chatbot: Sure! I can answer simple greetings, tell you my name, and respond to 'bye'.")
        
        else:
            print("Chatbot: Sorry, I didn’t understand that. Can you try again?")
chatbot()
