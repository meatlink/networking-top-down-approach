from socket import socket, AF_INET, SOCK_DGRAM

host = "localhost"
port = 12000

s = socket(AF_INET, SOCK_DGRAM)

msg = input("Input lowercase sentence: ")

s.sendto(msg.encode(), (host, port))

modified_msg, server_addr = s.recvfrom(2048)

print(modified_msg.decode())

s.close()
