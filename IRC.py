#Made by salty on github
#@https://github.com/JustFast

##Lib##

import socket, os, sys

##Lib##

class connection:

	def __init__(self, oauth, username):

		##SET UP THE SOCKET##
		self.server = 'irc.chat.twitch.tv'
		self.port = 6667
		self.user = username
		self.token = oauth
		self.sock = socket.socket()
		##SET UP THE SOCKET##

		##INIT VARIABLES##

		self.inturupt = False
		self.Itype = "default"
		self.msg = "no message selected!"
		self.stream = "#none"
		self.fname = None
		self.writeToFile = True

		##INIT VARIABLES##

		##CONNECT TO THE TWITCH SERVER##
		self.sock.connect((self.server, self.port))
		##CONNECT TO THE TWITCH SERVER##

		##SEND TO THE TWITCH SERVER WHAT WE ARE##

		self.sock.send(f"PASS {self.token}\n".encode("utf-8")) #SEND THE PASSWORD WITH UTF-8 ENCODING THE REASON THERE IS \n AT THE END IS BECAUSE TWITCH IRC NEEDS A \n
		self.sock.send(f"NICK {self.user}\n".encode("utf-8"))

		##SEND TO THE TWITCH SERVER WHAT WE ARE##

		print(self.sock.recv(2048).decode("utf-8")) #Send the recv

	def join(self, streamer):
		##NOTE##
		#STREAMER'S NAME MUST BE SAID WITH A HASHTAG AT THE START WITH NO CAPS!! EG. #minecraft
		##NOTE##
		self.stream = streamer
		self.sock.send(f"JOIN {streamer}\n".encode("utf-8"))

	def log(self, file=None):

		if file == None: #If there is no file than do nothing
			pass
		else: #If there is a file than create a file and write to it
			self.File = open(file, mode="a")
			self.fname = file

		self.pID = os.fork() #Make a fork

		if self.pID == 0: #Make the child process do this

			while True:

				responce = self.sock.recv(2048).decode("utf-8")

				##MAKE SURE THE CLIENTS CONNECTION STAYS##

				if responce.startswith("PING"): 
					self.writeToFile = False #Make sure the PING messages are not written into the file
					self.sock.send("PONG\n".encode("utf-8")) 

				##MAKE SURE THE CLIENTS CONNECTION STAYS##

				if file != None:
					if self.writeToFile:
						self.File.write(responce) #Log the chat
					else:
						self.writeToFile = True

				print(responce) #Print out the chat

		else: #If the parrent process just continue doing nothing
			pass

	def getLastMessage(self):

		if self.fname is None: #Make sure that the user has to be logging a file
			print("Invalid logging file! Please log a file!!!")
			quit()

		else:
			loggingfile = open(self.fname, mode="r").readline() #Read the lines of the file
			lastMessage = loggingfile.readline(len(loggingfile)) #Get the last message
			return lastMessage #Return the last message



	def sendMSG(self, message):
		self.sock.send(f"PRIVMSG {self.stream} :{message}\n".encode("utf-8")) #Send the message