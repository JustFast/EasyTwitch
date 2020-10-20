# Made by JustFast on Github
# @https://github.com/JustFast
# IRC.py

# import required modules
import socket, os, sys


# define Connection class
class Connection:
	
	# constructor
	# @param oauth {string}
	# @param username {string}
	def __init__(self, oauth, username):

		# Set up the socket
		self.server = 'irc.chat.twitch.tv'
		self.port = 6667
		self.user = username
		self.token = oauth
		self.sock = socket.socket()

		# Define variables
		self.inturupt = False
		self.Itype = "default"
		self.msg = "no message selected!"
		self.stream = "#none"
		self.fname = None
		self.writeToFile = True

		# Connect to server
		self.sock.connect((self.server, self.port))

		# Notify the server about our pass and nick
		# Twitch IRC requires a newline
		self.sock.send(f"PASS {self.token}\n".encode("utf-8"))
		self.sock.send(f"NICK {self.user}\n".encode("utf-8"))

		# Log the response
		print(self.sock.recv(2048).decode("utf-8")) #Send the recv

	# Join a streamer
	# @param streamer {string}
	def join(self, streamer):
		# Hashtag must prepend the streamer's name. Streamer's name must also be all lowercase
		# Make sure the streamer's name is lowercase
		streamer = streamer.lower()
		self.stream = streamer
		self.sock.send(f"JOIN {streamer}\n".encode("utf-8"))

	# Log messages
	# @param file {string}
	def log(self, file=None):

		# Check if a file was passed
		if file == None:
			pass
		else:
			# Create/write to file if it was passed
			self.File = open(file, mode="a")
			self.fname = file

		# Create a fork
		self.pID = os.fork() 

		# Child process behavior
		if self.pID == 0:

			while True:
				response = self.sock.recv(2048).decode("utf-8")

				# Ping server to retain connection
				if response.startswith("PING"): 
					# Don't write pings to file
					self.writeToFile = False
					self.sock.send("PONG\n".encode("utf-8")) 

				if file != None:
					if self.writeToFile:
						self.File.write(response) # Log the chat
					else:
						self.writeToFile = True
				# Log the chat
				print(response)

		else:
			# Do nothing if parent process
			pass

	def getLastMessage(self):
		# Make sure user is logging to file
		if self.fname is None: 
			print("Invalid logging file! Please log a file!!!")
			quit()

		else:
			# Real lines of file, get the least message, and return it
			loggingfile = open(self.fname, mode="r").readline()
			lastMessage = loggingfile.readline(len(loggingfile))
			return lastMessage


	# Send a message
	# @param message {string}
	def sendMSG(self, message):
		self.sock.send(f"PRIVMSG {self.stream} :{message}\n".encode("utf-8")) #Send the message