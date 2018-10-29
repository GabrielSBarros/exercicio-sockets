import socket
import threading

HOST, PORT = input().split(":")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, int(PORT)))

while True:
    msg = input()
    client.send(bytes(msg, 'utf-8'))
    if (msg == 'bye'):
        break;
    print(client.recv(1024).decode('utf-8'))

client.close()
