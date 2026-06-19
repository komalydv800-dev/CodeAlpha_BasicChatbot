def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")
        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand.")

chatbot()
