import threading
import time

def print_numbers():
    for i in range(10):
        print(f"Число: {i}")
        time.sleep(2)

def print_letters():
    for char in "ABCDEFGHIJ":
        print(f"Буква: {char}")
        time.sleep(2)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start(); t2.start()