from http import client
import socket

# print(socket.gethostname())

s = socket.socket()
s.bind((socket.gethostname(), 1809))
s.listen(5)


while True:
    client_socket, address = s.accept()
    print(f'Connection from {address} has been established!')
    client_socket.send(bytes("Hola! I am from the server", "utf-8"))
    client_socket.close()