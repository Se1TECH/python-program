# basic chatbot in python

import random

def get_greeting():
    greetings = ["Hello!","Hi There!","Greetings!","Nice to Meet You!"]
    return random.choice(greetings)

# funtion to generate response
def get_response(user_input):
    user_input = user_input.lower()
    if "how are you" in user_input:
        return "I'm good, thank you! how about you?"
    elif "your name" in user_input:
        return "My name is 7tech ChatBot. Nice to meet you. "
    elif "weather" in user_input:
        return "The weather is nice today."
    elif "bye" in user_input:
        return "Goodbye! It was nice talking to you."
    else:
        return "Sorry I didn't understand that. can you please rephrase."


# Main conversation loop
def chat():
    print(get_greeting())
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break
        response = get_response(user_input)
        print("ChatBot: ",response)

#start conversation
chat()
