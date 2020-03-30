import socket

"""
tcp socket
"""

# create socket 创建 tcp 套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.close()
