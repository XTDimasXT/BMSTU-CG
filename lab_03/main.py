import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math

# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №3. Реализация и исследование алгоритмов построения отрезков.")
window.geometry("1550x860")

# Поле для рисования
canvas = tk.Canvas(window, width=1155, height=780, bg="white")

# Текст
cur_font = "Helvetica 10"
main_font = "Helvetica 12"
tmp_1 = " " * 13
tmp_2 = " " * 23
tmp_3 = " " * 16
tmp_4 = " " * 25
tmp_5 = " " * 5

label_available_algorithms = tk.Label(text="ДОСТУПНЫЕ АЛГОРИТМЫ {}".format(tmp_1), font=main_font)
label_colour_choose = tk.Label(text="ВЫБОР ЦВЕТА {}".format(tmp_2), font=main_font)
label_colour_background = tk.Label(text="Цвет фона:", font=cur_font)
label_colour_line = tk.Label(text="Цвет линий:", font=cur_font)
label_line_construction = tk.Label(text="ПОСТРОЕНИЕ ЛИНИЙ {}".format(tmp_3), font=main_font)
label_line_x0 = tk.Label(text="x0 {}".format(tmp_5), font=cur_font)
label_line_y0 = tk.Label(text="y0 {}".format(tmp_5), font=cur_font)
label_line_x1 = tk.Label(text="x1 {}".format(tmp_5), font=cur_font)
label_line_y1 = tk.Label(text="y1 {}".format(tmp_5), font=cur_font)
label_angle = tk.Label(text="Угол поворота (°):", font=cur_font)
label_compare_lines = tk.Label(text="СРАВНЕНИЯ {}".format(tmp_4), font=main_font)
label_line_length=tk.Label(text="Длина линии:", font=cur_font)

# Поля ввода
entry_x0 = tk.Entry(width=11)
entry_y0 = tk.Entry(width=11)
entry_x1 = tk.Entry(width=11)
entry_y1 = tk.Entry(width=11)
entry_angle = tk.Entry(width=22)
entry_line_length=tk.Entry(width=22)

# Кнопки
dda_but = tk.Button(window, text="Цифровой дифференциальный анализатор", width=45, command=lambda: perform_actions(1))
brensenham_float_but = tk.Button(window, text="Брезенхэм (вещественные)", width=45, command=lambda: perform_actions(2))
brensenham_int_but = tk.Button(window, text="Брезенхэм (целые)", width=45, command=lambda: perform_actions(3))
brensenham_grad_but = tk.Button(window, text="Брезенхэм (с устр. ступенчатости)", width=45, command=lambda: perform_actions(4))
wu_but = tk.Button(window, text="Ву", width=45, command=lambda: perform_actions(5))
library_but = tk.Button(window, text="Библиотечная", width=45, command=lambda: perform_actions(6))

white_colour_bg_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour(1))
yellow_colour_bg_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour(2))
orange_colour_bg_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour(3))
red_colour_bg_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour(4))
green_colour_bg_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour(5))
purple_colour_bg_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour(6))
black_colour_bg_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour(7))

white_colour_line_but = tk.Button(window, width=3, bg="#FFFFFF", command=lambda: set_colour(1))
yellow_colour_line_but = tk.Button(window, width=3, bg="#FFFF00", command=lambda: set_colour(2))
orange_colour_line_but = tk.Button(window, width=3, bg="#FFA500", command=lambda: set_colour(3))
red_colour_line_but = tk.Button(window, width=3, bg="#FF0000", command=lambda: set_colour(4))
green_colour_line_but = tk.Button(window, width=3, bg="#00FF7F", command=lambda: set_colour(5))
purple_colour_line_but = tk.Button(window, width=3, bg="#8A2BE2", command=lambda: set_colour(6))
black_colour_line_but = tk.Button(window, width=3, bg="#000000", command=lambda: set_colour(7))

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
canvas.grid(column=0, row=0, rowspan=23, sticky="w")

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

label_angle.grid(column=1, row=13, columnspan=4, sticky="ne", padx=5, pady=5)
entry_angle.grid(column=5, row=13, columnspan=4, sticky="ne", padx=5, pady=5)

draw_line_but.grid(column=1, row=14, columnspan=8, sticky="ne")
draw_spectre_but.grid(column=1, row=15, columnspan=8, sticky="ne")

## Сравнение времени + очистка + возврат
label_compare_lines.grid(column=1, row=16, columnspan=8, sticky="ne", padx=5, pady=5)
label_line_length.grid(column=1, row=17, columnspan=4, sticky="ne", padx=5, pady=5)
entry_line_length.grid(column=5, row=17, columnspan=4, sticky="ne", padx=5, pady=5)

compare_time_but.grid(column=1, row=18, columnspan=8, sticky="ne")
compare_gradation_but.grid(column=1, row=19, columnspan=8, sticky="ne", pady=(0,20))
clear_but.grid(column=1, row=20, columnspan=8, sticky="ne")
return_but.grid(column=1, row=21, columnspan=8, sticky="ne")

window.mainloop()