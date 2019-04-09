import socket
import sys


#create a socket
def create_socket():

	try:
		global host
		global port
		global s

		host = ''
		port= 5555
		s = socket.socket()

	except socket.error as err:
		print("socket creation error: " + str(err))