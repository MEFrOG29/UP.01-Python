import clr
import os

# Получаем полный путь к нашей DLL
dll_path = os.getcwd() + "\\libraryPR17.dll"

# Подключаем библиотеку
clr.AddReference(dll_path)

# Импортируем класс из пространства имен C#
from libraryPR17 import Class1

print("--- Тестирование C# модуля в Python ---")

file_name = "test_practice.txt"

# 1. Создание
res_create = Class1.CreateFile(file_name, "Привет из Python через C#!")
print(res_create)

# 2. Чтение
content = Class1.ReadFile(file_name)
print(f"Содержимое файла: {content}")

# 3. Изменение
res_append = Class1.AppendToFile(file_name, "Добавляем новую строку.")
print(res_append)

# Проверяем чтение после изменения
print(f"Обновленное содержимое: {Class1.ReadFile(file_name)}")

# 4. Удаление
if Class1.DeleteFile(file_name):
    print("Файл успешно удален.")
else:
    print("Не удалось удалить файл.")