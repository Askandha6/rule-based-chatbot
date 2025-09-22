This is a simple *rule-based chatbot* built using Python.  
It uses basic if-else conditions to respond to user input with predefined answers.

The chatbot can:
- Greet the user
- Introduce itself
- Respond to simple queries
- Exit when the user types bye
- *Keyword Matching*: Detects specific words like "hello", "how are you", "help".
- *Loop Interaction*: Keeps chatting until the user types bye.
- *Case Insensitive*: Works regardless of input case (Hello, HELLO, hello are the same).
- Python 3.x (No external libraries needed)
1. Save the chatbot code in a file, e.g., chatbot.py.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
  

Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.
You: hello
Chatbot: Hello! How can I help you?
You: how are you
Chatbot: I'm just a program, but I'm doing great! Thanks for asking.
You: your name
Chatbot: I’m ChatBot 1.0, your friendly assistant.
You: bye
Chatbot: Goodbye! Have a nice day.
📖 How It Works
User input is taken with input().
The text is converted to lowercase to avoid case mismatches.
The chatbot checks for specific keywords using if-elif-else.
If no match is found, it gives a default "didn’t understand" message.
Typing bye ends the conversation.
Add more responses and rules.
Use regular expressions for smarter matching.
Extend with NLP libraries like NLTK or spaCy for better understanding.
