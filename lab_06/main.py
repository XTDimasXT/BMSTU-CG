import tkinter as tk
from tkinter import colorchooser, messagebox
from constants import *
import time

root = tk.Tk()
root.title("Лабораторная работа №6. Реализация и исследование алгоритма построчного затравочного заполнения сплошных областей")
root["bg"] = MAIN_COLOUR

root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
root.resizable(height=False, width=False)


def clearScreen():
    allFigures.clear()
    currentFigure.clear()
    listPoint_scroll.delete(0, tk.END)
    canvasField.delete("all")
    canvasImg.put(CANVAS_COLOUR, to=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))
    canvasField.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=canvasImg, state="normal")


dataFrame = tk.Frame(root, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT)
dataFrame["bg"] = MAIN_FRAME_COLOR

dataFrame.pack(side=tk.LEFT, padx=BORDERS_SPACE, fill=tk.Y)

listFrame = tk.Frame(root, width=LIST_FRAME_WIGHT, height=LIST_FRAME_HEIGHT)
listFrame["bg"] = MAIN_FRAME_COLOR

listLabel = tk.Label(listFrame, bg=MAIN_COLOUR_LABEL_BG, text="Список точек", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

listPoint_scroll = tk.Listbox(listFrame, font=("Consolas", 14))

listLabel.place(x=0, y=0, width=LIST_FRAME_WIGHT, height=LIST_FRAME_HEIGHT // COLUMNS)
listPoint_scroll.place(x=0, y=LIST_FRAME_HEIGHT // COLUMNS * 1.2, width=LIST_FRAME_WIGHT, height=LIST_FRAME_HEIGHT - LIST_FRAME_HEIGHT // COLUMNS)
listFrame.pack(side=tk.RIGHT, padx=BORDERS_SPACE, fill=tk.Y)

chooseColourMainLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА ЗАКРАСКИ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

size = (DATA_FRAME_WIGHT // 1.6) // 8
chooseColourMainLabel.place(x=0, y=0, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)


borderColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет границы:", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)
fillColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет закраски:", font=("Consolas", 13), fg=MAIN_COLOUR_LABEL_TEXT)

borderCurColourLabel = tk.Label(dataFrame, bg=BORDER_COLOUR)
fillCurColourLabel = tk.Label(dataFrame, bg=FILL_COLOUR)


def get_colour(mode):
    global BORDER_COLOUR, FILL_COLOUR, CANVAS_COLOUR
    if mode == "border":
        colour_code = colorchooser.askcolor(title="Выбрать цвет границы!")
        colour = colour_code[-1]
        BORDER_COLOUR = colour
        borderCurColourLabel.configure(bg=colour)
    if mode == "fill":
        colour_code = colorchooser.askcolor(title="Выбрать цвет закраски!")
        colour = colour_code[-1]
        FILL_COLOUR = colour
        fillCurColourLabel.configure(bg=colour)


borderColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать цвет гр-цы', font=("Consolas", 13), command=lambda: get_colour("border"))
fillColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать цвет закр-ки', font=("Consolas", 13), command=lambda: get_colour("fill"))

yColourLine = 1.2
borderColourLabel.place(x=0, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)
fillColourLabel.place(x=0, y=(yColourLine + 1.1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)


borderColourBtn.place(x=1.5 * DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2, height=DATA_FRAME_HEIGHT // COLUMNS)
fillColourBtn.place(x=1.5 * DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1.1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2, height=DATA_FRAME_HEIGHT // COLUMNS)


borderCurColourLabel.place(x=DATA_FRAME_WIGHT // 3 + BORDERS_SPACE, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS + 5, width=DATA_FRAME_WIGHT // 9, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
fillCurColourLabel.place(x=DATA_FRAME_WIGHT // 3 + BORDERS_SPACE, y=(yColourLine + 1.1) * DATA_FRAME_HEIGHT // COLUMNS + 5, width=DATA_FRAME_WIGHT // 9, height=DATA_FRAME_HEIGHT // COLUMNS - 10)


modeMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="РЕЖИМ ЗАКРАСКИ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

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


pointMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ЛИНИИ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)

msgAboutPoint = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="X       Y", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

xEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
yEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

makePoint = modeDraw + 2.1
pointMakeLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
msgAboutPoint.place(x=0, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

xEntry.place(x=DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
yEntry.place(x=2 * DATA_FRAME_WIGHT // 4, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)

makePoint += 0.2

modeMouse = makePoint + 1

lineMakeLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ПОСТРОЕНИЕ ОКРУЖНОСТИ ИЛИ ЭЛЛИПСА", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
lineMakeCircle = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="ОКРУЖНОСТЬ", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)
lineMakeEllipse = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="ЭЛЛИПС", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)

argumnetsCenterLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Коорд. центра:     Xс         Yс                  ",
                     font=("Consolas", 13),  justify="right",
                     fg=MAIN_COLOUR_LABEL_TEXT)

radiusCircleLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Радиус (R):", font=("Consolas", 13),  justify="center", fg=MAIN_COLOUR_LABEL_TEXT)
widthEllipseLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Высота (Ry):", font=("Consolas", 13),  justify="center", fg=MAIN_COLOUR_LABEL_TEXT)
heightEllipseLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Ширина (Rx):", font=("Consolas", 13),  justify="center", fg=MAIN_COLOUR_LABEL_TEXT)

xcEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ycEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
rEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
rxEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
ryEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

makeCircleOREllipse = modeMouse + 5.2
lineMakeLabel.place(x=0, y=makeCircleOREllipse * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
argumnetsCenterLabel.place(x=0, y=(makeCircleOREllipse + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)
xcEntry.place(x=DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
ycEntry.place(x=2 * DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)

lineMakeCircle.place(x=0, y=(makeCircleOREllipse + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2, height=DATA_FRAME_HEIGHT // COLUMNS)
lineMakeEllipse.place(x=DATA_FRAME_WIGHT // 2, y=(makeCircleOREllipse + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2, height=DATA_FRAME_HEIGHT // COLUMNS)

radiusCircleLabel.place(x=0, y=(makeCircleOREllipse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4, height=DATA_FRAME_HEIGHT // COLUMNS)
rEntry.place(x=DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 20, height=DATA_FRAME_HEIGHT // COLUMNS)

heightEllipseLabel.place(x=10 + 2 * DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
widthEllipseLabel.place(x=10 + 2 * DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 5) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 10, height=DATA_FRAME_HEIGHT // COLUMNS)
rxEntry.place(x=10 + 3 * DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 4) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 20, height=DATA_FRAME_HEIGHT // COLUMNS)
ryEntry.place(x=10 + 3 * DATA_FRAME_WIGHT // 4, y=(makeCircleOREllipse + 5) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 4 - 20, height=DATA_FRAME_HEIGHT // COLUMNS)


def show_info():
    messagebox.showinfo('Информация',
                        'С помощью данной программы можно построить фигуру и закрасить ее:\n'
                        '\nДля построения закраски фигуры используется алгоритм с упорядоченным списоком ребер \n'
                        'и его реализация САР(список активных ребер).\n')

currentFigure = []
allFigures = []
seed_pixels = []

canvasField = tk.Canvas(root, bg=CANVAS_COLOUR)
canvasField.place(x=WINDOW_WIDTH * DATA_SITUATION + BORDERS_SPACE, y=BORDERS_SPACE, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

canvasImg = tk.PhotoImage(width=CANVAS_WIDTH + 1, height=CANVAS_HEIGHT + 1)
canvasField.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=canvasImg, state="normal")
canvasImg.put(CANVAS_COLOUR, to=(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT))


timeLabel = tk.Label(root, bg="gray", text="Время закраски: ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
clearCanvasBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Очистить экран", font=("Consolas", 14), command=clearScreen)
infoBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text="Справка", font=("Consolas", 14), command=show_info)
btninfo = makeCircleOREllipse + 7
timeLabel.place(x=DATA_FRAME_WIGHT + 2 * BORDERS_SPACE, y=CANVAS_HEIGHT + BORDERS_SPACE - DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 60, height=DATA_FRAME_HEIGHT // COLUMNS)
clearCanvasBtn.place(x=40, y=(btninfo + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)
infoBtn.place(x=40, y=(btninfo + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT - 80, height=DATA_FRAME_HEIGHT // COLUMNS)


xcEntry.insert(0, "500")
ycEntry.insert(0, "500")

rEntry.insert(0, "100")
rxEntry.insert(0, "200")
ryEntry.insert(0, "100")

root.mainloop()