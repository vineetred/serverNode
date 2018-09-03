import socket
import time
import os

s = socket.socket()          # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 7008                  # Reserve a port for your service.

s.bind((host, port))

s.listen(5)

print ("Server is up")

while True:

	connection, address = s.accept()
	print address
	message=connection.recv(7)
	if message=='Send':
		fileName = ''
		while True:
			data = connection.recv(1)
			if data == '\n':
				break
			fileName += data

		new_file = fileName + '.tmp'  # get name of file

		with open(new_file, 'wb') as f:

			print 'file opened'
			while True:
				data = connection.recv(1024)
				# print('File Name: ', (data))
				if not data:
					break
				# write data to a file
				f.write(data)

		print('Successfully get the file')
		os.rename(new_file,fileName)
s.close()
print('connection closed')
