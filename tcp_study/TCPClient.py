from socket import *

def sendTCP():
   ##192.168.50.237
    serverName = '192.168.50.66'
    serverPort = 12000

    while True:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        content = input('Input lower message\n')
        print('content:', content)
        clientSocket.send(content.encode())
        modifiedMessage = clientSocket.recv(1024)
        print('From Server:', modifiedMessage.decode())
        clientSocket.close()
        print('connect closed\n')

if __name__ == '__main__':
    sendTCP()