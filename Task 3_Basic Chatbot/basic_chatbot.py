# TASK 4: Basic Chatbot
# A simple rule-based chatbot

def chatbot():

    print("=" * 50)
    print("             🤖 WELCOME TO PY-BOT 🤖")
    print("=" * 50)
    print("Bot: Hello! I am Py-Bot.")
    print("Bot: I am a simple rule-based chatbot.")
    print("Bot: Let's have a small conversation!")
    print("Bot: Type 'help' to see what I can understand.")
    print("Bot: Type 'bye' to end the chat.")
    print("-" * 50)

    while True:

        user_input = input("You: ").lower().strip()

        # Greeting
        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! 👋 Nice to meet you!")

        # Asking about chatbot
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! 😊")
            print("Bot: I hope you are doing great too!")

        # Name
        elif user_input == "what is your name":
            print("Bot: My name is Py-Bot. 🤖")

        # Identity
        elif user_input == "who are you":
            print("Bot: I am a simple Python-based chatbot.")
            print("Bot: I reply using predefined rules.")

        # User's name
        elif user_input == "my name is anshika":
            print("Bot: Nice to meet you, Anshika! 😊")

        # Python
        elif user_input == "do you like python":
            print("Bot: Yes! 🐍 Python is simple and beginner-friendly.")

        # Study
        elif user_input == "what can you do":
            print("Bot: I can have a simple conversation with you.")
            print("Bot: I can respond to greetings and some predefined questions.")

        # Hobby
        elif user_input == "what is your hobby":
            print("Bot: My hobby is chatting with users! 😄")

        # Thanks
        elif user_input == "thank you" or user_input == "thanks":
            print("Bot: You're welcome! 😊")

        # Help
        elif user_input == "help":
            print("\nBot: Here are some messages you can try:")
            print("     → hello")
            print("     → how are you")
            print("     → what is your name")
            print("     → who are you")
            print("     → my name is anshika")
            print("     → do you like python")
            print("     → what can you do")
            print("     → what is your hobby")
            print("     → thank you")
            print("     → bye")

        # Exit
        elif user_input == "bye":
            print("Bot: It was nice chatting with you! 👋")
            print("Bot: Goodbye! Have a great day! 😊")
            print("=" * 50)
            break

        # Unknown input
        else:
            print("Bot: Hmm... I don't understand that yet. 🤔")
            print("Bot: Type 'help' to see what I can understand.")

# Start the chatbot
chatbot()
