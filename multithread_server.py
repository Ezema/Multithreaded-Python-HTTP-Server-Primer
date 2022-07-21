import socket
import threading

class HTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

    def start(self):
        self.socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"Connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024).decode()
        print(f"Request data:\n{request_data}")
        response = self.get_response(request_data)
        client_socket.sendall(response.encode())
        client_socket.close()

    def get_response(self, request_data):
        headers = ["HTTP/1.1 200 OK", "Content-Type: text/html"]
        body = "<html><body><h1>Hello, world!</h1></body></html>"
        headers.append(f"Content-Length: {len(body)}")
        response = "\r\n".join(headers) + "\r\n\r\n" + body
        return response

if __name__ == "__main__":
    server = HTTPServer("127.0.0.1", 8080)
    server.start()
