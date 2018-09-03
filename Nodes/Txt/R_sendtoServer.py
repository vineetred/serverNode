#NODE. THIS GETS THE FILE NAME FROM THE SERVER AND SENDS THE FILE BACK
import socket

s = socket.socket()
host = socket.gethostname()
port = 7013
s.bind((host,port))
s.listen(5)
print("<<-NODE IS UP->>")

while True:
    connection, address = s.accept() #Accepts the connection from the server

    print("Node is connected to:",address)
    nameFile = connection.recv(1024) #Gets the file name from the client-->Server-->Node
    print nameFile

    file = open(nameFile, 'rb') #Opens the file
    reading = file.read(1024) #First 1024 bytes
    print("Sending %s to server",nameFile)
    while(reading):
        connection.send(reading) #sends them to the node --> Server -->Client
        reading = file.read(1024)
    file.close()
    print("File has been sent to the server")
    connection.close()

s.close()