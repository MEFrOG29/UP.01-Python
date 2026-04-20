from tkinter import *
from tkinter import ttk
from tkinter import filedialog


root = Tk()
root.title("PR15")
root.geometry("500x450+700+300")

#task1
# text_field = Text()
# text_field.pack()
# def save_file(event=None):
#     filepath = filedialog.asksaveasfilename()
#     if(filepath != ""):
#         text = text_field.get("1.0", END)
#         with open(filepath, "w") as file:
#             file.write(text)
#
# def close_app(event=None):
#     root.destroy()
#
# save_button = ttk.Button(text="Сохранить файл", command=save_file)
# save_button.pack()
# root.bind('<Control-s>', save_file)
# root.bind('<Escape>', close_app)


#task2
# def left_click(event):
#     widget_index = entries.index(event.widget) + 1
#     label_info.config(text=f"Поле ввода: {widget_index}")
#
# def right_click(event):
#     widget_index = entries.index(event.widget) + 1
#     print(f"Поле ввода: {widget_index}")
#
#
# label_info = ttk.Label(root, text="fsfs")
# label_info.pack()
#
# entries = []
#
# for i in range(1, 4):
#     entry = Entry(root, name=f"text №{i}")
#     entry.pack(pady = 5)
#     entries.append(entry)
#
# root.bind_class("Entry", "<Button-1>", left_click)
# root.bind_class("Entry", "<Button-3>", right_click)


#task3
# mouse_cord = Label(text="Координаты мыши: x=0 y=0")
# mouse_cord.pack()
#
# def motion(event):
#     mouse_cord.config(text=f"Координаты мыши: x={event.x} y={event.y}")
#
# root.bind('<Motion>', motion)

#task4
# keys = Label(text="Нажатые клавиши: ")
# keys.pack()
#
# def key_pressed(event):
#     keys.config(text=f"Нажатые клавиши:{event.char}")
#
# root.bind('<Key>', key_pressed)

root.mainloop()
