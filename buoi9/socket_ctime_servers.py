import socket
import os

# nguyen minh quan -211200891
# server.py

if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 1234))
    s.listen(5)  #lắng nghe nối từ client, và sẵn sàng 5 hàng doi
    client_sk,client_addr=s.accept()
    print(f"Client {client_addr} connected")

    data = "hello from server !"
    client_sk.send(data.encode("utf-8"))
    while True:
        cmd = client_sk.recv(1024).decode("utf-8")
        if cmd == "dir":
            list_dir = os.listdir()
            data = ""
            for file in list_dir:
                data += file+"\t"
            client_sk.send(data.encode("utf-8"))
        elif "get" in cmd:
            file = cmd.split()[1]
            if file in os.listdir():
                with open(file,"r") as f:
                    data = f.read()
                    client_sk.send(data.encode("utf-8"))
            else:
                client_sk.send("File ko ton tai".encode("utf-8"))
        else:
            client_sk.send("ERROR!".encode("utf-8"))
    client_sk.close()
    s.close()