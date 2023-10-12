## Chatbot Application GUI

This is a small chatbot that takes user input and returns a response based on the OPENAi's 
ChatGPT model - **gpt3.5-turbo-instruct**

The GUI has been designed using a simple interface using PyQT6 Library. 
- The main application window has the main ChatBot Window where you see the interaction between the user input 
and response from the OpenAi model
- The user input editor area where user enters any input it wants to send to the ChatGPT model.
- A send button. (An enter key on user's keyboard also sends the user input)

**Files**
- main.py: Runs the main application. Calls backend for responses from OpenAi.
- backend.py: Calls the openai model and receives the responses from OpenAi. 
