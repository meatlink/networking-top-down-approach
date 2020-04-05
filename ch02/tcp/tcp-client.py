from socket import socket, AF_INET, SOCK_STREAM

host = "localhost"
port = 12000

s = socket(AF_INET, SOCK_STREAM)

s.connect((host, port))

msg = input("Input lowercase sentence: ")

s.send(msg.encode())

modified_msg = s.recv(1024)

print(modified_msg.decode())

s.close()
