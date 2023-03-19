import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk
import math

# Настройка основного окна
window = tk.Tk()
window.title("Лабораторная работа №3. Реализация и исследование алгоритмов построения отрезков.")
window.geometry("1000x700")

# Поле для рисования
canvas = tk.Canvas(window, width=700, height=700, bg="white")

# Текст
cur_font = "Helvetica 10"

label_available_algorithms = tk.Label(text="Доступные алгоритмы", font=cur_font)
label_colour_choose = tk.Label(text="Выбор цвета", font=cur_font)
label_colour_background = tk.Label(text="Цвет фона:", font=cur_font)
label_colour_line = tk.Label(text="Цвет линий:", font=cur_font)
label_line_construction = tk.Label(text="Построение линий", font=cur_font)
label_line_x0 = tk.Label(text="x0", font=cur_font)
label_line_y0 = tk.Label(text="y0", font=cur_font)
label_line_x1 = tk.Label(text="x1", font=cur_font)
label_line_y1 = tk.Label(text="y0", font=cur_font)
label_angle = tk.Label(text="Угол поворота (°):", font=cur_font)
label_line_length=tk.Label(text="Длина линии", font=cur_font)

# Поля ввода
entry_x0 = tk.Entry(width=10)
entry_y0 = tk.Entry(width=10)
entry_x1 = tk.Entry(width=10)
entry_y1 = tk.Entry(width=10)
entry_angle = tk.Entry(width=10)
entry_line_length=tk.Entry(width=10)

# Кнопки
