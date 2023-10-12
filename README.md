# ChatbotGPT Application GUI

This is a small application that allows user to enter any input which interacts 
with the OpenAI ChatGPT model.

OpenAI model: **gpt-3.5-turbo-instruct** 

The application is built using the PyQT6 library.

**<u>Files</u>**

- ###**main.py**

  - This executed the main application window, 
  - Allows user to provide an input 
  - Calls the backend program that makes the call to OpenAI ChatGPT model for responses
  - Returns the response from OpenAi
- ###**backend.py**
  - contains the get response method that will create the input to send to ChatGPT
  - returns response from the model.

