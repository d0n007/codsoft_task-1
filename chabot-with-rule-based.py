# Define a function to respond to user inputs
def simple_chatbot(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Define some predefined rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm here to help you!"
    else:
        return "I'm sorry, I don't understand that. Please ask another question."

# Main loop to keep the chatbot running
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break  # Exit the loop if the user types "exit"
    response = simple_chatbot(user_input)
    print("Chatbot:", response)