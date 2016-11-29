import socket
import sys
import time

host, port = "localhost", 3001

data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(bytes(data + "\n", "utf-8"))
while True
    received = str(sock.recv(1024), "utf-8")
 

 break
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
