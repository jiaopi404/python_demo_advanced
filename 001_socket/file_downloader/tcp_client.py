from socket import *


def main():
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)

    server_ip = input('server ip: ')
    server_port = int(input('server port: '))

    tcp_client_socket.connect((server_ip, server_port))

    file_name = input('please enter the file path')

    tcp_client_socket.send(file_name.encode('utf-8'))

    recv_data = tcp_client_socket.recv(1024)

    if recv_data:
        with open('[recv]' + file_name, 'wb') as f:
            f.write(recv_data)

    tcp_client_socket.close()
    pass


if __name__ == '__main__':
    main()
