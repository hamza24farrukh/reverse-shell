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

#binding the socket and listening for connections

def bind_socket():

	try:
		global host
		global port
		global s

		print ("binding the Port: " + str(port))

		s.bind(host,port)
		s.listen(5) #number if connections it tolerates before throwing 

	except socket.error as err:
		print("socket binding error " + str(err) + "\n" + "Retrying...")
		bind_socket()

# establish connection with a client (socket must be listening)

def socket_accept():
	global host
	global port
	global s

	conn, address = s.accept()
	print("connection has been established! " + "IP " + address[0] + "| Port " + str(address[1]))
	send_command(conn)

	conn.close()

