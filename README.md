# serverNode

Programming assignment 3 for the Operating Systems course at Ashoka University taught by Professor Anirban Mondol. Uses the Python Socket library as well as the Watchdog library (modified a lot!).

## Folder Structure --

My program is designed to run on three different 'systems' at once. However, it is possible to run them on the same machine but with different
terminal sessions.

- ### Client: This is the code that runs on the computer which syncs all the data. The watchdog client tells the server what files have been added or deleted.

- ### Server: This is where most of the work happens. The script listens for connections from the client, writes a synced file locally, decides the storage node (port number) a file must be sent to on the basis of its extension, sends the file to the appropriate storage node, updates the local file index on the server.

- ### Storage Nodes: The script is esentially storing all our data. Basically a remote data storage server.



