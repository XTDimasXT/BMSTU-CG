import tkinter as tk
from tkinter import colorchooser

from constants import *
from commands import clear_canvas, click_btn, close_figure, add_vertex, cut_off, show_info

root = tk.Tk()
root.title("Лабораторная работа №9. Реализация алгоритма отсечения произвольного многоугольника выпуклым отсекателем")
root["bg"] = MAIN_COLOUR

root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.resizable(height=False, width=False)

figure = []
clipper = []

dataFrame = tk.Frame(root, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT)
dataFrame["bg"] = MAIN_FRAME_COLOR

dataFrame.pack(side=tk.LEFT, padx=BORDERS_SPACE, fill=tk.Y)


chooseColourMainLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

size = (DATA_FRAME_WIGHT // 1.7) // 8
chooseColourMainLabel.place(x=0, y=0, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

lineColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет фигуры:", font=("Consolas", 13), fg=MAIN_COLOUR_LABEL_TEXT)


def get_colour_line():
    color_code = colorchooser.askcolor(title="Choose colour line")
    set_linecolour(color_code[-1])


def set_linecolour(color):
    global FIGURE_COLOUR
    FIGURE_COLOUR = color


whiteLine = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_linecolour("white"))
yellowLine = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_linecolour("yellow"))
orangeLine = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_linecolour("orange"))
redLine = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_linecolour("red"))
purpleLine = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_linecolour("purple"))
greenLine = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_linecolour("green"))
darkGreenLine = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen", command=lambda: set_linecolour("darkgreen"))
lightBlueLine = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_linecolour("lightblue"))

lineColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет фигуры', font=("Consolas", 11), command=get_colour_line)

yColourLine = 1.2
lineColourLabel.place(x=5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

whiteLine.place(x=DATA_FRAME_WIGHT // 2.5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
yellowLine.place(x=DATA_FRAME_WIGHT // 2.5 + size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
orangeLine.place(x=DATA_FRAME_WIGHT // 2.5 + 2 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
redLine.place(x=DATA_FRAME_WIGHT // 2.5 + 3 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
purpleLine.place(x=DATA_FRAME_WIGHT // 2.5 + 4 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
greenLine.place(x=DATA_FRAME_WIGHT // 2.5 + 5 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
darkGreenLine.place(x=DATA_FRAME_WIGHT // 2.5 + 6 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
lightBlueLine.place(x=DATA_FRAME_WIGHT // 2.5 + 7 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)

lineColourBtn.place(x=DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.5, height=DATA_FRAME_HEIGHT // COLUMNS)

clipperColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет отсекателя:", font=("Consolas", 13), fg=MAIN_COLOUR_LABEL_TEXT)


def get_colour_clipper():
    color_code = colorchooser.askcolor(title="Choose colour clipper")
    set_clippercolour(color_code[-1])


def set_clippercolour(color):
    global CLIPPER_COLOUR
    CLIPPER_COLOUR = color

whiteClipper = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_clippercolour("white"))
yellowClipper = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_clippercolour("yellow"))
orangeClipper = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_clippercolour("orange"))
redClipper = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_clippercolour("red"))
purpleClipper = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_clippercolour("purple"))
greenClipper = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_clippercolour("green"))
darkGreenClipper = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen", command=lambda: set_clippercolour("darkgreen"))
lightBlueClipper = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_clippercolour("lightblue"))

clipperColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет отсекателя', font=("Consolas", 11), command=get_colour_clipper)

yColourLine += 3
clipperColourLabel.place(x=5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

whiteClipper.place(x=DATA_FRAME_WIGHT // 2.5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
yellowClipper.place(x=DATA_FRAME_WIGHT // 2.5 + size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
orangeClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 2 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
redClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 3 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
purpleClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 4 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
greenClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 5 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
darkGreenClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 6 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
lightBlueClipper.place(x=DATA_FRAME_WIGHT // 2.5 + 7 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)

clipperColourBtn.place(x=DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.5, height=DATA_FRAME_HEIGHT // COLUMNS)

resultColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет результата:", font=("Consolas", 13), fg=MAIN_COLOUR_LABEL_TEXT)

def get_colour_result():
    color_code = colorchooser.askcolor(title="Choose colour result")
    set_resultcolour(color_code[-1])


def set_resultcolour(color):
    global RESULT_COLOUR
    RESULT_COLOUR = color

whiteResult = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_resultcolour("white"))
yellowResult = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_resultcolour("yellow"))
orangeResult = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_resultcolour("orange"))
redResult = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_resultcolour("red"))
purpleResult = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_resultcolour("purple"))
greenResult = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_resultcolour("green"))
darkGreenResult = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen", command=lambda: set_resultcolour("darkgreen"))
lightBlueResult = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_resultcolour("lightblue"))

resultColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет результата', font=("Consolas", 11), command=get_colour_result)

yColourLine += 3
resultColourLabel.place(x=5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

whiteResult.place(x=DATA_FRAME_WIGHT // 2.5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
yellowResult.place(x=DATA_FRAME_WIGHT // 2.5 + size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
orangeResult.place(x=DATA_FRAME_WIGHT // 2.5 + 2 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
redResult.place(x=DATA_FRAME_WIGHT // 2.5 + 3 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
purpleResult.place(x=DATA_FRAME_WIGHT // 2.5 + 4 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
greenResult.place(x=DATA_FRAME_WIGHT // 2.5 + 5 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
darkGreenResult.place(x=DATA_FRAME_WIGHT // 2.5 + 6 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
lightBlueResult.place(x=DATA_FRAME_WIGHT // 2.5 + 7 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)

resultColourBtn.place(x=DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.5, height=DATA_FRAME_HEIGHT // COLUMNS)


pointMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ФИГУРЫ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutPoint = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="X\t\tY", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

xFigureEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
yFigureEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

drawFigureVertexBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить вершину", font=("Consolas", 13), command=lambda: add_vertex(canvasField, clipper, figure, CLIPPER_COLOUR, FIGURE_COLOUR, xFigureEntry, yFigureEntry))
drawFigureCloseBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Замкнуть фигуру", font=("Consolas", 13), command=lambda: close_figure(canvasField, figure, FIGURE_COLOUR, "Фигура"))

makePoint = yColourLine + 3.1
pointMakeLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutPoint.place(x=0, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xFigureEntry.place(x=10,                         y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
yFigureEntry.place(x=DATA_FRAME_WIGHT // 2, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)

makePoint += 0.2
drawFigureVertexBtn.place(x=10, y=(makePoint + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
drawFigureCloseBtn.place(x=DATA_FRAME_WIGHT // 2, y=(makePoint + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)


clipperMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОТСЕКАТЕЛЯ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutClipper = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="X\t\tY", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

xclEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
yclEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

drawClipperVertexBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Построить вершину", font=("Consolas", 13), command=lambda: add_vertex(canvasField, figure, clipper, FIGURE_COLOUR, CLIPPER_COLOUR, xclEntry, yclEntry))
drawClipperCloseBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Замкнуть отсекатель", font=("Consolas", 13), command=lambda: close_figure(canvasField, clipper, CLIPPER_COLOUR, "Отсекатель"))

makeClipper = makePoint + 4.1
clipperMakeLabel.place(x=0, y=makeClipper * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutClipper.place(x=0, y=(makeClipper + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xclEntry.place(x=10,                         y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
yclEntry.place(x=1 * DATA_FRAME_WIGHT // 2, y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)

makeClipper += 0.2
drawClipperVertexBtn.place(x=10, y=(makeClipper + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
drawClipperCloseBtn.place(x=DATA_FRAME_WIGHT // 2, y=(makeClipper + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)

modeMouse = makeClipper + 2.2

currentFigure = []
allFigures = []

canvasField = tk.Canvas(root, bg=CANVAS_COLOUR, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvasField.pack(side=tk.RIGHT, padx=BORDERS_SPACE)

canvasField.bind("<Button-1>", lambda event: click_btn(event, figure, clipper, canvasField, CLIPPER_COLOUR, FIGURE_COLOUR))
canvasField.bind("<Button-3>", lambda event: click_btn(event, clipper, figure, canvasField, FIGURE_COLOUR, CLIPPER_COLOUR))


cutBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Отсечь", font=("Consolas", 14), command=lambda: cut_off(canvasField, figure, clipper, RESULT_COLOUR))
clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=lambda: clear_canvas(canvasField, figure, clipper))
infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14), command=show_info)

cutBtn.place(x=40, y=(modeMouse + 5) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)
clearCanvasBtn.place(x=40, y=(modeMouse + 6) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)
infoBtn.place(x=40, y=(modeMouse + 7) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)

xFigureEntry.insert(0, 100)
yFigureEntry.insert(0, 200)

xclEntry.insert(0, 200)
yclEntry.insert(0, 100)

root.mainloop()