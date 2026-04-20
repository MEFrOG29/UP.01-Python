import socket
import tkinter
from tkinter import Entry, Button


def send_massage():
    login = login_entry.get()
    message = message_entry.get()

    HOST = 'localhost'
    PORT = 50007

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(login.encode('utf-8'))
    import time
    time.sleep(0.1)
    s.sendall(message.encode('utf-8'))

    s.close()

    message_entry.delete(0, tkinter.END)
    print(f"Сообщение от {login} отправлено")



root = tkinter.Tk()
root.title("Мессанджер")
root.geometry('500x300')

tkinter.Label(text="Логин").pack(pady=5)
login_entry = Entry()
login_entry.pack()

tkinter.Label(text="Сообщение").pack(pady=5)
message_entry = Entry()
message_entry.pack()

button_send = Button(text="Отправить", command=send_massage)
button_send.pack(pady=20)

root.mainloop()