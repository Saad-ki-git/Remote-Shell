# Remote Shell
## This repository contains a simple implementation of a reverse shell for remote command execution between a server and multiple clients. The reverse shell allows a user to remotely control client machines through a command-line interface.
***You can convert to convert py to and exe => https://www.geeksforgeeks.org/convert-python-script-to-exe-file/***
### How this works
![Diagram of the reverse shell](https://github.com/Saad-ki-git/Remote-Shell/assets/93855880/aa7db193-29a5-4a25-8e5d-9e3989dd2f43)

**Server (server.py)**
 ***Overview***
 **The server-side script creates a reverse shell that facilitates remote control of multiple client machines. It utilizes threading to handle two main tasks simultaneously: listening for incoming connections and managing commands with connected clients.**

***How it Works***

**Create Socket:**
The script creates a socket for communication.

**Bind Socket:**
Binds the socket to a specified host IP and port.
Handles binding errors and retries until successful.

**Handle Connection:**
Manages incoming client connections.
Creates a separate thread for each connected client.
Keeps track of active connections and their addresses.

**Interactive Shell:**
Provides an interactive shell for the user to input commands.
Supports commands like "exit," "list" to display connected clients, and "select" to choose a client for sending commands.

**List Connections:**
Displays a list of all connected clients with their IDs, addresses, and ports.
Checks and removes inactive clients.

**Send Command:**
Sends user input commands to the selected client.
Receives and prints the output from the client.
Thread Management:

Creates threads for handling connection and command tasks.
Threads run concurrently, one for each task.
Initiates the threads and their respective tasks.


***Usage
Run server.py on the machine intended to control the remote clients.
Interact with the server using the provided commands.***

**Client (client.py)**

***Overview***
**The client-side script establishes a connection to the server and executes commands received from the server. It allows remote control of the client machine through a reverse shell.**

**Main Logic**
Creates a socket and connects to the server using a specified IP and port.
Enters a loop to continuously receive commands from the server and execute them.
Supports changing the current working directory using the "cd" command.
Uses a subprocess to execute commands and captures the output to send back to the server.

**Usage**
Run client.py on the machines intended to be controlled remotely.
The client will connect to the server, and the server can then send commands to be executed on the client.
