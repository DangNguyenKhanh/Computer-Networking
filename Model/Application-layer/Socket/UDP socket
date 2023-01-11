- client đọc kí tự từ bàn phím gửi cho server
- server nhận các kí tự, cuyển thành upper case
- server gửi lại dữ liệu cập nhật
- client nhận dữ liệu và in ra


# UDP client
from socket import *
serverName = 'hostname'
serverPort = 12000

# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get user input
message = input("Input lowercase sentence: ")

# send to server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# read characters from socket and modified to UPPERCASE
modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

# print out string 
print(modifiedMessage.decode())

# close socket
clientSocket.close()


# UDP server
from socket import *
serverPort = 12000

# create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# connect to port 12000
serverSocket.bind(serverPort)

print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

