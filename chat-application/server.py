from http import client
import socket
import select

host = socket.gethostname()
# print(host)
port = 6969
REQUEST_QUEUE_SIZE = 5

s = socket.socket()
s.bind((host,port))
s.listen(REQUEST_QUEUE_SIZE)

socket_list = [s]


clients = {}


def recv_response(clients_socket):
    try:
        response = clients_socket.recv(1024)

        if not len(response):
            return False 
        
    except:
        return False