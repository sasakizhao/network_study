from socket import *

serverPort = 12000
#192.168.50.66
serverIp = '192.168.50.66'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))
serverSocket.listen(1)
print('tcp server started\n')
while True:
    connectSock, clientAddr = serverSocket.accept()
    message = connectSock.recv(1024).decode()
    print('receive msg:', message, 'from:', clientAddr)
    modifiedMsg = message.upper()
    connectSock.send(modifiedMsg.encode())
    connectSock.close()
