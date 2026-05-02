import psutil
import subprocess

def task_manager():
    print("1. Список процессов\n2. Запустить программу\n3. Завершить процесс\n0. Выход")
    while True:
        choice = input("\nВыберите действие: ")
        if choice == '1':
            for proc in psutil.process_iter(['pid', 'name']):
                print(f"PID: {proc.info['pid']} | Name: {proc.info['name']}")
        elif choice == '2':
            path = input("Введите путь к программе или имя")
            subprocess.Popen(path)
        elif choice == '3':
            pid = int(input("Введите PID для завершения: "))
            psutil.Process(pid).terminate()
        elif choice == '0':
            break

task_manager()