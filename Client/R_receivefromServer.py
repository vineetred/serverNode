import socket
s = socket.socket()
# s.settimeout(5.0)             # Create a socket object
host = '10.1.17.89'    # Get local machine name
port = 7001    # Reserve a port for your service.
s.connect((host, port))

print("<<-Client is up->>")
task = raw_input("What do you wanna do?: ")
s.send(task)
if task != "R":
	data = s.recv(1024)
	with open('log_client', 'wb') as f:
		while data:
			f.write(data)
			data = s.recv(1024)
			# print('File Name: ', (data))
			if not data:
				
				break
			# write data to a file
	print "Log Delivered"
	
else:		
	nameFile = raw_input("Enter the name of the file you need: ")
	#Sending the name of the file to the server
	s.send(nameFile)

	data = s.recv(1024)
	if data != "Not found":
		with open(nameFile, 'wb') as f:
			while data:
				f.write(data)
				data = s.recv(1024)
				# print('File Name: ', (data))
				if not data:
					print "Data recieved"
					break
				# write data to a file
	print("File has been recieved from the server")
s.close()
