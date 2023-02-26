import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math

arr_dots = []

def paint_dot(event):
    global arr_dots
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)
    colour = "#000fff000"
    canvas.create_oval(x1, y1, x2, y2, fill=colour)
    arr_dots.append([event.x, event.y])


def show_dot(x, y, arr_dots):
    x1, y1, x2, y2 = (x - 3), (y - 3), (x + 3), (y + 3)
    colour = "#000fff000"
    canvas.create_oval(x1, y1, x2, y2, fill=colour)
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

# Настройка поля для рисования
canvas = tk.Canvas(window, width=700, height=700, bg="white")
canvas.bind("<Button-1>", paint_dot)

# Текст
label_x = tk.Label(text="Значение по x:")
label_y = tk.Label(text="Значение по y:")

# Поля ввода и вывода
entry_x = tk.Entry()
entry_y = tk.Entry()
result = tk.Entry(width=100)

# Кнопки
point = tk.Button(window, text="Поставить точку", command = lambda: perform_actions(1))
clear = tk.Button(window, text="Очистить экран", command = lambda: perform_actions(2))
calculate = tk.Button(window, text="Выполнить задание", command = lambda: perform_actions(3))

# Вкладки
frame1 = tk.Button(window, text="О программе", command = lambda: perform_actions(4))
frame2 = tk.Button(window, text="Об авторе", command = lambda: perform_actions(5))

frame1.pack(anchor=tk.NW)
frame2.pack(anchor=tk.NW)

# Размещение
canvas.pack(side=tk.LEFT)

label_x.pack(anchor=tk.N)
entry_x.pack(anchor=tk.N)
label_y.pack(anchor=tk.N)
entry_y.pack(anchor=tk.N)

point.pack(anchor=tk.N)
clear.pack(side=tk.BOTTOM)
calculate.pack(side=tk.BOTTOM)

result.pack(side=tk.RIGHT)
result.config(stat=tk.DISABLED)

window.mainloop()