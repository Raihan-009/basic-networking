from http import client
import socket

# print(socket.gethostname())

s = socket.socket()
s.bind((socket.gethostname(), 1809))
s.listen(5)

client_socket, address = s.accept()
print(f'Connection from {address} has been established!')
client_socket.send(bytes("Hola! I am from the server", "utf-8"))

conn = True

while conn:
    client_msg = client_socket.recv(1024)
    client_msg = client_msg.decode("utf-8")
    if (client_msg == "terminate"):
        conn = False
        print("Message from client :: Connection with client got disconnected")
        s.close()
    else:
        print(f"Message from client :: {client_msg}")