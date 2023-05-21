from tkinter import messagebox
from algorithms import *

import copy

def set_pixel(canvas, x, y, colour):
    canvas.create_line(x, y, x + 1, y, fill=colour)


def clear_canvas(canvas, figure, clipper):
    canvas.delete("all")
    figure.clear()
    clipper.clear()


def clear_clipper(canvas, figure, clipper, figure_colour):
    canvas.delete("all")

    draw_figure(canvas, figure, figure_colour)
    clipper.clear()


def show_info():
    messagebox.showinfo('Информация о программе',
                        'Автор программы - Писаренко Дмитрий ИУ7-44Б.\n'
                        'Для отсечения прозивольного многоугольника выпуклым отсекателем используется алгоритм Сазерленда-Ходжмена.\n'
                        '========Инструкции для пользователя:========\n'
                        'ЛКМ - добавление вершины отсекателя.\n'
                        'ПКМ - добавление вершины фигуры.')


def draw_figure(canvas, figure, figure_colour):
    for i in range(len(figure) - 1):
        canvas.create_line(figure[i], figure[i + 1], fill=figure_colour)


def close_figure(canvas, figure, figure_colour, fig_name):
    if len(figure) < 3:
        messagebox.showwarning("Ошибка ввода!", "%s иметь >= 3 вершин!\n" % (fig_name))
        return

    if figure[0] == figure[-1]:
        messagebox.showwarning("Ошибка ввода!", "%s замкнут!\n" % (fig_name))
        return

    figure.append(figure[0])

    canvas.create_line(figure[-2], figure[-1], fill=figure_colour)


def click_btn(event, figure, clipper, canvas, clipper_colour, colour_figure):
    if len(clipper) > 3 and clipper[0] == clipper[-1]:
        clear_clipper(canvas, figure, clipper, colour_figure)

    x = event.x
    y = event.y

    if len(clipper) > 0 and clipper[-1][0] == x and clipper[-1][1] == y:
        return

    set_pixel(canvas, x, y, clipper_colour)

    clipper.append([x, y])

    if len(clipper) >= 2:
        canvas.create_line(clipper[-2], clipper[-1], fill=clipper_colour)


def add_vertex(canvas, figure, clipper, figure_colour, clipper_colour, x_entry, y_entry):
    try:
        x = int(x_entry.get())
        y = int(y_entry.get())
    except:
        messagebox.showwarning("Ошибка",
                               "Неверно заданны координаты вершины!\n"
                               "Ожидался ввод целых чисел.")
        return

    if len(clipper) > 3 and clipper[0] == clipper[-1]:
        clear_clipper(canvas, figure, clipper, figure_colour)

    set_pixel(canvas, x, y, clipper_colour)

    clipper.append([x, y])

    if len(clipper) >= 2:
        canvas.create_line(clipper[-2], clipper[-1], fill=clipper_colour)


def cut_off(canvas, figure, clipper, result_colour):
    if not clipper:
        messagebox.showinfo("Ошибка!", "Отсутствует отсекатель")
        return
    if not check_polygon(clipper):
        messagebox.showinfo("Ошибка!", "Отсекатель невыпуклый!\nОжидалось, что отсекатель будет выпуклым!")
        return

    result = copy.deepcopy(figure)

    for index in range(-1, len(clipper) - 1):
        line = [clipper[index], clipper[index + 1]]
        position_dot = clipper[index + 1]

        result = sutherland_hodgman_algorythm(line, position_dot, result)

        if len(result) <= 2:
            return

    draw_result_figure(result, canvas, result_colour)


def draw_result_figure(figure_dots, canvas, result_colour):
    fixed_figure = remove_odd_sides(figure_dots)

    for line in fixed_figure:
        canvas.create_line(line[0], line[1], fill = result_colour)