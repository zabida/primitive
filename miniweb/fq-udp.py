# coding: utf-8
from socket import *


def create_udp_socket():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    return udp_socket


def udp_socket_recv(port):
    u_sock = create_udp_socket()
    local_addr = ('', port)
    u_sock.bind(local_addr)
    recv_data = u_sock.recvfrom(1024)
    print(recv_data)
    print(recv_data[0].decode('gbk'))
    u_sock.close()


def udp_socket_send(host, port):
    while True:
        u_sock = create_udp_socket()
        dest_addr = (host, port)
        send_data = input('请输入要发送的数据:')
        u_sock.sendto(send_data.decode('utf-8').encode('gbk'), dest_addr)
    u_sock.close()


if __name__ == '__main__':
    # udp_socket_send('192.168.124.35', 7788)
    udp_socket_recv(7788)