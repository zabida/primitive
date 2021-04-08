# coding:utf-8
# from socket import *
import logging
import socket
import traceback


def do_connect(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((address, port))
        return sock
    except:
        logging.error(traceback.print_exc())
        return None


def main():
    # 1.创建tcp_client_socket 套接字对象
    # 作为客户端，主动连接服务器较多，一般不需要绑定端口

    # 2.连接服务器
    tcp_client_socket = do_connect("127.0.0.1", 8080)
    while True:
        try:
            """无限循环可以实现无限聊天"""
            # 3.向服务器发送数据
            msg = input("请输入要发送的消息：")
            tcp_client_socket.sendall(msg.encode())

            # 在linux中默认是utf-8编码
            # 在udp协议中使用的sendto() 因为udp发送的为数据报，包括ip port和数据，
            # 所以sendto()中需要传入address，而tcp为面向连接，再发送消息之前就已经连接上了目标主机

            # 4.接收服务器返回的消息
            recv_data = tcp_client_socket.recv(1024)  # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
            print(222, recv_data, 222)

            if recv_data:
                print("返回的消息为:", recv_data)
            else:
                print("对方已离线。。")
                break
        except:
            tcp_client_socket = do_connect("127.0.0.1", 8080)

    tcp_client_socket.close()


if __name__ == '__main__':
    main()
