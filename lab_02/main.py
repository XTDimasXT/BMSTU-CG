import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math
import copy

arr = []
arr_connects = []
prev_arr = []
anchor = [150, 200]
anchor_default = [150, 200]
prev_anchor = [150, 200]
prev_dx = prev_dy = 0
prev_scale_x = prev_scale_y = 1
last_action = -1
angle = 0


def array_preparation(file_dots, file_connects):
    global arr, arr_connects

    arr = file_dots.readlines()
    for i in range(len(arr)):
        arr[i] = arr[i].replace("\n", "")
        temp = arr[i].split(" ")
        arr[i] = [int(temp[0]), int(temp[1])]
    
    arr_connects = file_connects.readlines()
    for i in range(len(arr_connects)):
        arr_connects[i] = arr_connects[i].replace("\n", "")
        temp = arr_connects[i].split(" ")
        arr_connects[i] = [int(temp[0]), int(temp[1])]


def create_drawing(arr, arr_connects, anchor):
    canvas.delete("all")
    create_dots(arr)
    create_lines(arr, arr_connects)
    canvas.create_oval(anchor[0] - 3, anchor[1] - 3, anchor[0] + 3, anchor[1] + 3, fill="#000fff000")


def create_dots(arr):
    for i in range(len(arr)):
        x, y = arr[i][0], arr[i][1]
        x1, y1, x2, y2 = (x - 2), (y - 2), (x + 2), (y + 2)
        #canvas.create_oval(x1, y1, x2, y2, fill="#000fff000")


def create_block(arr, ind_prev, range1, range2):
    prev = arr[ind_prev]
    for i in range(range1, range2):
        cur = arr[i]
        canvas.create_line(prev[0], prev[1], cur[0], cur[1])
        prev = cur


def create_lines(arr, arr_connects):
    for i in range(len(arr_connects)):
        first, second = arr_connects[i][0], arr_connects[i][1]
        canvas.create_line(arr[first][0], arr[first][1], arr[second][0], arr[second][1])


def create_line(arr, ind1, ind2):
    canvas.create_line(arr[ind1][0], arr[ind1][1], arr[ind2][0], arr[ind2][1])


def create_triangle(arr, ind1, ind2, ind3):
    canvas.create_line(arr[ind1][0], arr[ind1][1], arr[ind2][0], arr[ind2][1])
    canvas.create_line(arr[ind2][0], arr[ind2][1], arr[ind3][0], arr[ind3][1])


def perform_actions(action):
    global arr, arr_default, arr_connects, anchor, angle, anchor_default, last_action, prev_dx, prev_dy, prev_scale_x, prev_scale_y, prev_anchor

    if action == 0:
        create_drawing(arr_default, arr_connects, anchor_default)
        prev_arr = copy.deepcopy(arr)
        prev_anchor = copy.deepcopy(anchor)
        arr = copy.deepcopy(arr_default)
        anchor = copy.deepcopy(anchor_default)

        last_action = 0
    
    elif action == 1:
        dx = entry_dx.get()
        dy = entry_dy.get()

        try:
            dx = int(dx)
            dy = int(dy)
            
            for i in range(len(arr)):
                arr[i][0] += dx
                arr[i][1] += dy
            
            prev_dx = dx
            prev_dy = dy
        
            create_drawing(arr, arr_connects, anchor)
        except:
            tkmb.showerror("Ошибка", "Координаты могут задаваться только целыми числами")
            entry_dx.delete(0, tk.END)
            entry_dy.delete(0, tk.END)
        
        last_action = 1
    
    elif action == 2:
        anchor_x = entry_anchor_x.get()
        anchor_y = entry_anchor_y.get()
        prev_anchor = anchor

        try:
            anchor_x = int(anchor_x)
            anchor_y = int(anchor_y)
            anchor = [anchor_x, anchor_y]
            create_drawing(arr, arr_connects, anchor)
        except:
            tkmb.showerror("Ошибка", "Координаты могут задаваться только целыми числами")
            entry_anchor_x.delete(0, tk.END)
            entry_anchor_y.delete(0, tk.END)
        
        last_action = 2
    
    elif action == 3:
        angle = entry_angle.get()

        try:
            angle = float(angle)
            angle *= math.pi / 180

            for i in range(len(arr)):
                tmp_x = (arr[i][0] - anchor[0]) * math.cos(angle) - (arr[i][1] - anchor[1]) * math.sin(angle) + anchor[0]
                tmp_y = (arr[i][0] - anchor[0]) * math.sin(angle) + (arr[i][1] - anchor[1]) * math.cos(angle) + anchor[1]
                arr[i] = [tmp_x, tmp_y]
            
            create_drawing(arr, arr_connects, anchor)
        except:
            tkmb.showerror("Ошибка", "Угол может задаваться только действительным числом")
            entry_angle.delete(0, tk.END)
        
        last_action = 3
        
    elif action == 4:
        scale_x = entry_scale_x.get()
        scale_y = entry_scale_y.get()

        try:
            scale_x = float(scale_x)
            scale_y = float(scale_y)

            for i in range(len(arr)):
                tmp_x = scale_x * (arr[i][0] - anchor[0]) + anchor[0]
                tmp_y = scale_y * (arr[i][1] - anchor[1]) + anchor[1]
                arr[i] = [tmp_x, tmp_y]
            
            prev_scale_x = 1 / scale_x
            prev_scale_y = 1 / scale_y
            
            create_drawing(arr, arr_connects, anchor)
        except:
            tkmb.showerror("Ошибка", "Масштабирование может задаваться только действительным числом (кроме 0)")
            entry_scale_x.delete(0, tk.END)
            entry_scale_y.delete(0, tk.END)
        
        last_action = 4
    
    elif action == 5:
        
        if last_action == 0:
            arr = copy.deepcopy(prev_arr)
            anchor = copy.deepcopy(prev_anchor)
        
        elif last_action == 1:
            for i in range(len(arr)):
                arr[i][0] -= prev_dx
                arr[i][1] -= prev_dy
        
        elif last_action == 2:
            anchor = prev_anchor
        
        elif last_action == 3:
            angle = 2 * math.pi - angle

            for i in range(len(arr)):
                tmp_x = (arr[i][0] - anchor[0]) * math.cos(angle) - (arr[i][1] - anchor[1]) * math.sin(angle) + anchor[0]
                tmp_y = (arr[i][0] - anchor[0]) * math.sin(angle) + (arr[i][1] - anchor[1]) * math.cos(angle) + anchor[1]
                arr[i] = [tmp_x, tmp_y]
        
        elif last_action == 4:
            for i in range(len(arr)):
                tmp_x = prev_scale_x * (arr[i][0] - anchor[0]) + anchor[0]
                tmp_y = prev_scale_y * (arr[i][1] - anchor[1]) + anchor[1]
                arr[i] = [tmp_x, tmp_y]
        
        elif last_action == -1:
            tkmb.showinfo("Вернуть последнее действие", "Вернуть последнее действие можно только один раз")
        
        create_drawing(arr, arr_connects, anchor)
        last_action = -1

    elif action == 6:
        tkmb.showinfo("Условие программы", "Программа рисует исходный рисунок на холсте и производит действия согласно кнопкам.\n"
        "Переместить: двигает полигон относительно его текущей позиции по осям Ox и Oy на введенные величины.\n"
        "Обновить точку-якорь: обновляет точку, относительно которой будет производиться поворот и масштабирование.\n"
        "Повернуть: поворачивает относительно точки-якоря на введенное количество градусов.\n"
        "Масштабировать: масштабирует относительно точки-якоря.\n"
        "Вернуть последнее действие: откатывает к предыдущему состоянию.\n"
        "Вернуть к изначальному: возвращает исходное значение каждой точке.\n")
    
    elif action == 7:
        tkmb.showinfo("Об авторе", "Автор программы - Писаренко Дмитрий ИУ7-44Б")

# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №2. Геометрические преобразования.")
window.geometry("1000x700")

# Конфигурация
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1000)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)
window.rowconfigure(9, weight=1)
window.rowconfigure(10, weight=1)
window.rowconfigure(11, weight=1000)
window.rowconfigure(12, weight=1)
window.rowconfigure(13, weight=1)

# Поле для рисования
canvas = tk.Canvas(window, width=700, height=700, bg="white")

# Текст
cur_font = "Helvetica 10"
tmp = ' '*25

label_dx = tk.Label(text="Перемещение по X:", font=cur_font)
label_dy = tk.Label(text="Перемещение по Y:", font=cur_font)
label_anchor = tk.Label(text="Точка-якорь:{0}".format(tmp), font=cur_font)
label_angle = tk.Label(text="Угол поворота (°):", font=cur_font)
label_scale_x = tk.Label(text="Масштаб. по X:", font=cur_font)
label_scale_y = tk.Label(text="Масштаб. по Y:", font=cur_font)

# Поля ввода
entry_dx = tk.Entry(width=22)
entry_dy = tk.Entry(width=22)
entry_anchor_x = tk.Entry(width=22)
entry_anchor_y = tk.Entry(width=22)
entry_angle = tk.Entry(width=22)
entry_scale_x = tk.Entry(width=22)
entry_scale_y = tk.Entry(width=22)

# Кнопки
return_to_orig = tk.Button(window, text="Вернуть к изначальному", width=40, command=lambda: perform_actions(0))
move = tk.Button(window, text="Переместить", width=40, command=lambda: perform_actions(1))
update_anchor = tk.Button(window, text="Обновить точку-якорь", width=40, command=lambda: perform_actions(2))
rotate = tk.Button(window, text="Повернуть", width=40, command=lambda: perform_actions(3))
scale = tk.Button(window, text="Масштабировать", width=40, command=lambda: perform_actions(4))
cancel = tk.Button(window, text="Вернуть последнее действие", width=40, command=lambda: perform_actions(5))

# Вкладки
menu = tk.Menu()
window.config(menu=menu)
menu.add_command(label="О программе", command=lambda: perform_actions(6))
menu.add_command(label="Об авторе", command=lambda: perform_actions(7))

# Размещение
canvas.grid(column=0, row=0, columnspan=4, rowspan=14, sticky="w")

label_dx.grid(column=3, row=0, sticky="ne", padx=5, pady=5)
entry_dx.grid(column=3, row=1, sticky="ne", padx=5, pady=5)
label_dy.grid(column=4, row=0, sticky="ne", padx=5, pady=5)
entry_dy.grid(column=4, row=1, sticky="ne", padx=5, pady=5)
move.grid(column=3, row=2, columnspan=2, sticky="ne")

label_anchor.grid(column=3, row=3, columnspan=2, sticky="ne", padx=5, pady=(60, 5))
entry_anchor_x.grid(column=3, row=4, sticky="ne", padx=5, pady=5)
entry_anchor_y.grid(column=4, row=4, sticky="ne", padx=5, pady=5)
update_anchor.grid(column=3, row=5, columnspan=2, sticky="ne")

label_angle.grid(column=3, row=6, sticky="ne", padx=5, pady=(60, 5))
entry_angle.grid(column=4, row=6, sticky="ne", padx=5, pady=(60, 5))
rotate.grid(column=3, row=7, columnspan=2, sticky="ne")

label_scale_x.grid(column=3, row=8, sticky="ne", padx=5, pady=(60, 5))
entry_scale_x.grid(column=3, row=9, sticky="ne", padx=5, pady=5)
label_scale_y.grid(column=4, row=8, sticky="ne", padx=5, pady=(60, 5))
entry_scale_y.grid(column=4, row=9, sticky="ne", padx=5, pady=5)
scale.grid(column=3, row=10, columnspan=2, sticky="ne")

cancel.grid(column=3, row=12, columnspan=2, sticky="se", padx=5, pady=5)
return_to_orig.grid(column=3, row=13, columnspan=2, sticky="se", padx=5, pady=5)

file_dots = open("dots.txt", "r")
file_connects = open("connects.txt", "r")
array_preparation(file_dots, file_connects)
arr_default = copy.deepcopy(arr)
create_drawing(arr, arr_connects, anchor)
file_dots.close()
file_connects.close()

window.mainloop()