import datetime

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking 😊"

    elif "your name" in user_input:
        return "I am a simple rule-based chatbot."

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif "help" in user_input:
        return "I can answer simple questions like greetings, time, or my name."

    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()