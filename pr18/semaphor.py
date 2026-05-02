import random
import threading
import time

server_semaphore = threading.Semaphore(3)

def request_handler(user_id):
    print(f"Пользователь {user_id} ждет доступа")
    with server_semaphore:
        print(f"Пользователь {user_id} подключился к серверу")
        time.sleep(random.uniform(1, 3))
        print(f"Пользователь {user_id} отключился")

threads = [threading.Thread(target=request_handler, args=(i,)) for i in range(10)]
for t in threads: t.start()