import threading
import time

message_ready = threading.Event()

def sender():
    print("Отправитель: подготавливаю данные...")
    time.sleep(3)
    print("Отправитель: данные готовы!")
    message_ready.set()

def receiver():
    print("Получатель: жду сигнал...")
    message_ready.wait()
    print("Получатель: сигнал получен, начинаю обработку.")

threading.Thread(target=sender).start()
threading.Thread(target=receiver).start()