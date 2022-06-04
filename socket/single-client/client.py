import socket

s = socket.socket()
s.connect((socket.gethostname(), 1809))


server_msg = s.recv(1024)
print(f'Message from Server :: {server_msg.decode("utf-8")}')