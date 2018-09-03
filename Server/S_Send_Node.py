import socket, os
import time

def sock1(file): #socket 1 for txt
	s1 = socket.socket()             # Create a socket object
	host = socket.gethostname()     # Get local machine name
	port = 7002     # Reserve a port for your service.
	print host
	print ("WE are in")
			# global file
	s1.connect((host, port)) # connection, address = s.accept()
	
	s1.send('Send')
	time.sleep(1)
	s1.send(file + '\n')

	print file
			# fileName = 'image.png'
	with open(file, 'rb') as f:
		reading = f.read(1024)
		while(reading):
			s1.send(reading)
			print("Sending",file)
			reading = f.read(1024)
	os.remove(file)
	print('Successfully sent the file')
	s1.close()
	print('connection closed')

def sock2(file):	#socket 2 for pdf
	s1 = socket.socket()             # Create a socket object
	host = socket.gethostname()     # Get local machine name
	port = 7010     # Reserve a port for your service.

	print ("WE are in")
			# global file
	s1.connect((host, port)) # connection, address = s.accept()
	
	s1.send('Send')
	time.sleep(1)
	s1.send(file + '\n')

	print file
			# fileName = 'image.png'
	with open(file, 'rb') as f:
		reading = f.read(1024)
		while(reading):
			s1.send(reading)
			print("Sending",file)
			reading = f.read(1024)
	os.remove(file)
	print('Successfully sent the file')
	s1.close()
	print('connection closed')

def sock3(file):	#socket 3 for mp3
	s1 = socket.socket()             # Create a socket object
	host = socket.gethostname()     # Get local machine name
	port = 7006     # Reserve a port for your service.

	print ("WE are in")
			# global file
	s1.connect((host, port)) # connection, address = s.accept()
	
	s1.send('Send')

	s1.send(file + '\n')

	print file
			# fileName = 'image.png'
	with open(file, 'rb') as f:
		reading = f.read(1024)
		while(reading):
			s1.send(reading)
			print("Sending",file)
			reading = f.read(1024)
	os.remove(file)
	print('Successfully get the file')
	s1.close()
	print('connection closed')

def sock4(file):	#socket 4 for rest of the files
	s1 = socket.socket()             # Create a socket object
	host = socket.gethostname()     # Get local machine name
	port = 7008     # Reserve a port for your service.

	print ("WE are in")
			# global file
	s1.connect((host, port)) # connection, address = s.accept()
	
	s1.send('Send')
	time.sleep(1)
	s1.send(file + '\n')

	print file
			# fileName = 'image.png'
	with open(file, 'rb') as f:
		reading = f.read(1024)
		while(reading):
			s1.send(reading)
			print("Sending",file)
			reading = f.read(1024)
	os.remove(file)
	print('Successfully sent the file')
	s1.close()
	print('connection closed')

s = socket.socket()          # Create a socket object
host = socket.gethostname()      # Get local machine name
port = 7000                  # Reserve a port for your service.
print host
s.bind((host, port))

s.listen(5)

print ("<--Server is up-->")

while True:
	connection, address = s.accept()
	print address

	fileName = ''
	while True:
		data = connection.recv(1)
		if data == '\n':
			break
		fileName += data

	print fileName

	with open(fileName, 'wb') as f:

		print 'file opened'
		while True:
			data = connection.recv(1024)
			# print('File Name: ', (data))
			if not data:
				print "Data recieved"
				break
			# write data to a file
			f.write(data)

	if fileName != "input.txt":
		print fileName

		# if fileName[-1:]=="r":
		# 	rname=fileName[:-1]
		# 	GetFile(rname)
		
		if fileName[-3:]=="txt":
			# s.close()
			sock1(fileName)
		elif fileName[-3:]=="pdf":
			# s.close()
			sock2(fileName)
		elif fileName[-3:]=="mp3":
			sock3(fileName)
		else:
			sock4(fileName)

		with open('log','a') as log:
			log.write(fileName)
			log.write('\n')

	print('Successfully get the file')

s.close()
print('connection closed')
