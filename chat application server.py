#  chat application using socket programming in python
# Server Side
import socket
import threading

HOST = 'localhost'
PORT = 8888

def handle_client(client_socket, client_address):
    print(f'Connected: ', {client_address})

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == 'exit':
                print(f'Disconnected: {client_address}')
                break
            print(f'Received from {client_address}: {message} ')
            broadcast(message,client_socket)
        except ConnectionResetError:
            print(f'Disconnected: {client_address}')
            break
    client_socket.close()

def broadcast(message,sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            client_socket.sendall(message.encode())
        
def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST,PORT))
        server_socket.listen()
        print(f'Server Started and Listening on {HOST} : {PORT}')

        while True:
            client_socket,client_address = server_socket.accept()
            clients.append(client_socket)
            threading.Thread(target=handle_client,args=(client_socket,client_address)).start()

if __name__ == '__main__':
    clients = []
    start_server()
