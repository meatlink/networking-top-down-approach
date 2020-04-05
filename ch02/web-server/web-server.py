from socket import socket, AF_INET, SOCK_STREAM

from request_processor import RequestProcessor
from http_wrapper import HTTPRequest
from simple_file_reader import SimpleFileReader


host = "localhost"
port = 12000


request_processor = RequestProcessor(
    file_reader=SimpleFileReader("./")
)


def main():
    s = socket(AF_INET, SOCK_STREAM)

    s.bind(("", port))
    s.listen(1)

    print("The server is ready to receive")

    while True:
        conn, addr = s.accept()
        msg = conn.recv(2048).decode()
        try:
            conn.send(process_message(msg).encode())
            print("Request processed")
        except:
            print("Can't process the request")
        conn.close()


def process_message(msg):
    response = request_processor.process(HTTPRequest(msg))
    return response.to_text()


main()
