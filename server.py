import sys
import socketserver
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        received_data = self.request.recv(2048)
        sys.stdout.flush()
        sys.stderr.flush()

        decodeDataIndex = received_data.find("\r\n\r\n".encode())
        decodedData = received_data[:decodeDataIndex].decode().split(" ")
        reqType = decodedData[1]

        if str(reqType) == "/Login":
            self.request.sendall("HTTP/1.1 200 OK\r\nContent-Length: 18\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello World! login".encode())
        elif str(reqType) == "/signUp":
            self.request.sendall("HTTP/1.1 200 OK\r\nContent-Length: 19\r\nContent-Type: text/plain; charset=utf-8\r\n\r\nHello World! signUp".encode())
        