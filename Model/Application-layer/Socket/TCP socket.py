- client đọc kí tự từ bàn phím gửi cho server
- server nhận các kí tự, cuyển thành upper case
- server gửi lại dữ liệu cập nhật
- client nhận dữ liệu và in ra


# TCP client
from socket import *
serverName = 'servername'
serverPort = 12000

# create TCP socket 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# get input
message = input("Input lowercase sentence: ")

# send message
clientSocket.send(message.encode())

# read message have been modified sent by server at socket
modifiedMessage = clientSocket.recv(1024)

print("From Server: ", modifiedMessage.decode())

# close socket
clientSocket.close()


# TCP server
from socket import *
serverPort = 12000

# create TCP socket 
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", serverPort))

# listen for incoming TCP requests
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # server waits on accept() for incoming requests, new socket client on return
    connectionSocket, addr = serverSocket.accept()
    
    message = connectionSocket.recv(1024).decode()
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()

