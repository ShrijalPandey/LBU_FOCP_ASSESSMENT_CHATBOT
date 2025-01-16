import tkinter as tk
import random
from datetime import datetime

responses = {
    # Predefined responses to common campus-related queries
    "coffee": "The campus coffee shop is open from 8 AM to 5 PM.",
    "library": "The library is open 24/7 for students.",
    "wifi": "Campus Wi-Fi is available in all buildings.",
    "cafeteria": "The cafeteria is open from 7 AM to 7 PM.",
    "parking": "Parking is free for students.",
    "events": "You can find upcoming campus events on the college website.",
    "sports": "The sports ground is open from 6 AM to 10 PM.",
    "timings": "The college timing is from 7 AM to 11 AM for morning shift and 12 PM to 3 PM for evening shift.",
    "grades": "You can check your grades on the student portal on the college website.",
    "help": "Feel free to ask any campus-related question!",
}
# Random fallback responses for unrecognized queries
random_responses = [
    "That's interesting, could you be more specific?",
    "I'm not sure about that.",
    "Can you please rephrase the question?",
    "Let me think about that.",
]
# List of chatbot agent names for random selection
agent_names = ["Stefen", "Micra", "Tayler", "Wisey", "Bravo"]

# Select a random chatbot agent name
agent_name = random.choice(agent_names)

# Generate a unique log file for the chat history
log_file = f"chat_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Easter egg responses for specific keywords. This makes chatbot more engaging and entertaining.
easter_eggs = {
    "who are you": f"I'm {agent_name}, your friendly virtual assistant!",
    "joke": "Why did the student eat his homework? Because the teacher said it was a piece of cake!",
    "quote": "You must be the change, you wish to see in the world.",
    "game": "I'd love to play, but I'm a bit stuck in this chatbot world!",
}

# Variable to store the user's name after the first interaction
user_name = None

# Function to log the conversation to a file
def log_conversation(message):
    with open(log_file, "a") as log:
        log.write(message + "\n")

# Function to handle user input and provide chatbot responses
def send_message():
    global user_name
    user_input = user_entry.get()  # Get user input from the entry field
    if user_input.strip() == "":  # Ignore empty input
        return

    # Display user input in the chatbox
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user_message")
    log_conversation(f"You: {user_input}")
    user_entry.delete(0, tk.END)  # Clear the entry field

    # Handle first interaction: asking for the user's name
    if user_name is None:
        user_name = user_input
        chatbot_response = (
            f"Hello {user_name}. Nice to meet you. How can I assist you today? "
            "Feel free to ask me any questions about the campus. If you don't find the answer you're looking for, "
            "you can reach out to us directly at our campus number: 014513646."
        )
        chat_box.insert(tk.END, f"{agent_name}: {chatbot_response}\n", "chatbot_message")
        log_conversation(f"{agent_name}: {chatbot_response}")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        return

    # Handling the exit commands
    if user_input.lower() in ["bye", "quit", "exit"]:
        chatbot_response = f"Goodbye, {user_name}! Have a great day!"
        chat_box.insert(tk.END, f"{agent_name}: {chatbot_response}\n", "chatbot_message")
        log_conversation(f"{agent_name}: {chatbot_response}")
        chat_box.config(state=tk.DISABLED)
        app.after(4000, app.quit)  # Close the app after 4 seconds
        return

    # Check for easter egg responses or predefined answers
    user_input_lower = user_input.lower()
    if user_input_lower in easter_eggs:
        chatbot_response = easter_eggs[user_input_lower]
    else:
        # Search for matching keywords in predefined responses
        chatbot_response = next(
            (response for keyword, response in responses.items() if keyword in user_input_lower), None
        )
        # Use a random fallback response if no match is found
        chatbot_response = chatbot_response or random.choice(random_responses)

    # Display chatbot response in the chatbox
    chat_box.insert(tk.END, f"{agent_name}: {chatbot_response}\n", "chatbot_message")
    log_conversation(f"{agent_name}: {chatbot_response}")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# Function to reset the chat history
def reset_chat():
    global user_name
    user_name = None  # Reset the user name
    chat_box.config(state=tk.NORMAL)
    chat_box.delete("1.0", tk.END)  # Clear the chatbox
    chat_box.insert(
        tk.END,
        f"{agent_name}: Hi! I'm {agent_name}, your virtual assistant. Please enter your name?\n",
        "chatbot_message",
    )
    chat_box.config(state=tk.DISABLED)

# Function to close the application
def exit_app():
    app.quit()

# Initialize the GUI application
app = tk.Tk()
app.title("Chatbot")  # Set the window title
app.geometry("900x550")  # Set the window size

# Chat display area
chat_box = tk.Text(app, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
chat_box.tag_config("user_message", background="#E1E1E1", foreground="black")
chat_box.tag_config("chatbot_message", background="#D3D3D3", foreground="black")
chat_box.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Display initial chatbot message
chat_box.config(state=tk.NORMAL)
chat_box.insert(
    tk.END,
    f"{agent_name}: Hi! I'm {agent_name}, your virtual assistant. Please enter your name?\n",
    "chatbot_message",
)
chat_box.config(state=tk.DISABLED)

# Input frame for user interaction
input_frame = tk.Frame(app)
input_frame.pack(pady=10)

# Input field for user messages
user_entry = tk.Entry(input_frame, font=("Arial", 14), width=50)
user_entry.grid(row=0, column=0, padx=5, pady=5)

# Buttons for sending messages, resetting, and exiting
button_width = 10
send_button = tk.Button(
    input_frame, text="Send", font=("Arial", 12), bg="#3498db", fg="white", width=button_width, command=send_message)
send_button.grid(row=0, column=1, padx=5, pady=5)

reset_button = tk.Button(
    input_frame, text="Reset", font=("Arial", 12), bg="#f1c40f", fg="black", width=button_width, command=reset_chat)
reset_button.grid(row=0, column=2, padx=5, pady=5)

exit_button = tk.Button(
    input_frame, text="Exit", font=("Arial", 12), bg="#e74c3c", fg="white", width=button_width, command=exit_app)
exit_button.grid(row=0, column=3, padx=5, pady=5)

# Bind the Enter key to send messages
app.bind("<Return>", lambda event: send_message())

# Start the main GUI loop
app.mainloop()
