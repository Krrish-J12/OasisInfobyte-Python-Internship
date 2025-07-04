import socket
import threading
from colorama import init, Fore, Style

# Initialize colorama
init()

# Server configuration
host = '127.0.0.1'
port = 12345

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# Ask for nickname
nickname = input("Enter your nickname: ") or "Client"

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print(f"\n{Fore.RED}Error receiving message. Connection may have been closed.{Style.RESET_ALL}")
            client_socket.close()
            break

# Function to send messages to the server
def write():
    while True:
        message = input()            
        client_socket.send(message.encode('utf-8')) # send actual message
        if message.lower() == 'exit':
            client_socket.close()
            break

# Run threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
