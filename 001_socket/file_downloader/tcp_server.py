from socket import *
import sys


def get_file_content(file_name):
    # get file content
    try:
        with open(file_name, 'rb') as f:
            content = f.read()
        return content
    except IOError as e:
        print('没有下载的文件: %s, e is: %s' % (file_name, e))
    pass


def main():
    if len(sys.argv) != 2:
        print('please run as follow: python3 xxx.py 7890')
        return
    else:
        port = int(sys.argv[1])

    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    address = ('', port)

    tcp_server_socket.bind(address)
    tcp_server_socket.listen(128)

    while True:
        client_socket, clientAddr = tcp_server_socket.accept()

        recv_data = client_socket.recv(1024)
        file_name = recv_data.decode('utf-8')
        print('the file name of client request is: %s' % file_name)
        file_content = get_file_content(file_name)

        if file_content:
            client_socket.send(file_content)

        client_socket.close()
        pass

    tcp_server_socket.close()
    pass


if __name__ == '__main__':
    main()
