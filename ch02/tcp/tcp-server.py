from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR

host = "localhost"
port = 12000

s = socket(AF_INET, SOCK_STREAM)

s.bind(("", port))
s.listen(1)

print("The server is ready to receive")

while True:
    conn, addr = s.accept()
    msg = conn.recv(2048).decode()
    modified_msg = msg.upper()
    conn.send(modified_msg.encode())
    conn.close()
