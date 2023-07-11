import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot. I'm here to help you."]
    ],
    [
        r"how are you ?",
        ["I'm doing well. Thank you for asking!"]
    ],
    [
        r"sorry (.*)",
        ["No problem."]
    ],
    [
        r"2+3",
        ["5"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day."]
    ],
]

# Create a chatbot instance using the pairs defined above
chatbot = Chat(pairs, reflections)

# Start the chatbot interaction
print("Welcome to the ChatBot. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    response = chatbot.respond(user_input)
    print(response)
