from socket import *
import re
import random

is_login = True
UNAUTHORIZED = "401 Unauthorized"
OK = "200 OK"
KEY = "200 0K/key=c31b32364ce19ca8fcd150a417ecce58"
FORMAT_LOGIN = r'(POST/username=1b0679be72ad976ad5d491ad57a5eec0&passwd=2cea53149c42a690714f3f4a8a93647c)'
FORMAT_GET_PIC = r'(GET/key=c31b32364ce19ca8fcd150a417ecce58/pic/pic=\d*)'
ID = r'(id=\d\d)'


def login():
    # TCP
    loginSocket = socket(AF_INET, SOCK_STREAM)
    loginSocket.bind(("", 6614))
    loginSocket.listen(2)
    while True:
        connectionSocket, addr = loginSocket.accept()
        message = connectionSocket.recv(1024).decode()
        if re.match(FORMAT_LOGIN, message):
            send_key_TCP(connectionSocket)
            global is_login
            is_login = True
        else:
            send_unauthorized_reply_TCP(connectionSocket)


def getPicture():
    # UDP
    picSocket = socket(AF_INET, SOCK_DGRAM)
    picSocket.bind(("", 6615))
    while True:
        message, addr = picSocket.recvfrom(1024)
        print("here1")
        if re.match(FORMAT_GET_PIC, message.decode()):
            print("here2")
            id = re.search(ID, message.decode())
            print(id)
            send_ok_reply_UDP(picSocket, addr)
            rand = random.randint(0, 10)
            number = 0
            if (rand < 4):
                continue
            picSocket.sendto(message, addr)
            send_unauthorized_reply_UDP(picSocket, addr)
        else:
            send_unauthorized_reply_UDP(picSocket, addr)
            picSocket.close()
            return


def send_unauthorized_reply_UDP(socket, addr):
    socket.sendto(UNAUTHORIZED.encode(), addr)


def send_ok_reply_UDP(socket, addr):
    socket.sendto(OK.encode(), addr)


def send_unauthorized_reply_TCP(socket):
    socket.send(UNAUTHORIZED.encode())


def send_key_TCP(socket):
    socket.send(KEY.encode())


def main():
    if is_login:
        getPicture()
    else:
        login()


if __name__ == '__main__':
    main()
