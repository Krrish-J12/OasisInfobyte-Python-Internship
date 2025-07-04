import socket
import threading
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init()

#server configuration
host = '127.0.0.1'
port = 12345

# Ceate server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"{Fore.GREEN}Server is listening on port {port}...{Style.RESET_ALL}")

client = []
nicknames = []

# Broadcast function to send messages to all connected clients
def broadcast(message, _client):
    for client_socket in client:
        if client_socket != _client:
            try:
                client_socket.send(message)
            except:
                # Remove broken client
                index = client.index(client_socket)
                client.remove(client_socket)
                client_socket.close()
                nickname = nicknames.pop(index)

# Handle client connections
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message.decode('utf-8') == 'exit':
                index = client.index(client_socket)
                nickname = nicknames[index]
                print(f"{Fore.RED}{nickname}Client has left the chat.{Style.RESET_ALL}")
                broadcast(f"{nickname} has left the chat.".encode('utf-8'), client_socket)
                client.remove(client_socket)
                nicknames.remove(nickname)
                client_socket.close()
                break
            else:
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"{Fore.BLUE}[{now}] {message.decode('utf-8')}{Style.RESET_ALL}")
                broadcast(message, client_socket)
        except:
            break

# Accept client connections
def receive():
    while True:
        client_socket, address = server_socket.accept()
        print(f"{Fore.GREEN}Connected to {address}{Style.RESET_ALL}")
        
        # Ask for nickname
        client_socket.send("Enter your nickname: ".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        client.append(client_socket)
        
        print(f"{Fore.YELLOW}{nickname} has joined the chat.{Style.RESET_ALL}")
        broadcast(f"{nickname} has joined the chat.".encode('utf-8'), client_socket)
        client_socket.send("Connected to the server. Type 'exit' to leave.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()
        
# Function for server to send messages
def write():
    while True:
        message = input()
        broadcast(f"Server: {message}".encode('utf-8'), None)

# Start receive thread
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Start write thread (server can chat)
write_thread = threading.Thread(target=write)
write_thread.start()
