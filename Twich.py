#Made by salty on github
#@https://github.com/JustFast

##Lib##

import socket

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
		self.inturupt = False
		self.Itype = "default"
		self.msg = "no message selected!"
		self.stream = "#none"

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

	def log(self):
		while True:

			print(self.sock.recv(2048).decode("utf-8"))

	def sendMSG(self, message):
		self.sock.send(f"PRIVMSG {self.stream} :{message}\n".encode("utf-8")) #Send the message