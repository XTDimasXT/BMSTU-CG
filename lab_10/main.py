import tkinter as tk
from tkinter import colorchooser

from constants import *
from draw import *


def get_colour_res():
    colour_code = colorchooser.askcolor(title="Choose colour res")
    set_res_colour(colour_code[-1])


def set_res_colour(colour):
    global RESULT_COLOUR
    RESULT_COLOUR = colour


def main():
    window = tk.Tk()
    window.title("Лабораторная работа №10. Реализация алгоритма плавающего горизонта построения трехмерных поверхностей")
    window["bg"] = MAIN_COLOUR

    window.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
    window.resizable(height=False, width=False)

    dataFrame = tk.Frame(window, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT)
    dataFrame["bg"] = MAIN_FRAME_COLOR

    dataFrame.pack(side=tk.LEFT, padx=BORDERS_SPACE, fill=tk.Y)

    canvasField = tk.Canvas(window, bg=CANVAS_COLOUR, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvasField.pack(side=tk.RIGHT, padx=BORDERS_SPACE)

    size = (DATA_FRAME_WIGHT // 1.7) // 8

    chooseColourMainLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ЦВЕТА", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    chooseColourMainLabel.place(x=0, y=0, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    colour_var = tk.IntVar()
    colour_var.set(2)

    resColourLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Цвет функций:", font=("Consolas", 14), fg=MAIN_COLOUR_LABEL_TEXT)

    whiteLine = tk.Button(dataFrame, bg="white", activebackground="white", command=lambda: set_res_colour("white"))
    yellowLine = tk.Button(dataFrame, bg="yellow", activebackground="yellow", command=lambda: set_res_colour("yellow"))
    orangeLine = tk.Button(dataFrame, bg="orange", activebackground="orange", command=lambda: set_res_colour("orange"))
    redLine = tk.Button(dataFrame, bg="red", activebackground="red", command=lambda: set_res_colour("red"))
    purpleLine = tk.Button(dataFrame, bg="purple", activebackground="purple", command=lambda: set_res_colour("purple"))
    greenLine = tk.Button(dataFrame, bg="green", activebackground="green", command=lambda: set_res_colour("green"))
    darkGreenLine = tk.Button(dataFrame, bg="darkgreen", activebackground="darkgreen", command=lambda: set_res_colour("darkgreen"))
    lightBlueLine = tk.Button(dataFrame, bg="lightblue", activebackground="lightblue", command=lambda: set_res_colour("lightblue"))

    resColourBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Выбрать другой цвет функций', font=("Consolas", 12), command=lambda: get_colour_res())

    yColourLine = 1.2
    resColourLabel.place(x=5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

    whiteLine.place(x=DATA_FRAME_WIGHT // 2.5, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    yellowLine.place(x=DATA_FRAME_WIGHT // 2.5 + size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    orangeLine.place(x=DATA_FRAME_WIGHT // 2.5 + 2 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    redLine.place(x=DATA_FRAME_WIGHT // 2.5 + 3 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    purpleLine.place(x=DATA_FRAME_WIGHT // 2.5 + 4 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    greenLine.place(x=DATA_FRAME_WIGHT // 2.5 + 5 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    darkGreenLine.place(x=DATA_FRAME_WIGHT // 2.5 + 6 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)
    lightBlueLine.place(x=DATA_FRAME_WIGHT // 2.5 + 7 * size, y=yColourLine * DATA_FRAME_HEIGHT // COLUMNS, width=size, height=DATA_FRAME_HEIGHT // COLUMNS - 10)

    resColourBtn.place(x=DATA_FRAME_WIGHT // 3 - BORDERS_SPACE, y=(yColourLine + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.5, height=DATA_FRAME_HEIGHT // COLUMNS)


    makePoint = yColourLine + 3
    chooseFunctionLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ФУНКЦИИ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    chooseFunctionLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    func_var = tk.IntVar()
    func_var.set(0)

    function_1_Btn = tk.Radiobutton(dataFrame, variable=func_var, value=0, bg="white", fg=MAIN_COLOUR_LABEL_TEXT, text='sin(x) * cos(z)', font=("Consolas", 14))
    function_2_Btn = tk.Radiobutton(dataFrame, variable=func_var, value=1, bg="white", fg=MAIN_COLOUR_LABEL_TEXT, text='sin(cos(x)) * sin(z)', font=("Consolas", 14))
    function_3_Btn = tk.Radiobutton(dataFrame, variable=func_var, value=2, bg="white", fg=MAIN_COLOUR_LABEL_TEXT, text='cos(x) * z / 4', font=("Consolas", 14))
    function_4_Btn = tk.Radiobutton(dataFrame, variable=func_var, value=3, bg="white", fg=MAIN_COLOUR_LABEL_TEXT, text='cos(x) * cos(sin(z))', font=("Consolas", 14))

    makePoint += 1.5
    function_1_Btn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 0.0) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)
    function_2_Btn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 1.1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)
    function_3_Btn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 2.2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)
    function_4_Btn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 3.3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)

    makePoint += 5.2


    chooseLimitsLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ПРЕДЕЛОВ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    chooseLimitsLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    makePoint += 1.2

    infoLimitsLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="От        До        Шаг", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    infoLimitsLabel.place(x=20, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    OXLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Ox:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    OZLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Oz:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    OXLabel.place(x=-50, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)
    OZLabel.place(x=-50, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

    xStartEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    xEndEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    xStepEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

    zStartEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    zEndEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    zStepEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

    xStartEntry.place(x=1 * DATA_FRAME_WIGHT // 6, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    xEndEntry.place(x=2.6 * DATA_FRAME_WIGHT // 6, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    xStepEntry.place(x=4.2 * DATA_FRAME_WIGHT // 6, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))

    zStartEntry.place(x=1 * DATA_FRAME_WIGHT // 6, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    zEndEntry.place(x=2.6 * DATA_FRAME_WIGHT // 6, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    zStepEntry.place(x=4.2 * DATA_FRAME_WIGHT // 6, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))

    makePoint += 3.2


    chooseLimitsLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР МАСШТАБИРОВАНИЯ", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    chooseLimitsLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    makePoint += 0.2

    coefScaleLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Коэффициент:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    coefScaleLabel.place(x=0, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

    coefScaleEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    coefScaleEntry.place(x=2.6 * DATA_FRAME_WIGHT // 6, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))

    scaleButton = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Масштабировать', font=("Consolas", 14), command=lambda: scale_graph(coefScaleEntry, canvasField, RESULT_COLOUR, func_var, xStartEntry, xEndEntry, xStepEntry, zStartEntry, zEndEntry, zStepEntry))
    scaleButton.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 2.0) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)

    makePoint += 3.2


    chooseLimitsLabel = tk.Label(dataFrame, bg=MAIN_COLOUR_LABEL_BG, text="ВЫБОР ПОВОРОТА", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT, relief=tk.SOLID)
    chooseLimitsLabel.place(x=0, y=makePoint * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT, height=DATA_FRAME_HEIGHT // COLUMNS)

    makePoint += 0.2

    OXLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Ox:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    OYLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Oy:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)
    OZLabel = tk.Label(dataFrame, bg=MAIN_FRAME_COLOR, text="Oz:", font=("Consolas", 16), fg=MAIN_COLOUR_LABEL_TEXT)

    OXLabel.place(x=-50, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)
    OYLabel.place(x=-50, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)
    OZLabel.place(x=-50, y=(makePoint + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 2.5, height=DATA_FRAME_HEIGHT // COLUMNS)

    xRotateEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    yRotateEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")
    zRotateEntry = tk.Entry(dataFrame, bg=MAIN_COLOUR_LABEL_TEXT, font=("Consolas", 14), fg=MAIN_FRAME_COLOR, justify="center")

    xRotateEntry.place(x=1 * DATA_FRAME_WIGHT // 6, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    yRotateEntry.place(x=1 * DATA_FRAME_WIGHT // 6, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    zRotateEntry.place(x=1 * DATA_FRAME_WIGHT // 6, y=(makePoint + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 5, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))

    xRotateBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Повернуть', font=("Consolas", 14), command=lambda: spin_x(xRotateEntry, canvasField, RESULT_COLOUR, func_var, xStartEntry, xEndEntry, xStepEntry, zStartEntry, zEndEntry, zStepEntry))
    yRotateBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Повернуть', font=("Consolas", 14), command=lambda: spin_y(yRotateEntry, canvasField, RESULT_COLOUR, func_var, xStartEntry, xEndEntry, xStepEntry, zStartEntry, zEndEntry, zStepEntry))
    zRotateBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Повернуть', font=("Consolas", 14), command=lambda: spin_z(zRotateEntry, canvasField, RESULT_COLOUR, func_var, xStartEntry, xEndEntry, xStepEntry, zStartEntry, zEndEntry, zStepEntry))

    xRotateBtn.place(x=DATA_FRAME_WIGHT // 2 - BORDERS_SPACE, y=(makePoint + 1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 3, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    yRotateBtn.place(x=DATA_FRAME_WIGHT // 2 - BORDERS_SPACE, y=(makePoint + 2) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 3, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))
    zRotateBtn.place(x=DATA_FRAME_WIGHT // 2 - BORDERS_SPACE, y=(makePoint + 3) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 3, height=DATA_FRAME_HEIGHT // (COLUMNS * 1.2))

    makePoint += 4.7


    constructFuctionBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Построить функцию', font=("Consolas", 14), command=lambda: build_graph(canvasField, RESULT_COLOUR, func_var, xStartEntry, xEndEntry, xStepEntry, zStartEntry, zEndEntry, zStepEntry, new_graph=True))
    clearBtn = tk.Button(dataFrame, bg=MAIN_COLOUR, fg=MAIN_COLOUR_LABEL_TEXT, text='Очистить экран', font=("Consolas", 14), command=lambda: clear_canvas(canvasField))

    constructFuctionBtn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 0.0) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)
    clearBtn.place(x=DATA_FRAME_WIGHT // 15 - BORDERS_SPACE, y=(makePoint + 1.1) * DATA_FRAME_HEIGHT // COLUMNS, width=DATA_FRAME_WIGHT // 1.1, height=DATA_FRAME_HEIGHT // COLUMNS)


    xStartEntry.insert(0, "-5")
    xEndEntry.insert(0, "5")
    xStepEntry.insert(0, "0.1")

    zStartEntry.insert(0, "-5")
    zEndEntry.insert  (0,  "5")
    zStepEntry.insert(0, "0.1")

    coefScaleEntry.insert(0, "50")
    
    xRotateEntry.insert(0, "60")
    yRotateEntry.insert(0, "60")
    zRotateEntry.insert(0, "60")


    window.mainloop()


if __name__ == "__main__":
    main()