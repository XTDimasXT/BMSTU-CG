import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math

arr_dots = []

def paint_dot(event):
    global arr_dots
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)
    colour = "#000fff000"
    canvas.create_oval(x1, y1, x2, y2, fill=colour)
    canvas.create_text(x1 + 5, y1 + 15, text="{0} {1}".format(event.x, event.y), tags="text")
    clear_not_full()
    if [event.x, event.y] not in arr_dots:
        arr_dots.append([event.x, event.y])


def show_dot(x, y, arr_dots):
    x1, y1, x2, y2 = (x - 3), (y - 3), (x + 3), (y + 3)
    colour = "#000fff000"
    canvas.create_oval(x1, y1, x2, y2, fill=colour)
    canvas.create_text(x1 + 5, y1 + 15, text="{0} {1}".format(x, y), tags="text")
    clear_not_full()
    arr_dots.append([x, y])

def clean_labels():
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)


def clean_table(arr_dots):
    canvas.delete("all")
    arr_dots.clear()

    result.config(stat=tk.NORMAL)
    result.delete(0, tk.END)
    result.config(stat=tk.DISABLED)


def canvas_recreate(arr_dots):
    canvas.delete("all")

    result.config(stat=tk.NORMAL)
    result.delete(0, tk.END)
    result.config(stat=tk.DISABLED)

    for i in range(len(arr_dots)):
        x1, y1, x2, y2 = (arr_dots[i][0] - 3), (arr_dots[i][1] - 3), (arr_dots[i][0] + 3), (arr_dots[i][1] + 3)
        colour = "#000fff000"
        canvas.create_oval(x1, y1, x2, y2, fill=colour)
        canvas.create_text(arr_dots[i][0] + 5, arr_dots[i][1] + 15, text="{0} {1}".format(arr_dots[i][0], arr_dots[i][1]))


def clear_not_full():
    canvas.delete("lines", "circles")
    result.config(stat=tk.NORMAL)
    result.delete(0, tk.END)
    result.config(stat=tk.DISABLED)


def perform_actions(action):
    global arr_dots

    if action == 1:
        x = entry_x.get()
        y = entry_y.get()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            if [x, y] in arr_dots:
                tkmb.showwarning("Предупреждение", "Эта точка уже была введена ранее")
                clean_labels()
                return 1
            if x >= 0 and x <= 700 and y >= 0 and y <= 700:
                show_dot(int(x), int(y), arr_dots)
                clean_labels()
            else:
                tkmb.showerror("Ошибка ввода", "Переданы значения, выходящие за размеры поля")
                clean_labels()
                return 1
        else:
            tkmb.showerror("Ошибка ввода", "Переданы не числа")
            clean_labels()
            return 1
    
    elif action == 2:
        clean_table(arr_dots)
    
    elif action == 3:
        if len(arr_dots) <= 2:
            tkmb.showerror("Ошибка выполнения", "Введено менее 3 точек")
            return 1

        canvas.delete("lines", "circles")
        res = find_min_delta()
        if res != -1:
            show_result("{:.2f}".format(res))
        else:
            tkmb.showerror("Ошибка выполнения", "Не обнаружено точек, из которых можно построить треугольник")
            return 1
    
    elif action == 4:
        tkmb.showinfo("Условие программы", "Из заданного на плоскости множества точек выбрать три различные точки так, чтобы"
        "разность между площадью круга, ограниченного окружностью, проходящей через эти"
        "три точки, и площадью треугольника с вершинами в этих точках была минимальной.")
    
    elif action == 5:
        tkmb.showinfo("Об авторе", "Автор программы - Писаренко Дмитрий ИУ7-44Б")
    
    elif action == 6:
        if len(arr_dots) == 0:
            tkmb.showinfo("Удаление точки", "На данный момент на поле нет точек")
        else:
            new_coords = simpledialog.askstring("Удаление точки", "Введите координаты через пробел").split()
            if len(new_coords) != 2:
                tkmb.showerror("Ошибка", "Координаты - это два различных числа")
            else:
                try:
                    x_coord = int(new_coords[0])
                    y_coord = int(new_coords[1])
                except:
                    tkmb.showerror("Ошибка", "Координаты могут задаваться только целыми числами")
                
                new_coords = [x_coord, y_coord]
                if new_coords in arr_dots:
                    arr_dots.remove(new_coords)
                    canvas_recreate(arr_dots)
                else:
                    tkmb.showinfo("Удаление точки", "Такая точка не была введена")
        
    
    elif action == 7:
        if len(arr_dots) == 0:
            tkmb.showinfo("Редактирование точки", "На данный момент на поле нет точек")
        else:
            dot_coords = simpledialog.askstring("Редактирование точки", "Введите координаты через пробел (точки, которую хотите заменить)").split()
            try:
                x_coord = int(dot_coords[0])
                y_coord = int(dot_coords[1])
            except:
                tkmb.showerror("Ошибка", "Координаты могут задаваться только целыми числами")
            
            if x_coord > 700 or y_coord > 700 or x_coord < 0 or y_coord < 0:
                tkmb.showerror("Ошибка", "Переданы значения, выходящие за размеры поля")
            else:
                dot_coords = [x_coord, y_coord]
                if dot_coords in arr_dots:
                    new_coords = simpledialog.askstring("Редактирование точки", "Введите координаты через пробел (точки, которую хотите добавить)", parent=window).split()
                    try:
                        x_coord_new = int(new_coords[0])
                        y_coord_new = int(new_coords[1])
                    except:
                        tkmb.showerror("Ошибка", "Координаты могут задаваться только целыми числами")

                    if x_coord_new > 700 or y_coord_new > 700 or x_coord_new < 0 or y_coord_new < 0:
                        tkmb.showerror("Ошибка", "Переданы значения, выходящие за размеры поля")

                    new_coords = [x_coord_new, y_coord_new]
                    if new_coords in arr_dots:
                        tkmb.showwarning("Предупреждение", "Эта точка уже существует на поле")
                    else:
                        arr_dots.remove(dot_coords)
                        arr_dots.append(new_coords)
                        canvas_recreate(arr_dots)



def create_triangle(res_dots):
    ind1, ind2, ind3 = res_dots[0], res_dots[1], res_dots[2]
    canvas.create_line(arr_dots[ind1][0], arr_dots[ind1][1], arr_dots[ind2][0], arr_dots[ind2][1], tags="lines")
    canvas.create_line(arr_dots[ind2][0], arr_dots[ind2][1], arr_dots[ind3][0], arr_dots[ind3][1], tags="lines")
    canvas.create_line(arr_dots[ind3][0], arr_dots[ind3][1], arr_dots[ind1][0], arr_dots[ind1][1], tags="lines")


def create_circle(res_dots, radius):
    global arr_dots

    ind1, ind2, ind3 = res_dots[0], res_dots[1], res_dots[2]

    x1, x2, x3 = arr_dots[ind1][0], arr_dots[ind2][0], arr_dots[ind3][0]
    y1, y2, y3 = arr_dots[ind1][1], arr_dots[ind2][1], arr_dots[ind3][1]

    zx = (y1 - y2) * (x3 ** 2 + y3 ** 2) + (y2 - y3) * (x1 ** 2 + y1 ** 2) + (y3 - y1) * (x2 ** 2 + y2 ** 2)
    zy = (x1 - x2) * (x3 ** 2 + y3 ** 2) + (x2 - x3) * (x1 ** 2 + y1 ** 2) + (x3 - x1) * (x2 ** 2 + y2 ** 2)
    z = (x1 - x2) * (y3 - y1) - (y1 - y2) * (x3 - x1)

    rx = (zx / (2 * z)) * (-1)
    ry = zy / (2 * z)

    canvas.create_oval(rx - radius, ry - radius, rx + radius, ry + radius, tags="circles")


def find_min_delta():
    res_dots = []
    delta = None

    for i in range(len(arr_dots) - 2):
        for j in range(i + 1, len(arr_dots) - 1):
            for k in range(j + 1, len(arr_dots)):
                x1, x2, x3 = arr_dots[i][0], arr_dots[j][0], arr_dots[k][0]
                y1, y2, y3 = arr_dots[i][1], arr_dots[j][1], arr_dots[k][1]

                triangle_square = math.fabs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

                a = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
                b = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
                c = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))

                if a + b > c and b + c > a and a + c > b:
                    semi_p = (a + b + c) / 2
                    r = a * b * c / 4 / math.sqrt(semi_p * (semi_p - a) * (semi_p - b) * (semi_p - c))
                    circle_square = r * r * math.pi
                    if delta == None or circle_square - triangle_square < delta:
                        delta = circle_square - triangle_square
                        res_dots = [i, j, k]
                        min_r = r
    
    if len(res_dots) == 0:
        delta = -1
    else:
        create_triangle(res_dots)
        create_circle(res_dots, min_r)
    
    return delta


def show_result(res):
    result.config(stat=tk.NORMAL)
    result.delete(0, tk.END)
    result.insert(0, res)
    result.config(stat=tk.DISABLED)


# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №1. Геометрические построения.")
window.geometry("1000x700")

#Конфигурация
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
window.rowconfigure(5, weight=1000)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)
window.rowconfigure(9, weight=1)


# Настройка поля для рисования
canvas = tk.Canvas(window, width=700, height=700, bg="white")
canvas.bind("<Button-1>", paint_dot)

# Текст
label_x = tk.Label(text="Значение по X:", font="Helvetica 10")
label_y = tk.Label(text="Значение по Y:", font="Helvetica 10")
label_res = tk.Label(text="Результат программы:                  ", font="Helvetica 10")

# Поля ввода и вывода
entry_x = tk.Entry(width=22)
entry_y = tk.Entry(width=22)
result = tk.Entry(width=35, font="Helvetica 11")

# Кнопки
point = tk.Button(window, text="Поставить точку", width=40, command = lambda: perform_actions(1))
clear = tk.Button(window, text="Очистить экран", width=40, command = lambda: perform_actions(2))
calculate = tk.Button(window, text="Выполнить задание", width=40, command = lambda: perform_actions(3))
delete = tk.Button(window, text="Удалить точку", width=40, command = lambda: perform_actions(6))
redact = tk.Button(window, text="Редактировать точку", width=40, command = lambda: perform_actions(7))

# Вкладки
tab1 = tk.Button(window, text="О программе", command = lambda: perform_actions(4))
tab2 = tk.Button(window, text="Об авторе", command = lambda: perform_actions(5))

# Размещение
tab1.grid(column=0, row=0, sticky="nw", padx=5, pady=5)
tab2.grid(column=1, row=0, sticky="nw", padx=5, pady=5)

canvas.grid(column=0, row=1, columnspan=4, rowspan=9, sticky="w")

label_x.grid(column=3, row=0, sticky="ne", padx=5, pady=5)
entry_x.grid(column=3, row=1, sticky="ne", padx=5, pady=5)
label_y.grid(column=4, row=0, sticky="ne", padx=5, pady=5)
entry_y.grid(column=4, row=1, sticky="ne", padx=5, pady=5)

label_res.grid(column=3, row=3, columnspan=2, sticky="se", padx=5, pady=5)
result.grid(column=3, row=4, columnspan=2, sticky="se", padx=5, pady=5)
result.config(stat=tk.DISABLED)

point.grid(column=3, row=2, columnspan=2, sticky="se")
clear.grid(column=3, row=6, columnspan=2, sticky="se")
calculate.grid(column=3, row=7, columnspan=2, sticky="se")
delete.grid(column=3, row=8, columnspan=2, sticky="se")
redact.grid(column=3, row=9, columnspan=2, sticky="se")

window.mainloop()