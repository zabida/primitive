# coding=utf-8
import socket
import time

udp_socket = None  # 保存udp套接字
feiq_version = 1  # 飞秋的版本
feiq_user_name = "dong-test"  # 用户名
feiq_host_name = "ubuntu-64-1604"  # 主机名字
broadcast_ip = "255.255.255.255"  # 广播ip
feiq_port = 2425  # 飞鸽传书的端口

# 飞秋command
IPMSG_BR_ENTRY = 0x00000001
IPMSG_BR_EXIT = 0x00000002
IPMSG_SENDMSG = 0x00000020  # 表示 发送消息


def create_udp_socket():
    """创建udp套接字"""
    global udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 设置允许广播
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def send_broadcast_online_msg():
    """发送上线提醒"""
    # online_msg = "1:123456789:itcast-python:localhost:1:飞飞"
    online_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()),
                                        feiq_user_name, feiq_host_name,
                                        IPMSG_BR_ENTRY, feiq_user_name)
    dest_addr = (broadcast_ip, feiq_port)
    udp_socket.sendto(online_msg.encode("gbk"), dest_addr)


def send_broadcast_offline_msg():
    """发送下线提醒"""
    # online_msg = "1:123456789:itcast-python:localhost:2:飞飞"
    online_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()),
                                        feiq_user_name, feiq_host_name,
                                        IPMSG_BR_EXIT, feiq_user_name)
    dest_addr = (broadcast_ip, feiq_port)
    udp_socket.sendto(online_msg.encode("gbk"), dest_addr)


def send_msg_2_ip():
    """向指定的ip发送飞秋数据"""
    dest_ip = input("请输入对方的ip:")
    send_data = input("请输入要发送的数据内容:")
    if dest_ip and send_data:
        chat_msg = "%d:%d:%s:%s:%d:%s" % (feiq_version, int(time.time()), feiq_user_name, feiq_host_name,
                                          IPMSG_SENDMSG, send_data)
        udp_socket.sendto(chat_msg.encode("gbk"), (dest_ip, feiq_port))


def recv_msg_1_time():
    """接收1次消息"""
    recv_data, dest_addr = udp_socket.recvfrom(1024)
    print("%s>>>%s" % (dest_addr, recv_data))


def print_menu():
    """显示飞鸽传书的功能"""
    print("     飞鸽传书v1.0")
    print("1:上线广播")
    print("2:下线广播")
    print("3:向指定ip发送消息")
    print("4:接收1次消息")
    print("0:退出")


def main():
    # 创建套接字
    create_udp_socket()

    while True:

        print_menu()
        command_num = input("请输入要进行的操作:")
        if command_num == "1":
            # 发送上线提醒
            send_broadcast_online_msg()
        elif command_num == "2":
            # 发送下线提醒
            send_broadcast_offline_msg()
        elif command_num == "3":
            # 向指定ip发送消息
            send_msg_2_ip()
        elif command_num == "4":
            # 接收1次消息
            recv_msg_1_time()
        elif command_num == "0":
            send_broadcast_offline_msg()
            # 关闭套接字
            udp_socket.close()
            exit()


if __name__ == "__main__":
    main()
