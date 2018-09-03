#THIS IS THE SERVER SEND! WE SEND THE FILE TO THE CLIENT FROM THE STORAGE NODE
import socket

s = socket.socket()
host = socket.gethostname()
port = 7001
s.bind((host,port))
s.listen(5)
print("<<-SERVER IS UP->>")
while True:
    connection, address = s.accept()

    print("Connected to: ", address)
    task = connection.recv(1024) #TO check what it needs to do?
    print "Task is: ", task
    if (task == "R"):
        nameFile = connection.recv(1024) #THE FILE NAME THAT WILL BE SEND TO THE NODE. THEN IT WILL RETRIEVE FROM NODE.
        print("File: ",nameFile)
        logFile = open('log','rb')
        logFileRead = logFile.read()
        if(nameFile in logFileRead):
            if(nameFile[-3:]=="txt"):
                nodePort = 7013
            elif(nameFile[-3:]=="pdf"):
                nodePort = 7015
            elif(nameFile[-3:]=="mp3"):
                nodePort = 7017
            else:
                nodePort = 7019
            recvClient = socket.socket()
            host = socket.gethostname()
            # nodePort = 7004 #NODE PORT
            recvClient.connect((host,nodePort)) # WE CONNECT TO THE NODE
            
            recvClient.send(nameFile) #Sending the filename to the node
            
            file = open(nameFile, 'wb')

            #FILE RECIEVE FROM NODE!
            data = recvClient.recv(1024)
            while (data):
                if not data:
                    break
                print "IN"
                file.write(data)
                data = recvClient.recv(1024)
            file.close()
            recvClient.close()

            #Begin the code that sends above file to client
            file = open(nameFile, 'rb')
            reading = file.read(1024)
            print("Sending the file to the client!", nameFile)
            while(reading):
                connection.send(reading)
                reading = file.read(1024)
            file.close()
            print("File has been sent to the client")
            connection.close()

        else:
            print ("File does not exist.")
            connection.send("Not found")
            connection.close()
    else:
        file = open('log', 'rb')
        reading = file.read(1024)
        print("Sending the LOG to the client!")
        while(reading):
            connection.send(reading)
            reading = file.read(1024)
        file.close()
        print("LOG has been sent to the client")
        connection.close()   
s.close()