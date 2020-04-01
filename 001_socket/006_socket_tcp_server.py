from socket import *


def main():
    # create socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    # local info
    address = ('', 8098)

    # bind
    tcp_server_socket.bind(address)

    print(tcp_server_socket)

    # 使用socket创建的套接字默认的属性是主动的, 使用 listen 将其
    # 变为被动的, 这样就可以接收别人的链接了
    tcp_server_socket.listen(128)

    # 如果有新的客户端来链接服务器, 那么就产生一个新的套接字专门为
    # 这个客户端服务
    # client_socket 用来为这个客户端服务
    # tcp_server_socket 就可以省下来专门等待其他新客户端的链接
    client_socket, client_addr = tcp_server_socket.accept()

    # 接收对方发送过来的数据
    recv_data = client_socket.recv(1024)
    print('接收的数据为: ', recv_data.decode('gbk'))

    # 发送一些数据到客户端
    client_socket.send('thank you !'.encode('gbk'))

    # 关闭为这个客户端服务的套接字, 只要关闭了,
    # 就意味着为不能再为这个客户端服务了,
    # 如果还需要服务, 只能再次重新连接
    client_socket.close()


if __name__ == '__main__':
    main()
