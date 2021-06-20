from socket import *

serverPort = 12000
#192.168.50.66
serverIp = '192.168.50.66'
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIp, serverPort))
print('udp server started\n')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('receive msg:', message.decode(), 'from:', clientAddress)
    modifiedMsg = message.decode().upper()
    serverSocket.sendto(modifiedMsg.encode(), clientAddress)
