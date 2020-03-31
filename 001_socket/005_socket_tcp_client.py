from socket import *


def main():
    # 1. create socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    # 2. connect server
    tcp_client_socket.connect(('192.168.0.115', 8080))

    # 3. do send and save
    send_data = input('data for sending: ')
    tcp_client_socket.send(send_data.encode('gbk'))

    recv_data = tcp_client_socket.recv(1024)
    print('data response: %s' % recv_data.decode('gbk'))

    # 4. close socket()
    tcp_client_socket.close()
    pass


if __name__ == '__main__':
    main()
