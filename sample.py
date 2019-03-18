from socket import *
import re
import random

is_login = False


def login():
    # TCP
    loginSocket = socket(AF_INET, SOCK_STREAM)
    loginSocket.bind(("", 6000))
    loginSocket.listen(2)
    while True:
        connectionSocket, addr = loginSocket.accept()
        message = connectionSocket.recv(1024)
        global is_login
        if re.match("GET/HTTP/1.1/username=&passwd=", message):
            print("yes")
            is_login = True
        else:
            send_unauthorized_reply_TCP(connectionSocket)


def getPicture():
    # UDP GET xxxxxx
    picSocket = socket(AF_INET, SOCK_DGRAM)
    picSocket.bind(("", 6001))
    while True:
        rand = random.randint(0, 10)
        number = 0
        message, addr = picSocket.recvfrom(1024)
        if is_login:
            if (rand < 4):
                continue
            picSocket.sendto(message, addr)
        else:
            send_unauthorized_reply_UDP(picSocket, addr)


def send_unauthorized_reply_UDP(socket, addr):
    socket.sendto("401 Unauthorized".encode(), addr)


def send_ok_reply_UDP(socket, addr):
    socket.sendto("200 OK".encode(), addr)


def send_unauthorized_reply_TCP(socket):
    socket.send("401 Unauthorized".encode())
