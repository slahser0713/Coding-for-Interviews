import socket
def main():
    #  1.建立tcp套接字
    tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #  2.连接服务器
    tcp_socket.connect(("192.168.14.139",8080)) #  需要连接的服务器的ip，端口
    #  3.发送数据
    send_data = input("输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))
    # 关闭套接字
    tcp_socket.close()
if __name__ == '__main__':
    main()