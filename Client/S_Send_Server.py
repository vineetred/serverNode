import time
import socket
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class LoggingEventHandler(FileSystemEventHandler):
	"""Logs all the events captured."""

	def sendFile(self, file):
		s = socket.socket()             # Create a socket object
		host = '10.1.17.89'     # Get local machine name
		port = 7000     # Reserve a port for your service.

		print ("We are in")
				# global file
		s.connect(('10.1.17.89', port))
		# connection, address = s.accept()
		
		filen=file+"\n"
		s.send(filen)
		if file != 'input.txt':
			print file
					# fileName = 'image.png'
			with open(file, 'rb') as f:
				reading = f.read()
				while(reading):
					s.send(reading)
					print("Sending",file)
					reading = f.read(1024)
			
			print 'Successfully sent the file'
		s.close()
		print 'connection closed'

	def on_modified(self, event):		
		if not event.is_directory:
			filename = os.path.split(event.src_path)[1]
			self.sendFile(filename)

	def on_created(self, event):
		if not event.is_directory:
			filename = os.path.split(event.src_path)[1]
			self.sendFile(filename)

	def on_moved(self, event):
		if not event.is_directory:
			filename = os.path.split(event.src_path)
			self.sendFile(filename)

event_handler = LoggingEventHandler()
observer = Observer()
observer.schedule(event_handler, '.', recursive=False)
observer.start()
try:
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	observer.stop()
observer.join()