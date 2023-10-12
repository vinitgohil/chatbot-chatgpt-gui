import openai
from config import api_key

class Chatbot:
	def __init__(self):
		openai.api_key = api_key

	def get_response(self, user_input):
		response = openai.Completion.create(
			engine="gpt-3.5-turbo-instruct",
			prompt=user_input,
			max_tokens=3000,
			temperature=0.5
		).choices[0].text
		return response

if __name__ == "__main__":
	chatbot = Chatbot()
	response = chatbot.get_response("Tell me a story about a Swiss and his food atrocities.")
	print(response)
