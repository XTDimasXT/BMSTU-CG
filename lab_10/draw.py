from tkinter import messagebox
from numpy import arange
from math import pi, sin, cos

from constants import *


trans_matrix = []


def clear_canvas(canvas):
    canvas.delete("all")


def set_trans_matrix():
    global trans_matrix

    trans_matrix.clear()

    for i in range(4):
        tmp_arr = []

        for j in range(4):
            tmp_arr.append(int(i == j))
            
        trans_matrix.append(tmp_arr)



def parse_funcs(func_num):
    if func_num == 0:
        func = lambda x, z: sin(x) * cos(z)
    elif func_num == 1:
        func = lambda x, z: sin(cos(x)) * sin(z)
    elif func_num == 2:
        func = lambda x, z: cos(x) * z / 4
    elif func_num == 3:
        func = lambda x, z: cos(x) * cos(sin(z))

    return func


def read_limits(x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry):
    try:
        x_0 = float(x_0_entry.get())
        x_1 = float(x_1_entry.get())
        x_2 = float(x_2_entry.get())

        x_limits = [x_0, x_1, x_2]

        z_0 = float(z_0_entry.get())
        z_1 = float(z_1_entry.get())
        z_2 = float(z_2_entry.get())

        z_limits = [z_0, z_1, z_2]
    
        return x_limits, z_limits
    except:
        return -1, -1


def rotate_matrix(matrix):
    global trans_matrix

    res_matrix = [[0 for i in range(4)] for j in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                res_matrix[i][j] += trans_matrix[i][k] * matrix[k][j]

    trans_matrix = res_matrix


def spin_x(x_spin_entry, canvas, RESULT_COLOUR, func_var,
           x_0_entry, x_1_entry, x_2_entry,
           z_0_entry, z_1_entry, z_2_entry):
    try:
        angle = float(x_spin_entry.get()) / 180 * pi
    except:
        messagebox.showerror("Ошибка", "Угол - число")
        return

    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    rotating_matrix = [[1, 0, 0, 0],
                       [0,  cos(angle), sin(angle), 0],
                       [0, -sin(angle), cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_graph(canvas, RESULT_COLOUR, func_var, 
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry)


def spin_y(y_spin_entry, canvas, RESULT_COLOUR, func_var,
           x_0_entry, x_1_entry, x_2_entry,
           z_0_entry, z_1_entry, z_2_entry):
        
    try:
        angle = float(y_spin_entry.get()) / 180 * pi
    except:
        messagebox.showerror("Ошибка", "Угол - число")
        return

    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    rotating_matrix = [[cos(angle), 0, -sin(angle), 0],
                       [0, 1, 0, 0],
                       [sin(angle), 0, cos(angle), 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_graph(canvas, RESULT_COLOUR, func_var, 
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry)


def spin_z(z_spin_entry, canvas, RESULT_COLOUR, func_var,
           x_0_entry, x_1_entry, x_2_entry,
           z_0_entry, z_1_entry, z_2_entry):
    try:
        angle = float(z_spin_entry.get()) / 180 * pi
    except:
        messagebox.showerror("Ошибка", "Угол - число")
        return

    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    rotating_matrix = [[ cos(angle), sin(angle), 0, 0],
                       [-sin(angle), cos(angle), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]]

    rotate_matrix(rotating_matrix)

    build_graph(canvas, RESULT_COLOUR, func_var,
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry)


def scale_graph(scale_entry, canvas, RESULT_COLOUR, func_var,
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry):
    try:
        scale_param = float(scale_entry.get())
    except:
        messagebox.showerror("Ошибка", "Коэффициент масштабирования должен быть числом")
        return

    if (len(trans_matrix) == 0):
        messagebox.showerror("Ошибка", "График не задан")
        return

    build_graph(canvas, RESULT_COLOUR, func_var, 
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry,
                False, scale_param)


def trans_dot(dot, scale_param):
    dot.append(1) 

    res_dot = [0, 0, 0, 0]

    for i in range(4):
        for j in range(4):
            res_dot[i] += dot[j] * trans_matrix[j][i]

    for i in range(3):
        res_dot[i] *= scale_param

    res_dot[0] += CANVAS_WIDTH  // 2
    res_dot[1] += CANVAS_HEIGHT // 2

    return res_dot[:3]


def is_visible(dot):
    return (0 <= dot[0] <= CANVAS_WIDTH) and \
           (0 <= dot[1] <= CANVAS_HEIGHT)

def draw_pixel(x, y, canvas, RESULT_COLOUR):
    canvas.create_line(x, y, x + 1, y + 1, fill = RESULT_COLOUR)


def draw_dot(x, y, high_horizon, low_horizon, canvas, RESULT_COLOUR):
    if (not is_visible([x, y])):
        return False

    x = int(x)
    y = int(y)

    if y > high_horizon[x]:
        high_horizon[x] = y
        draw_pixel(x, y, canvas, RESULT_COLOUR)

    elif y < low_horizon[x]:
        low_horizon[x] = y
        draw_pixel(x, y, canvas, RESULT_COLOUR)

    return True


def draw_horizon_part(dot1, dot2, high_horizon, low_horizon, canvas, RESULT_COLOUR):
    if (dot1[0] > dot2[0]):
        dot1, dot2 = dot2, dot1

    dx = dot2[0] - dot1[0]
    dy = dot2[1] - dot1[1]

    if (dx > dy):
        l = dx
    else:
        l = dy

    dx /= l
    dy /= l

    x = dot1[0]
    y = dot1[1]

    for _ in range(int(l) + 1):
        if not draw_dot(round(x), y, high_horizon, low_horizon, canvas, RESULT_COLOUR):
            return

        x += dx
        y += dy


def draw_horizon(function, high_horizon, low_horizon, limits, z, scale_param, canvas, RESULT_COLOUR):
    f = lambda x: function(x, z)

    prev = None

    for x in arange(limits[0], limits[1] + limits[2], limits[2]):
        cur = trans_dot([x, f(x), z], scale_param)

        if (prev):
            draw_horizon_part(prev, cur, high_horizon, low_horizon, canvas, RESULT_COLOUR)

        prev = cur


def draw_horizon_limits(f, x_limits, z_limits, scale_param, canvas, RESULT_COLOUR):
    for z in arange(z_limits[0], z_limits[1] + z_limits[2], z_limits[2]):
        dot1 = trans_dot([x_limits[0], f(x_limits[0], z), z], scale_param)
        dot2 = trans_dot([x_limits[0], f(x_limits[0], z + x_limits[2]), z + x_limits[2]], scale_param)

        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill = RESULT_COLOUR)

        dot1 = trans_dot([x_limits[1], f(x_limits[1], z), z], scale_param)
        dot2 = trans_dot([x_limits[1], f(x_limits[1], z + x_limits[2]), z + x_limits[2]], scale_param)

        canvas.create_line(dot1[0], dot1[1], dot2[0], dot2[1], fill = RESULT_COLOUR)


def build_graph(canvas, RESULT_COLOUR, func_var, 
                x_0_entry, x_1_entry, x_2_entry,
                z_0_entry, z_1_entry, z_2_entry, 
                new_graph = False, scale_param = DEFAULT_SCALE):
                
    clear_canvas(canvas)

    if (new_graph):
        set_trans_matrix()

    f = parse_funcs(func_var.get())
    x_limits, z_limits = read_limits(x_0_entry, x_1_entry, x_2_entry,
                                     z_0_entry, z_1_entry, z_2_entry)

    high_horizon = [0 for i in range(CANVAS_WIDTH + 1)]
    low_horizon = [CANVAS_HEIGHT for i in range(CANVAS_WIDTH + 1)]

    #  Горизонт
    for z in arange(z_limits[0], z_limits[1] + z_limits[2], z_limits[2]):
        draw_horizon(f, high_horizon, low_horizon, x_limits, z, scale_param, canvas, RESULT_COLOUR)

    # Границы горизонта
    draw_horizon_limits(f, x_limits, z_limits, scale_param, canvas, RESULT_COLOUR)