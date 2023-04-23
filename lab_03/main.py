import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math

from brensenham import *
from dda import *
from wu import *


bg_colour = "#FFFFFF"
line_colour = "#000000"
algorithm = "Библиотечная"


def set_default_colours_algorithms():
    dda_but.config(bg="#F0F0F0")
    brensenham_float_but.config(bg="#F0F0F0")
    brensenham_int_but.config(bg="#F0F0F0")
    brensenham_grad_but.config(bg="#F0F0F0")
    wu_but.config(bg="#F0F0F0")
    library_but.config(bg="#F0F0F0")


def draw_line_by_algorithm(canvas, points):
    for point in points:
        canvas.create_line(point[0], point[1], point[0] + 1, point[1], fill=point[2])


def draw_spectre_by_algorithm(canvas, algorithm, xs, ys, angle, length, line_colour):
    if algorithm == "ЦДА":
        i = 0
        while i < 2 * math.pi:
            xs_new = xs + math.cos(i) * length
            ys_new = ys - math.sin(i) * length
            points = dda_line(xs, ys, xs_new, ys_new, line_colour)
            draw_line_by_algorithm(canvas, points)
            i += angle
    
    elif algorithm == "Брезенхэм (вещественные)":
        i = 0
        while i < 2 * math.pi:
            xs_new = xs + math.cos(i) * length
            ys_new = ys - math.sin(i) * length
            points = brensenham_float_line(xs, ys, xs_new, ys_new, line_colour)
            draw_line_by_algorithm(canvas, points)
            i += angle
    
    elif algorithm == "Брезенхэм (целые)":
        i = 0
        while i < 2 * math.pi:
            xs_new = xs + math.cos(i) * length
            ys_new = ys - math.sin(i) * length
            points = brensenham_integer_line(xs, ys, xs_new, ys_new, line_colour)
            draw_line_by_algorithm(canvas, points)
            i += angle
    
    elif algorithm == "Брезенхэм (с устр. ступенчатости)":
        i = 0
        while i < 2 * math.pi:
            xs_new = xs + math.cos(i) * length
            ys_new = ys - math.sin(i) * length
            points = brensenham_smooth_line(canvas, xs, ys, xs_new, ys_new, line_colour)
            draw_line_by_algorithm(canvas, points)
            i += angle


def perform_actions(action):
    global bg_colour, line_colour, algorithm
    global dda_but, brensenham_float_but, brensenham_int_but, brensenham_grad_but, wu_but, library_but 
    
    cur_colour = "#FAE39E"
    
    if action == 1:
        algorithm = "ЦДА"
        set_default_colours_algorithms()
        dda_but = tk.Button(window, text="Цифровой дифференциальный анализатор", bg=cur_colour, width=45, command=lambda: perform_actions(1))
        dda_but.grid(column=1, row=1, columnspan=8, sticky="ne")
    
    elif action == 2:
        algorithm = "Брезенхэм (вещественные)"
        set_default_colours_algorithms()
        brensenham_float_but = tk.Button(window, text="Брезенхэм (вещественные)", bg=cur_colour, width=45, command=lambda: perform_actions(2))
        brensenham_float_but.grid(column=1, row=2, columnspan=8, sticky="ne")
    
    elif action == 3:
        algorithm = "Брезенхэм (целые)"
        set_default_colours_algorithms()
        brensenham_int_but = tk.Button(window, text="Брезенхэм (целые)", bg=cur_colour, width=45, command=lambda: perform_actions(3))
        brensenham_int_but.grid(column=1, row=3, columnspan=8, sticky="ne")
        
    elif action == 4:
        algorithm = "Брезенхэм (с устр. ступенчаности)"
        set_default_colours_algorithms()
        brensenham_grad_but = tk.Button(window, text="Брезенхэм (с устр. ступенчатости)", bg=cur_colour, width=45, command=lambda: perform_actions(4))
        brensenham_grad_but.grid(column=1, row=4, columnspan=8, sticky="ne")
        
    elif action == 5:
        algorithm = "Ву"
        set_default_colours_algorithms()
        wu_but = tk.Button(window, text="Ву", bg=cur_colour, width=45, command=lambda: perform_actions(5))
        wu_but.grid(column=1, row=5, columnspan=8, sticky="ne")
    
    elif action == 6:
        algorithm = "Библиотечная"
        set_default_colours_algorithms()
        library_but = tk.Button(window, text="Библиотечная", bg=cur_colour, width=45, command=lambda: perform_actions(6))
        library_but.grid(column=1, row=6, columnspan=8, sticky="ne")
        
    elif action == 7:
        x0 = entry_x0.get()
        y0 = entry_y0.get()
        x1 = entry_x1.get()
        y1 = entry_x1.get()
    
        try:
            x0, y0, x1, y1 = float(x0), float(y0), float(x1), float(y1)
        except:
            tkmb.showerror("Ошибка ввода", "Переданы некорректные значения")
            clear_line_entries()
            return 1
        
        if algorithm == "Библиотечная":
            library_line(x0, y0, x1, y1, line_colour)
            
        elif algorithm == "ЦДА":
            points = dda_line(x0, y0, x1, y1, line_colour)
            draw_line_by_algorithm(canvas, points)
        
        elif algorithm == "Брезенхэм (вещественные)":
            points = brensenham_float_line(x0, y0, x1, y1, line_colour)
            draw_line_by_algorithm(canvas, points)
        
        elif algorithm == "Брезенхэм (целые)":
            points = brensenham_integer_line(x0, y0, x1, y1, line_colour)
            draw_line_by_algorithm(canvas, points)
        
        elif algorithm == "Брезенхэм (с устр. ступенчатости)":
            points = brensenham_smooth_line(canvas, x0, y0, x1, y1, line_colour)
            draw_line_by_algorithm(canvas, points)
    
    elif action == 8:
        xs = entry_xs.get()
        ys = entry_ys.get()
        angle = entry_angle.get()
        length = entry_line_length.get()
        
        try:
            xs, ys, angle, length = float(xs), float(ys), float(angle), float(length)
            angle = angle * math.pi / 180
        except ValueError:
            tkmb.showerror("Ошибка ввода", "Переданы некорректные значения")
            clear_spectre_entries()
            return 1
        except ZeroDivisionError:
            tkmb.showerror("Ошибка ввода", "Угол не может быть равен 0")
            clear_spectre_entries()
            return 1
        
        if algorithm == "Библиотечная":
            library_spectre(xs, ys, angle, length, line_colour)
            
        elif algorithm == "ЦДА":
            draw_spectre_by_algorithm(canvas, "ЦДА", xs, ys, angle, length, line_colour)
        
        elif algorithm == "Брезенхэм (вещественные)":
            draw_spectre_by_algorithm(canvas, "Брезенхэм (вещественные)", xs, ys, angle, length, line_colour)
            
        elif algorithm == "Брезенхэм (целые)":
            draw_spectre_by_algorithm(canvas, "Брезенхэм (целые)", xs, ys, angle, length, line_colour)
            
        elif algorithm == "Брезенхэм (с устр. ступечатости)":
            draw_spectre_by_algorithm(canvas, "Брезенхэм (с устр. ступенчаности)", xs, ys, angle, length, line_colour)
        
    
    elif action == 11:
        clear_canvas()


def set_colour_bg(action):
    global canvas, bg_colour
    
    if action == 1:
        canvas.config(bg="#FFFFFF")
        bg_colour = "#FFFFFF"
    
    elif action == 2:
        canvas.config(bg="#FFFF00")
        bg_colour = "#FFFF00"
    
    elif action == 3:
        canvas.config(bg="#FFA500")
        bg_colour = "#FFA500"
        
    elif action == 4:
        canvas.config(bg="#FF0000")
        bg_colour = "#FF0000"
    
    elif action == 5:
        canvas.config(bg="#00FF7F")
        bg_colour = "#00FF7F"
    
    elif action == 6:
        canvas.config(bg="#8A2BE2")
        bg_colour = "#8A2BE2"
    
    elif action == 7:
        canvas.config(bg="#000000")
        bg_colour = "#000000"


def set_colour_line(action):
    global line_colour
    
    if action == 1:
        line_colour = "#FFFFFF"
    
    elif action == 2:
        line_colour = "#FFFF00"
    
    elif action == 3:
        line_colour = "#FFA500"
        
    elif action == 4:
        line_colour = "#FF0000"
    
    elif action == 5:
        line_colour = "#00FF7F"
    
    elif action == 6:
        line_colour = "#8A2BE2"
    
    elif action == 7:
        line_colour = "#000000"
        

def clear_canvas():
    canvas.delete("all")
    

def clear_line_entries():
    entry_x0.delete(0, tk.END)
    entry_y0.delete(0, tk.END)
    entry_x1.delete(0, tk.END)
    entry_y1.delete(0, tk.END)


def clear_spectre_entries():
    entry_xs.delete(0, tk.END)
    entry_ys.delete(0, tk.END)
    entry_angle.delete(0, tk.END)
    entry_line_length.delete(0, tk.END)


def library_line(x0, y0, x1, y1, line_colour):
    canvas.create_line(x0, y0, x1, y1, fill=line_colour)


def library_spectre(xs, ys, angle, length, line_colour):
    i = 0
    while i < 2 * math.pi:
        xs_new = xs + math.cos(i) * length
        ys_new = ys - math.sin(i) * length
        canvas.create_line(xs, ys, xs_new, ys_new, fill=line_colour)
        i += angle


# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №3. Реализация и исследование алгоритмов построения отрезков.")
window.geometry("1550x860")

# Поле для рисования
canvas = tk.Canvas(window, width=1155, height=770, bg=bg_colour)

# Текст
cur_font = "Helvetica 10"
main_font = "Helvetica 12"
tmp_1 = " " * 13
tmp_2 = " " * 23
tmp_3 = " " * 16
tmp_4 = " " * 25
tmp_5 = " " * 5
tmp_6 = " " * 2

label_available_algorithms = tk.Label(text="ДОСТУПНЫЕ АЛГОРИТМЫ {}".format(tmp_1), font=main_font)
label_colour_choose = tk.Label(text="ВЫБОР ЦВЕТА {}".format(tmp_2), font=main_font)
label_colour_background = tk.Label(text="Цвет фона", font=cur_font)
label_colour_line = tk.Label(text="Цвет линий", font=cur_font)
label_line_construction = tk.Label(text="ПОСТРОЕНИЕ ЛИНИЙ {}".format(tmp_3), font=main_font)
label_line_x0 = tk.Label(text="x0 {}".format(tmp_5), font=cur_font)
label_line_y0 = tk.Label(text="y0 {}".format(tmp_5), font=cur_font)
label_line_x1 = tk.Label(text="x1 {}".format(tmp_5), font=cur_font)
label_line_y1 = tk.Label(text="y1 {}".format(tmp_5), font=cur_font)
label_line_xs = tk.Label(text="xc {}".format(tmp_5), font=cur_font)
label_line_ys = tk.Label(text="yc {}".format(tmp_5), font=cur_font)
label_angle = tk.Label(text="Угол поворота (°) {}".format(tmp_6), font=cur_font)
label_compare_lines = tk.Label(text="СРАВНЕНИЯ {}".format(tmp_4), font=main_font)
label_line_length=tk.Label(text="Длина линии {}".format(tmp_5), font=cur_font)

# Поля ввода
entry_x0 = tk.Entry(width=11)
entry_y0 = tk.Entry(width=11)
entry_x1 = tk.Entry(width=11)
entry_y1 = tk.Entry(width=11)
entry_xs = tk.Entry(width=11)
entry_ys = tk.Entry(width=11)
entry_angle = tk.Entry(width=22)
entry_line_length=tk.Entry(width=22)

# Кнопки
dda_but = tk.Button(window, text="Цифровой дифференциальный анализатор", width=45, command=lambda: perform_actions(1))
brensenham_float_but = tk.Button(window, text="Брезенхэм (вещественные)", width=45, command=lambda: perform_actions(2))
brensenham_int_but = tk.Button(window, text="Брезенхэм (целые)", width=45, command=lambda: perform_actions(3))
brensenham_grad_but = tk.Button(window, text="Брезенхэм (с устр. ступенчатости)", width=45, command=lambda: perform_actions(4))
wu_but = tk.Button(window, text="Ву", width=45, command=lambda: perform_actions(5))
library_but = tk.Button(window, text="Библиотечная", bg="#FAE39E", width=45, command=lambda: perform_actions(6))

white_colour_bg_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour_bg(1))
yellow_colour_bg_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour_bg(2))
orange_colour_bg_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour_bg(3))
red_colour_bg_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour_bg(4))
green_colour_bg_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour_bg(5))
purple_colour_bg_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour_bg(6))
black_colour_bg_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour_bg(7))

white_colour_line_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour_line(1))
yellow_colour_line_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour_line(2))
orange_colour_line_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour_line(3))
red_colour_line_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour_line(4))
green_colour_line_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour_line(5))
purple_colour_line_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour_line(6))
black_colour_line_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour_line(7))

draw_line_but = tk.Button(window, text="Построить линию", width=45, command=lambda: perform_actions(7))
draw_spectre_but = tk.Button(window, text="Построить спектр", width=45, command=lambda: perform_actions(8))

compare_time_but = tk.Button(window, text="Сравнение времени", width=45, command=lambda: perform_actions(9))
compare_gradation_but = tk.Button(window, text="Сравнение ступенчатости", width=45, command=lambda: perform_actions(10))

clear_but = tk.Button(window, text="Очистить экран", width=45, command=lambda: perform_actions(11))
return_but = tk.Button(window, text="Вернуть последнее действие", width=45, command=lambda: perform_actions(12))

# Вкладки
menu = tk.Menu()
window.config(menu=menu)
menu.add_command(label="О программе", command=lambda: perform_actions(13))
menu.add_command(label="Об авторе", command=lambda: perform_actions(14))

# Размещение
canvas.grid(column=0, row=0, rowspan=24, sticky="w")

## Алгоритмы
label_available_algorithms.grid(column=1, row=0, columnspan=8, sticky="ne")
dda_but.grid(column=1, row=1, columnspan=8, sticky="ne")
brensenham_float_but.grid(column=1, row=2, columnspan=8, sticky="ne")
brensenham_int_but.grid(column=1, row=3, columnspan=8, sticky="ne")
brensenham_grad_but.grid(column=1, row=4, columnspan=8, sticky="ne")
wu_but.grid(column=1, row=5, columnspan=8, sticky="ne")
library_but.grid(column=1, row=6, columnspan=8, sticky="ne")

## Цвета
label_colour_choose.grid(column=1, row=7, columnspan=8, sticky="ne", padx=5, pady=5)

label_colour_background.grid(column=1, row=8, sticky="ne", padx=5, pady=5)
white_colour_bg_but.grid(column=2, row=8, sticky="ne")
yellow_colour_bg_but.grid(column=3, row=8, sticky="ne")
orange_colour_bg_but.grid(column=4, row=8, sticky="ne")
red_colour_bg_but.grid(column=5, row=8, sticky="ne")
green_colour_bg_but.grid(column=6, row=8, sticky="ne")
purple_colour_bg_but.grid(column=7, row=8, sticky="ne")
black_colour_bg_but.grid(column=8, row=8, sticky="ne")

label_colour_line.grid(column=1, row=9, sticky="ne", padx=5, pady=5)
white_colour_line_but.grid(column=2, row=9, sticky="ne")
yellow_colour_line_but.grid(column=3, row=9, sticky="ne")
orange_colour_line_but.grid(column=4, row=9, sticky="ne")
red_colour_line_but.grid(column=5, row=9, sticky="ne")
green_colour_line_but.grid(column=6, row=9, sticky="ne")
purple_colour_line_but.grid(column=7, row=9, sticky="ne")
black_colour_line_but.grid(column=8, row=9, sticky="ne")

## Построение линий
label_line_construction.grid(column=1, row=10, columnspan=8, sticky="ne", padx=5, pady=5)

label_line_x0.grid(column=1, row=11, columnspan=2, sticky="ne", padx=5, pady=5)
label_line_y0.grid(column=3, row=11, columnspan=2, sticky="ne", padx=5, pady=5)
label_line_x1.grid(column=5, row=11, columnspan=2, sticky="ne", padx=5, pady=5)
label_line_y1.grid(column=7, row=11, columnspan=2, sticky="ne", padx=5, pady=5)

entry_x0.grid(column=1, row=12, columnspan=2, sticky="ne", padx=5)
entry_y0.grid(column=3, row=12, columnspan=2, sticky="ne", padx=5)
entry_x1.grid(column=5, row=12, columnspan=2, sticky="ne", padx=5)
entry_y1.grid(column=7, row=12, columnspan=2, sticky="ne", padx=5)

label_line_xs.grid(column=1, row=14, columnspan=2, sticky="ne", padx=5, pady=5)
label_line_ys.grid(column=3, row=14, columnspan=2, sticky="ne", padx=5, pady=5)
label_angle.grid(column=5, row=14, columnspan=4, sticky="ne", padx=5, pady=5)

entry_xs.grid(column=1, row=15, columnspan=2, sticky="ne", padx=5)
entry_ys.grid(column=3, row=15, columnspan=2, sticky="ne", padx=5)
entry_angle.grid(column=5, row=15, columnspan=4, sticky="ne", padx=5)

label_line_length.grid(column=1, row=16, columnspan=4, sticky="ne", padx=5, pady=5)
entry_line_length.grid(column=5, row=16, columnspan=4, sticky="ne", padx=5, pady=5)

draw_line_but.grid(column=1, row=13, columnspan=8, sticky="ne")
draw_spectre_but.grid(column=1, row=17, columnspan=8, sticky="ne")

## Сравнение времени + очистка + возврат действия
label_compare_lines.grid(column=1, row=18, columnspan=8, sticky="ne", padx=5, pady=5)
compare_time_but.grid(column=1, row=19, columnspan=8, sticky="ne")
compare_gradation_but.grid(column=1, row=20, columnspan=8, sticky="ne", pady=(0, 20))
clear_but.grid(column=1, row=21, columnspan=8, sticky="ne")
return_but.grid(column=1, row=22, columnspan=8, sticky="ne")

window.mainloop()