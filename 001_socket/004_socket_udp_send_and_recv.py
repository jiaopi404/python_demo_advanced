# coding=utf-8

from socket import *

"""
使用mac工具: 网络调试助手(app store) 进行调试
"""

# 1. sendto(send_data.encode('utf-8'), ('192.168.1.1', 8080))
# 2. recvfrom(1024) 1024表示接收的最大字节

IP_ADDRESS = '192.168.0.115'
PORT = 8080


def create_socket():
    """
    create socket
    :return: socket instance
    """
    return socket(AF_INET, SOCK_DGRAM)


def do_send_and_recv(socket_instance):
    # recv address
    dest_addr = (IP_ADDRESS, PORT)
    send_data = input('请输入要发送的数据: ')
    # 发送数据到指定的电脑上的指定程序中
    socket_instance.sendto(send_data.encode('utf-8'), dest_addr)
    recv_msg = socket_instance.recv(1024)
    print_received_msg(recv_msg)
    pass


def close_socket(socket_instance):
    socket_instance.close()
    pass


def print_received_msg(msg):
    print(msg[0].decode('gbk'))  # data
    print(msg[1])  # ip, port


def main():
    udp_socket = create_socket()
    do_send_and_recv(udp_socket)
    close_socket(udp_socket)
    pass


if __name__ == '__main__':
    main()
