import socket



if __name__=='__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = 'hello servers'
    sk.sendto(data.encode('utf-8'), ('127.0.0.1', 9050))
    data = sk.recvfrom(1024)
    print("server gui: {}".format(data))
    sk.close()