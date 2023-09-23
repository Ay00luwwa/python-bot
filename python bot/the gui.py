import random
import tkinter as tk
from tkinter import ttk
from mylib import display_greeting, common_queries, Calculator
from tkinter import scrolledtext

# Your chatbot_response function here
def chatbot_response(text):
    text = text.lower()
    calc = Calculator()
    greetings = ["Hello there!", "It's a nice weather today, how can I be of help😀",
                 "Hello", "A.I bot at your service"
                 ]
    how_are_you = ["I'm just a bunch of code, but thanks for asking!", 
                   "I'm digital. So, no feelings, but I'm running fine!",
                   "Feeling 1's and 0's, thanks for asking!"
                   ]
    bye_responses = ["Goodbye! Have a great day!", "See you later!",
                     "Bye! Take care!"]
    
    # Define some rules for our bot
    if "hello" in text:
        return random.choice(greetings)
    elif "how are you" in text:
        return random.choice(how_are_you)
    elif "bye" in text:
        return random.choice(bye_responses)
    elif "what is python" in text:  
        return user_queries(text)   
    elif "what is" in text:  # Check if user's query starts with "what is"
        keyword = text.split("what is")[-1].strip()  # Extract keyword after "what is"
        return common_queries.get(keyword, "Sorry, I don't have information on that topic.")
    elif "calculate" in text:
        expression = extract_expression(text).split()
        
        # Check if we have the correct format (e.g., "3 + 5")
        if len(expression) == 3:
            x, operation, y = expression
            x, y = float(x), float(y)  # Convert strings to numbers

            # Now, based on the operation, use the appropriate Calculator method
            if operation == "+":
                return str(calc.add(x, y))
            elif operation == "-":
                return str(calc.subtract(x, y))
            elif operation == "*":
                return str(calc.multiply(x, y))
            elif operation == "/":
                if y == 0:  # Check for division by zero
                    return "Cannot divide by zero."
                return str(calc.divide(x, y))
            else:
                return "Sorry, I couldn't perform that calculation."
        else:
            return "Please provide a valid expression for calculation."
    
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
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("SimpleBot Chat")
        self.geometry("600x400")
        self.resizable(True, True)
        self.minsize(500, 400)

        # Styling
        style = ttk.Style()
        style.configure("TEntry", font=("Arial", 12), relief="groove")
        style.configure("TButton", font=("Arial", 12))
        # Note: If you'd like to further customize the look, you'd define more styles here

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, bg="#00FFFF", font=("Arial", 12))
        self.chat_display.config(state=tk.DISABLED)  # Make it read-only
        self.chat_display.pack(pady=(20, 10), padx=20, expand=True, fill=tk.BOTH)

        # User input
        self.user_input = ttk.Entry(self)
        self.user_input.pack(pady=(5, 20), padx=(20, 10), side=tk.LEFT, expand=True, fill=tk.X)
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        send_button = ttk.Button(self, text="Send", command=self.send_message)
        send_button.pack(pady=(5, 20), padx=(10, 20), side=tk.RIGHT)
        
        
    def draw_user_bubble(self, message):
        # Create a Canvas to contain the chat bubble
        canvas = tk.Canvas(self.chat_display, bg="#f5f5f5", highlightthickness=0)
        canvas.insert(tk.END, window=canvas)
        
        # Calculate bubble width and height based on the message
        text_width = canvas.textlength(message, font=("Arial", 12)) + 20
        text_width = min(self.chat_display.winfo_width() - 30, text_width)  # Limit width
        bubble_width = text_width + 20
        bubble_height = 60  # static height for simplicity
        
        # Create a rounded rectangle (the bubble) on the canvas
        x1 = self.chat_display.winfo_width() - bubble_width - 10  # Align to right
        y1 = 5
        x2 = x1 + bubble_width
        y2 = y1 + bubble_height
        radius = 10  # border-radius
        canvas.create_rounded_rect(x1, y1, x2, y2, radius=radius, fill="blue")  # custom method to draw rounded rectangle
        
        # Add the message text to the canvas inside the bubble
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=message, font=("Arial", 12), fill="white", width=text_width)
        
        canvas.pack(fill=tk.BOTH, expand=tk.TRUE, padx=10, pady=5)
        
    def draw_rounded_rect(self, canvas, x1, y1, x2, y2, radius, **kwargs):
        points = [x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2-radius, y2-radius,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1+radius, y1+radius]
        return canvas.create_polygon(points, **kwargs, smooth=True)

        

    def send_message(self, event=None):
        query = self.user_input.get()
        if query:
            self.display_message(query, "User")
            response = chatbot_response(query)
            self.display_message(response, "Bot")
            self.user_input.delete(0, tk.END)

    def display_message(self, message, sender):
        self.chat_display.config(state=tk.NORMAL)  # Enable editing
        if sender == "User":
            self.chat_display.tag_configure("right", justify="right")
            self.chat_display.insert(tk.END, message + "\n", "right")
        else:
            self.chat_display.tag_configure("left", justify="left")
            self.chat_display.insert(tk.END, message + "\n", "left")
        self.chat_display.config(state=tk.DISABLED)  # Disable editing
        self.chat_display.yview(tk.END)
        
        
        

if __name__ == "__main__":
    app = SimpleBot()
    app.mainloop()

