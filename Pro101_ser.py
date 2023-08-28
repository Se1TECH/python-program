# Basic Socket Programming
#serverside

import socket
HOST = 'localhost'
PORT = 8080

def handle_client(client_socket):
    file_name = client_socket.recv(1024).decode()
    try:
        with open(file_name,'rb') as file:
            data = file.read()
            client_socket.sendall(data)
    except FileNotFoundError:
        client_socket.sendall(b'File Not Found')

def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST,PORT))
        server_socket.listen(1)
        print("Server Started and listening on ", (HOST,PORT))


        while True:
            client_socket,client_address = server_socket.accept()
            print('Connected by ', client_address)
            handle_client(client_socket)
            client_socket.close()

if __name__ == "__main__":
    start_server()