def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot.")
    print("Chatbot: Type 'bye' or 'exit' to stop the conversation.")

    while True:
        user = input("You: ").lower().strip()

        
        if user in ["hi", "hello", "hey", "hii"]:
            print("Chatbot: Hello! Nice to meet you.")

        elif user in ["good morning", "morning"]:
            print("Chatbot: Good morning! Have a great day.")

        elif user in ["good evening", "evening"]:
            print("Chatbot: Good evening! How was your day?")

        elif user in ["good night", "night"]:
            print("Chatbot: Good night! Sleep well.")

     
        elif user in ["how are you", "how are u", "how is it going"]:
            print("Chatbot: I'm fine, thanks! How about you?")

        elif user in ["what are you doing", "what r u doing"]:
            print("Chatbot: I'm chatting with you right now!")

        elif user in ["what about you", "and you"]:
            print("Chatbot: I'm doing great! Thanks for asking.")

        elif user in ["what is your name", "who are you"]:
            print("Chatbot: I'm a simple Python rule-based chatbot.")

        
        elif user in ["thank you", "thanks", "thank u"]:
            print("Chatbot: You're welcome! ")

        
        elif user in ["help", "can you help me"]:
            print("Chatbot: Sure! I can chat with you using predefined responses.")

        
        elif user in ["what can you do", "what do you do"]:
            print("Chatbot: I can respond to simple questions and greetings.")

        elif user in ["tell me a joke", "joke"]:
            print("Chatbot: Why did the computer go to the doctor?")
            print("Chatbot: Because it had a virus! ")

    
        elif user in ["bye", "exit", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Take care. ")
            break

    
        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()