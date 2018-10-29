import socket
import threading

ip = '0.0.0.0'
port = 4658

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(socket.SOMAXCONN)

clients = []

def printToAll(msg):
    for c in clients:
        c.send(msg)


def client(client_skt, addr):
    print("ao bobina")
    response = 'a'
    while response != 'bye':
        response = client_skt.recv(1024)
        response = response.decode('utf-8')
        print(response)
        printThread = threading.Thread(target=printToAll, args=(response.encode('utf-8')))
        printThread.start()
    print('{} has desconnected'.format(addr))
    client_skt.close()




while(True):
    client_skt, addr = server.accept()
    print("* New Client {} \n  ".format(addr[0]))
    clients.append(client_skt)
    thread = threading.Thread(target=client, args=(client_skt, addr[0]))
    thread.start()


