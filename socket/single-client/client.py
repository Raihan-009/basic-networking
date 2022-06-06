from http import client
import socket

s = socket.socket()
s.connect((socket.gethostname(), 55551))


server_msg = s.recv(1024)
print(f'Message from Server :: {server_msg.decode("utf-8")}')
 
conn = True
while conn:
    client_msg = input()
    if client_msg == "terminate":
        s.send(client_msg.encode("utf-8"))
        conn = False
        s.close()
    else:
        s.send(client_msg.encode("utf-8"))