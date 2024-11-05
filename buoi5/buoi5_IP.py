import socket_1

def get_host_name_ip():
    try:
        hostname = 'www.utc.edu.vn'
        hostip = socket.gethostbyname(hostname)
        print("hostname", hostname)
        print("IP: ", hostip)
    except:
        print("Khong lay duoc ip")

get_host_name_ip()