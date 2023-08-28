# Basic Socket Programming
# Client Side

import socket

HOST = 'localhost'
PORT = 8080


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        file_name = input('Enter the file name: ')
        client_socket.sendall(file_name.encode())

        data = client_socket.recv(1024)
        if data == b'File not found':
            print('File not found on the server')
        else:
            with open(file_name, 'wb') as file:
                file.write(data)
                print('File downloaded successfully')


if __name__ == '__main__':
    start_client()
