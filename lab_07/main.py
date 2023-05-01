import tkinter as tk
from tkinter import colorchooser, messagebox

from constants import *
from draw import add_line, draw_rectangle, click_right, draw_rectangle_by_Button

root = tk.Tk()
root.title("Лабораторная работа №7. Реализация алгоритма отсечения отрезка регулярным отсекателем")
root["bg"] = MAIN_COLOUR

root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.resizable(height=False, width=False)

lines = []
rectangle = [-1, -1, -1, -1]
is_set_rectangle = False

def click_left_motion(event):
    global is_set_rectangle
    is_set_rectangle = draw_rectangle_by_Button(event, rectangle, lines, canvasField, CLIPPER_COLOUR, is_set_rectangle)


def clear_canvas():
    global is_set_rectangle
    canvasField.delete("all")
    lines.clear()
    is_set_rectangle = False
    for i in range(4):
        rectangle[i] = -1


def show_info():
    messagebox.showinfo('Информация о программе',
                        'Автор программы - Писаренко Дмитрий ИУ7-44Б.\n'
                        'С помощью данной программы можно исследовать алгоритм отсечения отрезка одним из способов.\n'
                        'Для отсечения используется алгоритм Сазерленда-Коэна.\n'
                        '========Инструкции для пользователя:========\n'
                        'С помощью левой кнопки мыши мы добавляем отсекатель (прямоугольник), с помощью правой - добавляем отрезок.\n')



dataFrame = tk.Frame(root, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT)
dataFrame["bg"] = MAIN_FRAME_COLOR

dataFrame.pack(side=tk.LEFT, padx=BORDERS_SPACE, fill=tk.Y)

chooseColourMainLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА",
                     font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

size = (DATA_FRAME_WIGHT // 1.7) // 8
chooseColourMainLabel.place(x=0, y=0, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

lineColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет отрезка:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)


def get_colour_line():
    color_code = colorchooser.askcolor(title="Choose colour line")
    set_linecolour(color_code[-1])


def set_linecolour(color):
    global LINE_COLOUR
    LINE_COLOUR = color


whiteLine = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_linecolour("white"))
yellowLine = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_linecolour("yellow"))
orangeLine = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_linecolour("orange"))
redLine = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_linecolour("red"))
purpleLine = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_linecolour("purple"))
greenLine = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_linecolour("green"))
darkGreenLine = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen", command=lambda: set_linecolour("darkgreen"))
lightBlueLine = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_linecolour("lightblue"))

lineColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет отрезка', font=("Consolas", 14), command=get_colour_line)

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

clipperColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет отсекателя:", font=("Consolas", 15), fg=MAIN_COLOUR_LABEL_TEXT)


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

clipperColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет отсекателя', font=("Consolas", 14), command=get_colour_clipper)

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

resultColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет результата:", font=("Consolas", 15), fg=MAIN_COLOUR_LABEL_TEXT)


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
lightBlueResult = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue",command=lambda: set_resultcolour("lightblue"))

resultColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет результата', font=("Consolas", 14), command=get_colour_result)

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


pointMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОТРЕЗКА", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutPoint = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Xн        Yн       Xк        Yк", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

xnEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ynEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
xkEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ykEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")


makePoint = yColourLine + 3.1
pointMakeLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutPoint.place(x=0, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xnEntry.place(x=5,                         y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 5, height=DATA_FRAME_HEIGHT // COLUMNS)
ynEntry.place(x=1 * DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
xkEntry.place(x=2 * DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
ykEntry.place(x=3 * DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 5, height=DATA_FRAME_HEIGHT // COLUMNS)

makePoint += 0.2


clipperMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОТСЕКАТЕЛЯ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutClipper = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Xлв       Yлв      Xпн        Yпн", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

xlbEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ylbEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
xrlEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
yrlEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

makeClipper = makePoint + 4.1
clipperMakeLabel.place(x=0, y=makeClipper * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutClipper.place(x=0, y=(makeClipper + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xlbEntry.place(x=5,                         y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 5, height=DATA_FRAME_HEIGHT // COLUMNS)
ylbEntry.place(x=1 * DATA_FRAME_WIGHT // 4, y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
xrlEntry.place(x=2 * DATA_FRAME_WIGHT // 4, y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
yrlEntry.place(x=3 * DATA_FRAME_WIGHT // 4, y=(makeClipper + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 5, height=DATA_FRAME_HEIGHT // COLUMNS)

makeClipper += 0.2

modeByMouse = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ С ПОМОЩЬЮ МЫШИ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
modeMouse = makeClipper + 4 + 0.2
modeByMouse.place(x=0, y=modeMouse * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

currentFigure = []
allFigures = []

canvasField = tk.Canvas(root, bg=CANVAS_COLOUR, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvasField.pack(side=tk.RIGHT, padx=BORDERS_SPACE)

canvasField.bind("<Button-3>", lambda event: click_right(event, lines, canvasField, LINE_COLOUR))
canvasField.bind("<B1-Motion>", lambda event: click_left_motion(event))


clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=clear_canvas)
infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14), command=show_info)

clearCanvasBtn.place(x=40, y=(modeMouse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)
infoBtn.place(x=40, y=(modeMouse + 5) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)

xnEntry.insert(0, 100)
ynEntry.insert(0, 200)
xkEntry.insert(0, 800)
ykEntry.insert(0, 500)

xlbEntry.insert(0, 200)
ylbEntry.insert(0, 100)

xrlEntry.insert(0, 700)
yrlEntry.insert(0, 600)

root.mainloop()