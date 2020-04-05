from socket import socket, AF_INET, SOCK_DGRAM

host = "localhost"
port = 12000

s = socket(AF_INET, SOCK_DGRAM)

s.bind(("", port))

print("The server is ready to receive")

while True:
    msg, client_addr = s.recvfrom(2048)
    modified_msg = msg.decode().upper()
    s.sendto(modified_msg.encode(), client_addr)
