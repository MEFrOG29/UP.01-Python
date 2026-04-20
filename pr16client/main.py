import socket

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

user_login = input("Введите ваш логин: ")
s.sendall(user_login.encode('utf-8'))

while True:
    text = input("Введите строку: ")
    if(text != "end"):
        s.sendall(f"{text}".encode('utf-8'))
        data = s.recv(1024)
    else:
        s.close()
        break
