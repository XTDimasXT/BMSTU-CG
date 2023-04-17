import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math
import copy


bg_colour = "#FFFFFF"
line_colour = "#000000"
algorithm = "Библиотечная"


def perform_actions(action):
    return 1


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


def set_colour_circle(action):
    global circle_colour
    
    if action == 1:
        circle_colour = "#FFFFFF"
    
    elif action == 2:
        circle_colour = "#FFFF00"
    
    elif action == 3:
        circle_colour = "#FFA500"
        
    elif action == 4:
        circle_colour = "#FF0000"
    
    elif action == 5:
        circle_colour = "#00FF7F"
    
    elif action == 6:
        circle_colour = "#8A2BE2"
    
    elif action == 7:
        circle_colour = "#000000"

# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №4. Реализация и исследование алгоритмов построения окружностей и эллипсов.")
window.geometry("1550x860")

# Поле для рисования
canvas = tk.Canvas(window, width=1155, height=770, bg="white")

# Текст
secondary_font = "Helvetica 10"
main_font = "Helvetica 12"
tmp_1 = " " * 13
tmp_2 = " " * 23
tmp_3 = " " * 16
tmp_4 = " " * 25
tmp_5 = " " * 5
tmp_6 = " " * 2

label_available_algorithms = tk.Label(text="ДОСТУПНЫЕ АЛГОРИТМЫ {}".format(tmp_1), font=main_font)
label_colour_choose = tk.Label(text="ВЫБОР ЦВЕТА {}".format(tmp_2), font=main_font)
label_colour_background = tk.Label(text="Цвет фона", font=secondary_font)
label_colour_circle = tk.Label(text="Цвет линий", font=secondary_font)
label_circle_ellipse_construction = tk.Label(text="ПОСТРОЕНИЕ ОКРУЖНОСТЕЙ/ЭЛЛИПСОВ {}".format(tmp_6), font=main_font)
label_circle_ellipse_xc = tk.Label(text="xc {}".format(tmp_5), font=secondary_font)
label_circle_ellipse_yc = tk.Label(text="yc {}".format(tmp_5), font=secondary_font)
label_circle = tk.Label(text="Окружность {}".format(tmp_5), font=secondary_font)
label_ellipse = tk.Label(text="Эллипс {}".format(tmp_5), font=secondary_font)
label_circle_radius = tk.Label(text="Радиус {}".format(tmp_5), font=secondary_font)
label_ellipse_width = tk.Label(text="Ширина {}".format(tmp_5), font=secondary_font)
label_ellipse_heigth = tk.Label(text="Высота {}".format(tmp_5), font=secondary_font)
label_step = tk.Label(text="Шаг изменения {}".format(tmp_6), font=secondary_font)
label_quantity = tk.Label(text="Кол-во фигур {}".format(tmp_6), font=secondary_font)

# Поля ввода
entry_xс = tk.Entry(width=11)
entry_yс = tk.Entry(width=11)
entry_radius = tk.Entry(width=11)
entry_width = tk.Entry(width=11)
entry_heigth = tk.Entry(width=11)
entry_step = tk.Entry(width=11)
entry_quantity = tk.Entry(width=11)

# Кнопки
canonical_but = tk.Button(window, text="Каноническое уравнение", width=45, command=lambda: perform_actions(1))
parametric_but = tk.Button(window, text="Параметрическое уравнение", width=45, command=lambda: perform_actions(2))
medium_but = tk.Button(window, text="Средняя точка", width=45, command=lambda: perform_actions(3))
brensenham_but = tk.Button(window, text="Брезенхэм", width=45, command=lambda: perform_actions(4))
library_but = tk.Button(window, text="Библиотечная", bg="#FAE39E", width=45, command=lambda: perform_actions(5))

white_colour_bg_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour_bg(1))
yellow_colour_bg_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour_bg(2))
orange_colour_bg_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour_bg(3))
red_colour_bg_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour_bg(4))
green_colour_bg_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour_bg(5))
purple_colour_bg_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour_bg(6))
black_colour_bg_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour_bg(7))

white_colour_circle_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour_circle(1))
yellow_colour_circle_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour_circle(2))
orange_colour_circle_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour_circle(3))
red_colour_circle_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour_circle(4))
green_colour_circle_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour_circle(5))
purple_colour_circle_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour_circle(6))
black_colour_circle_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour_circle(7))

