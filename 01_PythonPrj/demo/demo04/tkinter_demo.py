# https://www.runoob.com/python/python-gui-tkinter.html
import tkinter as tk
import random

root = tk.Tk()
root.title("随机点名系统")
root.geometry("250x150")

is_running = False
students = []
with open("resource/students_name.txt", 'r', encoding="utf-8") as f:
    for name in f.readlines():
        students.append(name.rstrip('\n'))


def on_click():
    global is_running
    if not is_running:
        is_running = True
        button.config(text="停止")
        roll_call()
    else:
        is_running = False
        button.config(text="开始")


def roll_call():
    if is_running:
        student_name = random.choice(students)
        label.config(text=student_name)
        root.after(50, roll_call)

label = tk.Label(root, text="", font=("Arial", 24))
label.pack(pady=20)

button = tk.Button(root, text="开始", command=on_click, font=("Arial", 18))
button.pack(pady=10)

root.mainloop()

