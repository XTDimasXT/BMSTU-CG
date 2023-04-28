import tkinter as tk
from tkinter import colorchooser, messagebox
from constants import *
import time

root = tk.Tk()
root.title("Лабораторная работа №5. Реализация и исследование алгоритмов растрового заполнения сплошных областей")
root["bg"] = MAIN_COLOUR

root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.resizable(height=False, width=False)

def clearScreen():
    allFigures.clear()
    currentFigure.clear()
    listPoint_scroll.delete(0, tk.END)
    canvasField.delete("all")


dataFrame = tk.Frame(root, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT)
dataFrame["bg"] = MAIN_FRAME_COLOR

dataFrame.pack(side=tk.LEFT, padx=BORDERS_SPACE, fill=tk.Y)

chooseColourMainLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА ЗАКРАСКИ",
                     font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

size = (DATA_FRAME_WIGHT // 1.6) // 8
chooseColourMainLabel.place(x=0, y=0, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

lineColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет:",
                     font=("Consolas", 16),
                     fg=MAIN_COLOUR_LABEL_TEXT)

lineCurColourLabel = tk.Label(dataFrame, bg="black")


def get_colour_line():
    color_code = colorchooser.askcolor(title="Choose colour line")
    set_linecolour(color_code[-1])


def set_linecolour(color):
    global LINE_COLOUR
    LINE_COLOUR = color
    lineCurColourLabel.constantsure(bg=LINE_COLOUR)


whiteLine = tk.Button(dataFrame, bg="white", activebackground="white",
                    command=lambda: set_linecolour("white"))
yellowLine = tk.Button(dataFrame, bg="yellow", activebackground="yellow",
                     command=lambda: set_linecolour("yellow"))
orangeLine = tk.Button(dataFrame, bg="orange", activebackground="orange",
                     command=lambda: set_linecolour("orange"))
redLine = tk.Button(dataFrame, bg="red", activebackground="red",
                  command=lambda: set_linecolour("red"))
purpleLine = tk.Button(dataFrame, bg="purple", activebackground="purple",
                     command=lambda: set_linecolour("purple"))
greenLine = tk.Button(dataFrame, bg="green", activebackground="green",
                    command=lambda: set_linecolour("green"))
darkGreenLine = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen",
                        command=lambda: set_linecolour("darkgreen"))
lightBlueLine = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue",
                        command=lambda: set_linecolour("lightblue"))

lineColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой', font=("Consolas", 14), command=get_colour_line)

yColourLine = 1.2
lineColourLabel.place(x=5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 3, height=DATA_FRAME_HEIGHT // COLUMNS)

whiteLine.pack(anchor=tk.NW, padx=BORDERS_SPACE)
whiteLine.place(x=DATA_FRAME_WIGHT // 3, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
yellowLine.place(x=DATA_FRAME_WIGHT // 3 + size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
orangeLine.place(x=DATA_FRAME_WIGHT // 3 + 2 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
redLine.place(x=DATA_FRAME_WIGHT // 3 + 3 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
purpleLine.place(x=DATA_FRAME_WIGHT // 3 + 4 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
greenLine.place(x=DATA_FRAME_WIGHT // 3 + 5 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
darkGreenLine.place(x=DATA_FRAME_WIGHT // 3 + 6 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
lightBlueLine.place(x=DATA_FRAME_WIGHT // 3 + 7 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)

lineColourBtn.place(x=DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.5, height=DATA_FRAME_HEIGHT // COLUMNS)


modeMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="РЕЖИМ ЗАКРАСКИ",
                         font=("Consolas", 16),
                         fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

modeDraw = yColourLine + 3.1
methodDraw = tk.IntVar()
methodDraw.set(1)
modeMakeLabel.place(x=0, y=modeDraw * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
tk.Radiobutton(dataFrame, variable=methodDraw, text="С задержкой", value=0, bg=MAIN_FRAME_COLOR,
                font=("Consolas", 16), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="purple",
                activebackground=MAIN_FRAME_COLOR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
               ).place(x=10, y=(modeDraw + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 2 * BORDERS_SPACE,
                       height=DATA_FRAME_HEIGHT // COLUMNS)
tk.Radiobutton(dataFrame, variable=methodDraw, text="Без задержки", value=1, bg=MAIN_FRAME_COLOR,
                font=("Consolas", 16), justify=tk.LEFT, fg=MAIN_COLOUR_LABEL_TEXT, selectcolor="purple",
                activebackground=MAIN_FRAME_COLOR, activeforeground=MAIN_COLOUR_LABEL_TEXT,
               ).place(x=DATA_FRAME_WIGHT // 2, y=(modeDraw + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2 - 2 * BORDERS_SPACE,
                       height=DATA_FRAME_HEIGHT // COLUMNS)


pointMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ТОЧКИ",
                          font=("Consolas", 16),
                          fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutPoint = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="X       Y",
                         font=("Consolas", 16),
                         fg=MAIN_COLOUR_LABEL_TEXT)

xEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_BG, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")
yEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_BG, font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT, justify="center")


makePoint = modeDraw + 2.1
pointMakeLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutPoint.place(x=0, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xEntry.place(x=DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
yEntry.place(x=2 * DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)

makePoint += 0.2

listPoint_scroll = tk.Listbox(font=("Consolas", 14))
makePoint += 0.4
listPoint_scroll.place(x=40, y=(makePoint + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 60, height=6 * DATA_FRAME_HEIGHT // COLUMNS)

modeMouse = makePoint + 10 + 0.2


def show_info():
    messagebox.showinfo('Информация о программе',
                        'Автор программы - Писаренко Дмитрий ИУ7-44Б.\n'
                        'С помощью данной программы можно построить фигуру и закрасить ее.\n'
                        'Для построения закраски фигуры используется алгоритм с упорядоченным списоком ребер и его реализация САР (список активных ребер).\n'
                        '========Инструкции для пользователя:========\n'
                        'С помощью левой кнопки мыши мы добавляем точку, с помощью правой - замыкаем фигуру.\n')


currentFigure = []
allFigures = []

canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
canvasField.place(x=WINDOW_WIDTH * DATA_SITUATION + BORDERS_SPACE, y=BORDERS_SPACE, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)


timeLabel = tk.Label(root, bg="gray", text="Время закраски: ",
                             font=("Consolas", 16),
                             fg=MAIN_COLOUR_LABEL_TEXT)
clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=clearScreen)
infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14),
                    command=show_info)

timeLabel.place(x=DATA_FRAME_WIGHT + 2 * BORDERS_SPACE, y=CANVAS_HEIGHT + BORDERS_SPACE - DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 60, height=DATA_FRAME_HEIGHT // COLUMNS)
clearCanvasBtn.place(x=40, y=(modeMouse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)
infoBtn.place(x=40, y=(modeMouse + 5) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)

root.mainloop()