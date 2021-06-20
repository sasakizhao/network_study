
from socket import *

def sendUdp(content):
   ##192.168.50.237
    serverName = '192.168.50.66'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = content
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()

if __name__ == '__main__':
    while True:
        content = input('Input lower message\n')
        print('content:', content)
        sendUdp(content)
