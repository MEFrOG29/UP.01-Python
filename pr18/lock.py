import threading

counter = 0
lock = threading.Lock()

def change_counter(thread_id, use_lock=True):
    global counter
    if use_lock:
        with lock:
            for _ in range(11):
                print(f"Поток {thread_id} меняет: {counter}")
                counter += 1
            counter = 0
    else:
        for _ in range(11):
            print(f"Поток {thread_id} (без lock) меняет: {counter}")
            counter += 1
        counter = 0


threads = [threading.Thread(target=change_counter, args=(i,)) for i in range(10)]
for t in threads: t.start()