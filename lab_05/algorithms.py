from dataclasses import dataclass
import time
from constants import *

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

@dataclass
class Node:
    x: float
    dx: float
    dy: int

    def __init__(self, x=0, dx=0, dy=0):
        self.x = x
        self.dx = dx
        self.dy = dy


def draw_line(canvas, ps, pe, colour):
    x_beg = ps.x + 0.5
    x_end = pe.x + 0.5
    y = ps.y
    canvas.create_line(x_beg, y, x_end, y, fill=colour)


def draw_edges(canvas, edges):
    for i in range(len(edges)):
        canvas.create_line(edges[i][0].x, edges[i][0].y,
                           edges[i][1].x, edges[i][1].y, fill="black")


def make_edges_list(figures):
    edges = list()
    for fig in figures:
        amount_point = len(fig)
        for i in range(amount_point):
            if i + 1 > amount_point - 1:
                edges.append([fig[-1], fig[0]])
            else:
                edges.append([fig[i], fig[i + 1]])

    return edges


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def find_extrimum_Y_figures(figures):
    yMin = figures[0][0].y
    yMax = figures[0][0].y
    for fig in figures:
        for p in fig:
            if p.y > yMax:
                yMax = p.y
            if p.y < yMin:
                yMin = p.y
    return yMin, yMax


def bubble_sort_y(pointList):
    for i in range(len(pointList)):
        for j in range(i + 1, len(pointList)):
            if pointList[i].y < pointList[j].y:
                pointList[i], pointList[j] = pointList[j], pointList[i]


def sort_x_in_y(pointList):
    for i in range(len(pointList)):
        for j in range(i + 1, len(pointList)):
            if pointList[i].x > pointList[j].x and pointList[i].y == pointList[j].y:
                pointList[i], pointList[j] = pointList[j], pointList[i]


def simple_algorithm_with_ordered_list_of_edges(canvas, polygon, colour, delay=False):
    edges = make_edges_list(polygon)

    ins = dda_find_insertion(edges)
    ins.sort(key=lambda point: point.y, reverse=True)
    sort_x_in_y(ins)

    for i in range(0, len(ins), 2):
        draw_line(canvas, ins[i], ins[i + 1], colour)
        if delay:
            time.sleep(0.00001)
            canvas.update()
    draw_edges(canvas, edges)


def dda_find_insertion(edges):
    intersections = []
    for edge in edges:
        x1 = edge[0].x
        y1 = edge[0].y
        x2 = edge[1].x
        y2 = edge[1].y

        len_x = abs(int(x2) - int(x1))
        len_y = abs(int(y2) - int(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            x1 += dx / 2
            y1 += dy / 2

            for j in range(len_y):
                intersections.append(Point(x1, y1))
                x1 += dx
                y1 += dy

    return intersections


def make_y_groups(Ymin=0, Ymax=CANVAS_HEIGHT):
    y_group = dict()
    for i in range(round(Ymax), round(Ymin), -1):
        y_group.update({i - 0.5: list()})
    return y_group


def dda_update_y_group(edges, y_groups):
    for edge in edges:
        x1 = edge[0].x
        y1 = edge[0].y
        x2 = edge[1].x
        y2 = edge[1].y

        len_x = abs(int(x2) - int(x1))
        len_y = abs(int(y2) - int(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            x1 += dx / 2
            y1 += dy / 2

            for j in range(len_y):
                sotYdr = y_groups.get(y1)
                sotYdr.append(x1)
                x1 += dx
                y1 += dy


def draw_all_ygroups(canvas, y_groups, colour, delay=False):
    for yValue in y_groups:
        draw_Y_group(canvas, yValue, y_groups.get(yValue), colour)
        if delay:
            time.sleep(0.0001)
            canvas.update()


def draw_Y_group(canvas, y, y_group, colour):
    for i in range(0, len(y_group), 2):
        canvas.create_line(y_group[i] + 0.5, y, y_group[i + 1] + 0.5, y, fill=colour)


def y_group_algorithm_with_ordered_list_of_edges(canvas, polygon, colour="black", delay=False):
    edges = make_edges_list(polygon)

    ymin, ymax = find_extrimum_Y_figures(polygon)
    y_groups = make_y_groups(ymin, ymax)
    dda_update_y_group(edges, y_groups)

    for yValue in y_groups:
        y_group = y_groups.get(yValue)
        y_group.sort()

    draw_all_ygroups(canvas, y_groups, colour, delay)
    draw_edges(canvas, edges)


def make_link_list(Ymin=0, Ymax=CANVAS_WIDTH):
    link_list = dict()
    for i in range(round(Ymax), round(Ymin), -1):
        link_list.update({i: list()})
    return link_list


def make_insert_thm(edges, link_list):
    for edge in edges:
        x1 = edge[0].x
        y1 = edge[0].y
        x2 = edge[1].x
        y2 = edge[1].y

        len_x = abs(int(x2) - int(x1))
        len_y = abs(int(y2) - int(y1))

        if len_y != 0:
            dx = ((x2 > x1) - (x2 < x1)) * len_x / len_y
            dy = ((y2 > y1) - (y2 < y1))

            nmax = max(y1, y2)

            x = x1 + dx / 2
            y = y2 + dy / 2

            for j in range(len_y):
                sotYdr = link_list.get(nmax)
                sotYdr.append(Node(x1))
                x += dx
                y += dy


def update_y_group(y_groups, x_start, y_start, x_end, y_end):
        if y_start > y_end:
            x_end, x_start = x_start, x_end
            y_end, y_start = y_start, y_end

        y_proj = abs(y_end - y_start)
        if y_proj != 0:
            x_step = -(x_end - x_start) / y_proj
            if y_end not in y_groups:
                y_groups[y_end] = [Node(x_end, x_step, y_proj)]
            else:
                y_groups[y_end].append(Node(x_end, x_step, y_proj))


def iterator_active_edges(active_edges):
    i = 0
    while i < len(active_edges):
        active_edges[i].x += active_edges[i].dx
        active_edges[i].dy -= 1
        if active_edges[i].dy < 1:
            active_edges.pop(i)
        else:
            i += 1


def add_active_edges(y_groups, active_edges, y):
    if y in y_groups:
        for y_group in y_groups.get(y):
            active_edges.append(y_group)
    active_edges.sort(key=lambda edge: edge.x)


def draw_act(canvas, active_edges, y, colour):
    len_edge = len(active_edges)
    for i in range(0, len_edge, 2):
        try:
            canvas.create_line(active_edges[i].x, y, active_edges[i + 1].x, y, fill=colour)
        except:
            canvas.create_line(active_edges[i].x, y, active_edges[i - 1].x, y, fill=colour)


def CAP_algorithm_with_ordered_list_of_edges(canvas, polygon, colour="black", delay=False):
    edges = make_edges_list(polygon)

    ymin, ymax = find_extrimum_Y_figures(polygon)
    y_groups = make_link_list(ymin, ymax)
        
    for edge in edges:
        update_y_group(y_groups, edge[0].x, edge[0].y, edge[1].x, edge[1].y)

    y_end = ymax
    y_start = ymin
    active_edges = []
    while y_end > y_start:
        iterator_active_edges(active_edges)
        add_active_edges(y_groups, active_edges, y_end)
        e = 1
        for i in active_edges:
            e += 1
        draw_act(canvas, active_edges, y_end, colour)
        y_end -= 1
        if delay:
            time.sleep(0.00001)
            canvas.update()
    draw_edges(canvas, edges)