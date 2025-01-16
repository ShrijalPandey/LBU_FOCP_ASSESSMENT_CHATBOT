# LBU_FOCP_ASSESSMENT_CHATBOT

Project Overview:

This is a simple yet interactive chatbot application built using Python and the tkinter library. The chatbot acts as a virtual assistant, designed to answer various campus-related queries, such as library timings, Wi-Fi availability, and cafeteria hours. Additionally, it includes engaging features like jokes, motivational quotes, and personalized greetings.

The following is a simplified version of what your chatbot program does:

1. Chat Window - GUI
In the chatbot, a chat interface is created  using a library called Tkinter. It has the following:
   A chatbox to display the user's conversation with the chatbot.
   A place where the user can input their questions.
   Three buttons:
    Send: To send the question.
    Reset: To clear the chat and start fresh.
    Exit: Quits the program.
   This makes it very easy and fun for the user to converse with the bot.

2. Random Fun
   To make the chatbot more realistic, it selects at random one of such names -like Stefen or Micra- when it is launched.
   If it does not understand a question, it responds randomly with "Can you rephrase that?" or any other pre defined response.
   This keeps the conversation interesting.

3. Understanding Questions
   The chatbot searches for keywords within the user's questions, general words like "coffee" or "library" automatically evoke answers like opening times.
   If no keywords are found, it responds with something random, such as "I'm not sure about that.
   This helps it accord with meaningful responses most of the time.

4. Easter Eggs- Hidden Surprises
   I've added fun, hidden responses for certain questions:
   If somebody asks, "Who are you?" it introduces itself.
   It tells a joke if they ask for one.
   If they request a quote, it shares something inspirational.
   These surprises make the chatbot fun.

6. Save the Chat
   The program saves all the conversations in a text file. The name includes the current date and time. 
   This may be useful to keeping track of what users ask, reviewing and improving the chatbot later.

7. Smart Input Handling
   The chatbot is clever in the way it processes input:
   It prompts for the user's name at the beginning and then remembers it to make responses more personalized.
   It recognizes phrases such as "bye" or "exit" and knows when to exit the chat.
   It ignores empty messages, so it doesn’t reply unnecessarily.


8. Starting Over
   There is a reset button that cleans up the chat, allowing users to start fresh without having to close the program. 
   This is quite handy in testing or trying different conversations.

9. Error Handling
The chatbot:
   Gives random responses if it doesn't recognize a question.
   Handles empty inputs gracefully.
   Lets users end the conversation smoothly.
   This makes it more reliable, as well as user-friendly.

10. Personal Touch
   The chatbot personalizes the conversation by:
   Using the user's name in some responses.
   Providing helpful hints to guide the conversation in a certain direction.
   Added random disconnects to make the simulation of chat systems more real

10.How It's Built
 I’ve used:
   Tkinter: Shall be used in developing the Chat window. 
   Random: For choosing names and default responses.
   Datetime: This will be used to create unique filenames whenever the chat logs are saved. 
   Functions: Like send_message() for handling questions, reset_chat() for clearing the chat

