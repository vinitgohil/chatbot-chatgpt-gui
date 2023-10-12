from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading

class ChatbotWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.chatbot = Chatbot()

		self.setMinimumSize(800, 600)

		# Add the Char Area Widget
		self.chat_area = QTextEdit(self)
		self.chat_area.setGeometry(20, 20, 680, 460)
		self.chat_area.setReadOnly(True)

		# Add the input field widget
		self.input_field = QLineEdit(self)
		self.input_field.setGeometry(20, 480, 680, 40)
		self.input_field.returnPressed.connect(self.send_message)

		# Add the Send button widget
		self.button = QPushButton("Send", self)
		self.button.setGeometry(20, 520, 80, 30)
		self.button.clicked.connect(self.send_message)

		self.show()

	def send_message(self):
		user_input = self.input_field.text().strip()
		self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
		self.input_field.clear()

		thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
		thread.start()

	def get_bot_response(self, user_input):
		response = self.chatbot.get_response(user_input)
		self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'> ChatBot: {response}</p>")

app = QApplication(sys.argv)
main_window = ChatbotWindow()
main_window.show()
sys.exit(app.exec())