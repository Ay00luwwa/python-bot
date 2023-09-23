import tkinter as tk
from tkinter import ttk
from mylib import display_greeting, common_queries

# ... [your functions like chatbot_response, user_queries, etc.]

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

class SimpleBot(tk.Tk):
    # ... [rest of the SimpleBot class code]
    def __init__(self):
            super().__init__()

            self.title("SimpleBot Chat")
            self.geometry("500x400")

            self.chat_display = ttk.Treeview(self, columns=("User", "Bot"), show="headings")
            self.chat_display.heading("User", text="You")
            self.chat_display.heading("Bot", text="SimpleBot")
            self.chat_display.pack(pady=20, padx=20, expand=True, fill=tk.BOTH)

            self.user_input = ttk.Entry(self)
            self.user_input.pack(pady=20, padx=20, side=tk.LEFT, expand=True, fill=tk.X)
            self.user_input.bind("<Return>", self.send_message)

            send_button = ttk.Button(self, text="Send", command=self.send_message)
            send_button.pack(pady=20, padx=20, side=tk.RIGHT)


    def send_message(self, event=None):
        app = SimpleBot()
        app.mainloop()
