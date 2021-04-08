# coding: utf-8
import socket


def tcp_server():
    # socket.AF_INET (IPV4)
    # socket.SOCK_STREAM (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听 IP:port
    s.bind(('127.0.0.1', 8080))

    # 最大允许连接数量
    s.listen(3)

    # 死循环，重复的处理着每个客户端的请求
    while True:
        # 阻塞 每当有客户端的请求过来开始执行
        # 连接处理 （已完成三次握手）并获取资源对象 | conn 请求对象 | addr 客户端地址 ip: port
        conn, addr = s.accept()

        # 请求处理 | 读取客户端发送过来的数据 | recv(1024) 指定每次读取 1024 字节，当数据较长时可以通过 while 循环读取
        data = conn.recv(1024)
        print('recv: {}'.format(data))

        msg = input("请输入要发送的消息：")
        # 响应处理 | 把客服端发送过来的数据又转发回去
        conn.sendall(msg.encode())

        # 关闭客户端连接
        conn.close()


if __name__ == '__main__':
    tcp_server()
