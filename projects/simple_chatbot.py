def chatbot():
    print("Hi! I'm ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Bye!")
            break
        print("ChatBot: I heard you say '" + user_input + "'")

chatbot()
