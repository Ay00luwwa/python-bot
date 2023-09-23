greeting = "Hello there welcome to my AYO IJI bot"

def display_greeting(name):
    return f"Hello, {name} how are you today? "

#calculator
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed.")
        return x / y

    def multiply(self, x, y):
        return x * y

    def evaluate(self, expression):
        try:
            # Only allow basic arithmetic operations
            allowed_chars = set('0123456789.+-*/ ')
            if set(expression) <= allowed_chars:
                return eval(expression)
            else:
                raise ValueError("Invalid characters in expression")
        except Exception as e:
            raise e

        
        
colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
}

def get_color(code):
    return colors.get(code, "Color not found")


# User Types
user_types = ['admin', 'editor', 'viewer', 'guest']

# Common User Queries
common_queries = {
    "python": "Python is a versatile programming language used for web development, data analysis, AI, and more.",
    "html": "HTML stands for HyperText Markup Language and is used to structure content on the web.",
    "ai": "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines.",
    "gpt-3": "GPT-3, developed by OpenAI, is a state-of-the-art language processing AI model.",
    "a.i": "AI stands for Artificial Intelligence, which refers to the simulation of human intelligence in machines.",
    "chatbot": "A chatbot is a software application designed to simulate human conversation. It can chat with a user in a natural language like English.",
    "your name": "As of my creation on the 27th of August, I was named after the developer Ayo Iji, I am basically a text-based ai"

}

# Operating Systems
operating_systems = ['Windows', 'MacOS', 'Linux', 'Android', 'iOS']

# Common File Extensions
file_extensions = {
    "py": "Python File",
    "html": "HTML File",
    "js": "JavaScript File",
    "css": "Cascading Style Sheets File",
    "txt": "Plain Text File"
}

# AI Frameworks & Libraries
ai_frameworks = ['TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'NLTK']

# User feedback options
feedback_options = ['Excellent', 'Good', 'Average', 'Poor']

# Days in a week
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Support links or documentation URLs
support_links = {
    "python": "https://docs.python.org/3/",
    "html": "https://developer.mozilla.org/en-US/docs/Web/HTML",
    "css": "https://developer.mozilla.org/en-US/docs/Web/CSS",
    "javascript": "https://developer.mozilla.org/en-US/docs/Web/JavaScript",
    "ai": "https://openai.com/research/"
}

