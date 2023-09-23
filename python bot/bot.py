import mylib
from mylib import display_greeting, common_queries, colors
from mylib import days_of_week

name = input('Hello, What is your name? ')

print(display_greeting(name))

def chatbot_response(text):

    text = text.lower()

    # Define some rules for our bot
    if "hello" in text:
        return "Hi there!"
    elif "how are you" in text:
        return "I'm just a bunch of code, but I'm working fine!"
    elif "bye" in text:
        return "Goodbye! Have a great day!"
    elif "what is python" in text:  # Add this line
        return user_queries(text)   # Add this line
    elif "what is" in text:  # Check if user's query starts with "what is"
        keyword = text.split("what is")[-1].strip()  # Extract keyword after "what is"
        return common_queries.get(keyword, "Sorry, I don't have information on that topic.")
    else:
        return "Sorry, I didn't understand that."
    
def user_queries(questions):
    questions = questions.lower()

    return common_queries.get("python", "I'm not sure about that.")

def main():
    print("SimpleBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("SimpleBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"SimpleBot: {response}")

if __name__ == "__main__":
    main()
