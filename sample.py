from socket import *
import re

is_login = True
UNAUTHORIZED = "401 Unauthorized"
OK = "200 OK\r\n"
FORMAT_GET = r'(GET/username=admin&passwd=c31b32364ce19ca8fcd150a417ecce58)'
ID = r'(id=\d\d)'
DATA_LIST = {'我在Android路上越走越远': '走到黑～',
             '推荐一个简单易用的组建化方案（支持多进程架构）': '组件化技术适用于需要多人协作的中大型项目，如果是一个人的项目且开发人员未实践过组件化方案则不建议采用。',
             'Native仍是王道，Flutter1.2难逆袭': '为什么？',
             '我获得两个奖项，送福利回馈': '我获得两个奖项，送福利回馈',
             '架构模式都没搞懂，拿什么去跳槽啊？': '已删除',
             'Android到底有多少种动画？准确告诉你！': 'Android动画可归纳为以下几种：视图动画、帧动画、属性动画、触摸反馈动画、揭露动画、转场（共享动画）、视图状态动画、矢量图动画、约束布局实现的关键帧动画。',
             'Flutter美团的实践及原理': 'Flutter的目标是使同一套代码同时运行在Android和iOS上。',
             '2019，你心累吗？': '2019，你心累吗？',
             '给大家说件好事': '福利中奖名单公布～有你吗？',
             'Java中的锁到底有几种，你知道吗？': '公平锁/非公平锁；可重入锁；独享锁/共享锁；互斥锁/读写锁；乐观锁/悲观锁；分段锁；偏段锁/轻量级锁/重量级锁；自旋锁。',
             '你必须要懂的APK瘦身知识': '得懂呀～',
             '第一条命令行～': 'sudo rm -rf ./*',
             '是时候下载Android9.0源码了': '是时候下载Android9.0源码了',
             '你知道什么是Android中的函数插桩吗？': '高深知识，别问，点进来看。',
             '或许你可以从这个角度去理解Handler': '带你再次理解Handler'}


def login():
    # TCP
    loginSocket = socket(AF_INET, SOCK_STREAM)
    loginSocket.bind(("", 6614))
    loginSocket.listen(2)
    while True:
        connectionSocket, addr = loginSocket.accept()
        message = connectionSocket.recv(1024).decode()
        if re.match(FORMAT_GET, message):
            send_OK_TCP(connectionSocket)
            send_data_TCP(connectionSocket)
        else:
            send_unauthorized_reply_TCP(connectionSocket)


def send_unauthorized_reply_TCP(socket):
    socket.send(UNAUTHORIZED.encode())


def send_data_TCP(socket):
    socket.sendall(str(DATA_LIST).encode())


def send_OK_TCP(socket):
    socket.send(OK.encode())


def main():
    login()


if __name__ == '__main__':
    main()
