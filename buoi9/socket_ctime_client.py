import socket

# nguyen van quy - 211213804
# client.py

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234))
data = s.recv(1024).decode("utf-8")
print(f"received: {data}")

while True:
    cmd = input("Command: ")
    s.send(cmd.encode("utf-8"))
    data = s.recv(4096).decode("utf-8")
    if "get" not in cmd:
        print(data)
    else:
        with open(cmd.split()[1], "w") as f:
            f.write(data)
        print(f"Get file {cmd.split()[1]} thanh cong")