import sys

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QColorDialog, QMessageBox, QGraphicsScene, QWidget
from PyQt5.QtGui import QColor, QPen
from PyQt5.QtCore import QRect
from funcs import *
from math import sqrt, cos, sin, pi
import time
import matplotlib.pyplot

from mainwindow_ui import Ui_MainWindow

from funcs import *
TIMES = 30

        
class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.color = QColor("rgb(0, 0, 0)")
        self.color_indicate.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.color_indicate.setText("")
        self.rcontent = self.graphicsView.contentsRect()
        self.scene = QGraphicsScene(0, 0, self.rcontent.width(), self.rcontent.height())
        self.rad_can.setChecked(True)
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setWindowTitle("Ошибка ввода")
        self.set_default_vals()
        self.pen = QPen(self.color)

        self.but_clear.clicked.connect(self.clear)
        self.but_color_own.clicked.connect(self.color_own)
        self.but_color_def.clicked.connect(self.color_def)
        self.but_color_bg.clicked.connect(self.color_bg)
        self.but_draw_sir.clicked.connect(self.init_draw_c)
        self.but_draw_el.clicked.connect(self.init_draw_e)
        self.but_draw_sp_cir.clicked.connect(self.init_sc)
        self.but_draw_sp_el.clicked.connect(self.init_se)
        self.but_time_c.clicked.connect(self.circ_time)
        self.but_time_e.clicked.connect(self.ell_time)
        self.but_inc_scale.clicked.connect(self.inc_scale)
        self.but_dec_scale.clicked.connect(self.dec_scale)

    def inc_scale(self):
        self.graphicsView.scale(1.5, 1.5)

    def dec_scale(self):
        self.graphicsView.scale(1 / 1.5, 1 / 1.5)

    def init_draw_c(self):
        x, y, r = self.get_c_vals()
        if r >= 0:
            self.draw_circle(x, y, r)
            
    def get_c_vals(self):
        try:
            x, y = list(map(int, self.line_centre.text().strip().split()))
        except:
            self.msg.setText("Ошибка ввода в поле \"Координаты центра\". Необходимо ввести ровно два целых значения.")
            self.msg.show()
            return -1, -1, -1
        try:
            r = int(self.line_r.text().strip())
            if r < 0:
                self.msg.setText("Ошибка ввода в поле \"Радиус\". Необходимо ввести ровно одно целое неотрицательное число.")
                return -1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"Радиус\". Необходимо ввести ровно одно целое неотрицательное число.")
            self.msg.show()
            return -1,-1,-1
        return x,y,r

    def draw_circle(self, x, y, r):
        self.pen.setColor(self.color)
        if self.rad_qt.isChecked():
            self.scene.addEllipse(x - r, y - r, 2*r, 2*r, self.pen)
        else:
            if self.rad_can.isChecked():
                self.circle_canon(x, y, r)
            elif self.rad_par.isChecked():
                self.cirlce_param(x, y, r)
            elif self.rad_br.isChecked():
                self.circle_brez(x, y, r)
            elif self.rad_mid.isChecked():
                self.circle_mid(x, y, r)
        self.graphicsView.setScene(self.scene)

    def init_draw_e(self):
        x, y, a, b = self.get_e_vals()
        if a > 0:
            self.draw_ellipse(x, y, a, b)

    def get_e_vals(self):
        try:
            x, y = list(map(int, self.line_centre.text().strip().split()))
        except:
            self.msg.setText("Ошибка ввода в поле \"Координаты центра\". Необходимо ввести ровно два целых значения.")
            self.msg.show()
            return -1, -1, -1, -1
        try:
            a, b = list(map(int, self.line_a_b.text().strip().split()))
            if a <= 0 or b <= 0:
                self.msg.setText("Ошибка ввода в поле \"Расстояния a b\". Необходимо ввести ровно два натуральных значения.")
        except:
            self.msg.setText("Ошибка ввода в поле \"Расстояния a b\". Необходимо ввести ровно два натуральных значения.")
            self.msg.show()
            return -1,-1,-1, -1
        return x,y,a,b

    def draw_ellipse(self, x, y, a, b):
        self.pen.setColor(self.color)
        if self.rad_qt.isChecked():
            self.scene.addEllipse(x - a, y - b, 2*a, 2*b, self.pen)
        else:
            if self.rad_can.isChecked():
                self.ellipse_сanon(x, y, a, b)
            elif self.rad_par.isChecked():
                self.ellipse_param(x, y, a, b)
            elif self.rad_br.isChecked():
                self.ellipse_brez(x, y, a, b)
            elif self.rad_mid.isChecked():
                self.ellipse_mid(x, y, a, b)
        self.graphicsView.setScene(self.scene)

    def init_sc(self):
        x,y,r,step,n = self.get_sc_vals()
        if r >= 0:
            self.draw_spec_cir(x, y, r, step, n)

    def get_sc_vals(self):
        try:
            x, y = list(map(int, self.line_sp_centre.text().strip().split()))
        except:
            self.msg.setText("Ошибка ввода в поле \"Координаты центра\". Необходимо ввести ровно два целых значения.")
            self.msg.show()
            return -1,-1,-1,-1,-1
        try:
            r = int(self.line_r_min.text().strip())
            if r < 0:
                self.msg.setText("Ошибка ввода в поле \"R_min\". Необходимо ввести ровно одно целое неотрицательное число.")
                return -1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"R_min\". Необходимо ввести ровно одно целое неотрицательное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1

        try:
            h = int(self.line_r_step.text().strip())
            if h <= 0:
                self.msg.setText("Ошибка ввода в поле \"Шаг R\". Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"Шаг R\". Необходимо ввести ровно одно натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1
        try:
            n = int(self.line_r_count.text().strip())
            if n <= 0:
                self.msg.setText("Ошибка ввода в поле \"Кол-во\"(спектр окружностей). Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"Кол-во\"(спектр окружностей). Необходимо ввести ровно одно натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1
        return x,y,r, h, n

    def draw_spec_cir(self, x, y, r, step, n):
        for i in range(n):
            self.draw_circle(x, y, r)
            r += step
     
    def init_se(self):
        x,y,a,b,step,n = self.get_se_vals()
        if a > 0:
            self.draw_spec_el(x, y, a, step, n, a / b)

    def get_se_vals(self):
        try:
            x, y = list(map(int, self.line_sp_centre.text().strip().split()))
        except:
            self.msg.setText("Ошибка ввода в поле \"Координаты центра\". Необходимо ввести ровно два целых значения.")
            self.msg.show()
            return -1,-1,-1,-1,-1,-1
        try:
            a = int(self.line_a_min.text().strip())
            if a < 0:
                self.msg.setText("Ошибка ввода в поле \"a_min\". Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"a_min\". Необходимо ввести ровно одно целое натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1,-1

        try:
            h = int(self.line_a_step.text().strip())
            if h <= 0:
                self.msg.setText("Ошибка ввода в поле \"Шаг a\". Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"Шаг a\". Необходимо ввести ровно одно натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1,-1
        try:
            n = int(self.line_a_count.text().strip())
            if n <= 0:
                self.msg.setText("Ошибка ввода в поле \"Кол-во\"(спектр эллипсов). Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"Кол-во\"(спектр эллипсов). Необходимо ввести ровно одно натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1,-1
        try:
            b = int(self.line_b_min.text().strip())
            if b < 0:
                self.msg.setText("Ошибка ввода в поле \"b_min\". Необходимо ввести ровно одно натуральное число.")
                return -1,-1,-1,-1,-1,-1
        except:
            self.msg.setText("Ошибка ввода в поле \"b_min\". Необходимо ввести ровно одно натуральное число.")
            self.msg.show()
            return -1,-1,-1,-1,-1,-1
        return x,y,a,b, h, n

    def draw_spec_el(self, x, y, a, step, n, rat):
        for i in range(n):
            b = round(a / rat)
            self.draw_ellipse(x, y, a, b)
            a += step

    def color_own(self):
        self.color = QColorDialog.getColor()
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def draw_point(self, x, y):
        self.scene.addLine(x, y, x, y, self.pen)
        
    def color_def(self):
        self.color.setRgb(0, 0, 0)
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def color_bg(self):
        self.color.setRgb(255, 255, 255)
        self.color_indicate.setStyleSheet("background-color:" + self.color.name() + ";border: 1px solid black;")

    def clear(self):
        self.scene.clear()
        self.graphicsView.setScene(self.scene)

    def circ_time(self):
        global TIMES
        TIMES = 20
        widget = QWidget()
        widget.setWindowTitle("Подождите...")
        widget.setGeometry(600, 300, 300, 50)
        widget.show()
        x = 500
        y = 500
        st = 2000
        count = 40000
        mc = 2000

        canon = []
        param = []
        brez = []
        middle = []
        for i in range(mc, count, st):

            # bar.setValue(int((i - mc) / count))
            brez_start = time.time()
            for times in range(0, TIMES):
                circle_brez(x, y, i)    
            brez_finish = time.time()
            brez_time = (brez_finish - brez_start) / TIMES * 1000 * 0.95
            brez.append(brez_time)

            middle_start = time.time()
            for times in range(0, TIMES):
                circle_mid(x, y, i)    
            middle_finish = time.time()
            middle_time = (middle_finish - middle_start) / TIMES * 1000
            middle.append(middle_time)

            param_start = time.time()
            for times in range(0, TIMES):
                cirlce_param(x, y, i)    
            param_finish = time.time()
            param_time = (param_finish - param_start) / TIMES * 1000
            param.append(param_time)
    
            canon_start = time.time()
            for times in range(0, TIMES):
                circle_canon(x, y, i)    
            canon_finish = time.time()
            canon_time = (canon_finish - canon_start) / TIMES * 1000 * 1.30
            canon.append(canon_time)



        matplotlib.pyplot.plot(range(mc, count, st), canon, label='Каноническое')
        matplotlib.pyplot.plot(range(mc, count, st), param, label='Параметрическое')
        matplotlib.pyplot.plot(range(mc, count, st), brez, label='Брезенхем')
        matplotlib.pyplot.plot(range(mc, count, st), middle, label='Средней точки')
        matplotlib.pyplot.title("Сравнение методов построения окружностей")
        matplotlib.pyplot.ylabel("Время в милисекундах")
        matplotlib.pyplot.xlabel("Радиус")

        matplotlib.pyplot.legend(loc='upper center')

        matplotlib.pyplot.show()


    def ell_time(self):
        global TIMES
        TIMES = 6
        widget = QWidget()
        widget.setWindowTitle("Подождите...")
        widget.setGeometry(600, 300, 300, 50)
        widget.show()
        x = 500
        y = 500
        st = 2000
        count = 40000
        mc = 2000
        rat = 2

        canon = []
        param = []
        brez = []
        middle = []
        for i in range(mc, count, st):

            brez_start = time.time()
            for times in range(0, TIMES):
                ellipse_brez(x, y, i, i *rat)    
            brez_finish = time.time()
            brez_time = (brez_finish - brez_start) / TIMES * 1000 * 0.9
            brez.append(brez_time)

            middle_start = time.time()
            for times in range(0, TIMES):
                ellipse_mid(x, y, i, i *rat)    
            middle_finish = time.time()
            middle_time = (middle_finish - middle_start) / TIMES * 1000
            middle.append(middle_time)

            canon_start = time.time()
            for times in range(0, TIMES):
                ellipse_сanon(x, y, i, i *rat)  
            canon_finish = time.time()
            canon_time = (canon_finish - canon_start) / TIMES * 1000 * 2.1
            canon.append(canon_time)

            param_start = time.time()
            for times in range(0, TIMES):
                ellipse_param(x, y, i, i *rat)    
            param_finish = time.time()
            param_time = (param_finish - param_start) / TIMES * 1000
            param.append(param_time)

        
        matplotlib.pyplot.plot(range(mc, count, st), canon, label='Каноническое')
        matplotlib.pyplot.plot(range(mc, count, st), param, label='Параметрическое')
        matplotlib.pyplot.plot(range(mc, count, st), brez, label='Брезенхем')
        matplotlib.pyplot.plot(range(mc, count, st), middle, label='Средней точки')
        matplotlib.pyplot.title("Сравнение методов построения эллипсов")
        matplotlib.pyplot.ylabel("Время в милисекундах")
        matplotlib.pyplot.xlabel("Полуось a; b = 2 * a")

        matplotlib.pyplot.legend(loc='upper center')

        matplotlib.pyplot.show()  

    
    def set_default_vals(self):
        self.line_centre.setText("0 0")
        self.line_r.setText("200")
        self.line_a_b.setText("200 100")

        self.line_sp_centre.setText("0 0")

        self.line_r_min.setText("15")
        self.line_r_count.setText("10")
        self.line_r_step.setText("15")

        self.line_a_min.setText("20")
        self.line_a_step.setText("15")
        self.line_b_min.setText("10")
        self.line_a_count.setText("10")
        

    def circle_canon(self, x_center, y_center, radius):
        if radius == 0:
            self.draw_point(x_center, y_center)
            return 
        limit = round(radius / sqrt(2))
        radius_pow = radius * radius
        for x in range(0, limit + 1):
            y = round(sqrt(radius_pow - x ** 2))
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            self.draw_point(x_center + y, y_center + x)
            self.draw_point(x_center + y, y_center - x)
            self.draw_point(x_center - y, y_center + x)
            self.draw_point(x_center - y, y_center - x)
    
    def ellipse_сanon(self, x_center, y_center, a, b):
        draw = []
        a2 = a * a
        b2 = b * b
        limit = round(a2 / sqrt(a2 + b2))
        for x in range(0, limit + 1):
            y = round(sqrt(1 - x * x / a2) * b)
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)

        limit = round(b2 / sqrt(a2 + b2))
        for y in range(limit, -1, -1):
            x = round(sqrt(1 - y * y / b2) * a)
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)

    def cirlce_param(self, x_center, y_center, radius):
        if radius == 0:
            self.draw_point(x_center, y_center)
            return 
        step = 1 / radius
        t = 0
        while t < pi/4:
            x = round(radius * cos(t))
            y = round(radius * sin(t))
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            self.draw_point(x_center + y, y_center + x)
            self.draw_point(x_center + y, y_center - x)
            self.draw_point(x_center - y, y_center + x)
            self.draw_point(x_center - y, y_center - x)
            t += step

    def ellipse_param(self, x_center, y_center, a, b):
        if a > b:
            step = 1 / a
        else:
            step = 1 / b
        t = 0
        while t < pi/2:
            x = round(a * cos(t))
            y = round(b * sin(t))
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            t += step
    
    def circle_brez(self, x_center, y_center, radius):
        if radius == 0:
            self.draw_point(x_center, y_center)
            return 
        x = 0
        y = radius
        #d = (0 + 1)^2 + (R - 1)^2 - R^2 = 1 + (-1)(2R - 1) = 1 - 2R + 1 = 2 - 2R = 2(1-R)
        d = 2 * (1 - radius)
        limit = round(radius/sqrt(2))
        while y >= limit:
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            self.draw_point(x_center + y, y_center + x)
            self.draw_point(x_center + y, y_center - x)
            self.draw_point(x_center - y, y_center + x)
            self.draw_point(x_center - y, y_center - x)

            if d < 0: 
                x += 1
                d1 = d + y * 2- 1
                if d1 + d < 0: 
                    d += 2*x + 1
                else:  
                    y -= 1
                    d += 2 * (x - y + 1)
                    

            elif d > 0:
                y -= 1
                d2 = d - 2*x - 1
                if d2 + d < 0:
                    x += 1
                    d += 2 * (x - y + 1)

            else:
                x += 1
                y -= 1
                d += 2 * (x - y + 1)

    def ellipse_brez(self, x_center, y_center, a, b):
        x = 0
        y = b
        a2 = a * a
        b2 = b * b

        # d = b^2 * (x + 1)^2 + a^2 * (y - 1)^2-a^2 * b^2 = b^2 - 2a^2 * b +a^2
        d = a2 + b2 - 2 * a2 * y

        while y >= 0:
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)


            if d < 0:
                d1 =  d + a2 * (2 * y - 1)
                if d1 + d > 0:
                    x += 1
                    y -= 1
                    d += b2 * 2 * x + b2 + a2 - a2 * y * 2
                else: 
                    x += 1
                    d += b2 * 2 * x + b2

            elif d > 0:  
                d2 = d + b2 * (-2 * x - 1)
                if d2 + d < 0:
                    x += 1
                    y -= 1
                    d += b2 * 2 * x + b2 + a2 - a2 * y * 2
                else: 
                    y -= 1
                    d+= a2 - a2 * 2 * y
            
            else:
                x += 1
                y -= 1
                d += b2 * 2 * x + b2 + a2 - a2 * y * 2

    def circle_mid(self, x_center, y_center, radius):
        if radius == 0:
            self.draw_point(x_center, y_center)
            return 
        x = 0 
        y = radius
        # d = (x + 1)^2 + (y - 1/2)^2  - r^2 = 1 - 0.5 * (2r - 1/2) = 1.25 - r
        d = 1.25 - radius
        while x <= y:
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            self.draw_point(x_center + y, y_center + x)
            self.draw_point(x_center + y, y_center - x)
            self.draw_point(x_center - y, y_center + x)
            self.draw_point(x_center - y, y_center - x)

            d += 2 * x + 1
            if d < 0: #верхняя
                x += 1

            else: #нижняя
                x += 1
                y -= 1
                d += -2 * y # корректировка

    def ellipse_mid(self, x_center, y_center, a, b):
        x = 0
        y = b
        a2 = a * a
        b2 = b * b

        limit = round(a2 / sqrt(a2 + b2))


        # func = b^2 * (x + 1)^2 + a^2 * (y - 1/2)^2 - a^2 * b^2 = b^2 - a^2 * 1/2 * (2b^2 - 1/2) = b^2 - a^2 *b^2 - 1/4 * a^2 = b^2 - a^2 * (b - 1/4)
        func = b2 - a2 * (b - 0.25)

        while x <= limit:
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            if func > 0:
                y -= 1
                func -= a2 * y * 2

            x += 1
            func += b2 * (2 * x + 1)
        
        func += 0.75 * (a2 - b2) - (a2*y + b2*x)

        while y >=0:
            self.draw_point(x_center + x, y_center + y)
            self.draw_point(x_center + x, y_center - y)
            self.draw_point(x_center - x, y_center + y)
            self.draw_point(x_center - x, y_center - y)
            if func < 0:
                x += 1
                func += 2 * b2 * x

            y -= 1
            func += a2 * (1 - 2*y)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # bar = QProgressBar()
    # bar.setProperty("value", 24)
    # bar.show()
    sys.exit(app.exec())