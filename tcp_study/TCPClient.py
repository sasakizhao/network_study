from socket import *

def sendTCP():
   ##192.168.50.237
    serverName = '192.168.50.66'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    while True:
        content = input('Input lower message\n')
        print('content:', content)
        clientSocket.send(content.encode())
        modifiedMessage = clientSocket.recv(1024)
        if content == '.exit':
            clientSocket.close()
            print('connect closed\n')
        print('From Server:', modifiedMessage.decode())

if __name__ == '__main__':
    sendTCP()