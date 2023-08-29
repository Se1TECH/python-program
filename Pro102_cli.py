#chat application using socket programming in python
# Client Side

import socket
import threading

HOST = 'localhost'
PORT = 8888

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except ConnectionResetError:
            print('Disconnected from the server')
            break

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    threading.Thread(target=receive_messages).start()

    while True:
        message = input()
        client_socket.sendall(message.encode())
        if message == 'exit':
            break

    client_socket.close()

if __name__ == '__main__':
    start_client()
