from math import sqrt, cos, sin, pi

def circle_canon(x_center, y_center, radius):
    if radius == 0:
        x_center, y_center
        return 
    limit = round(radius / sqrt(2))
    radius_pow = radius * radius
    for x in range(0, limit + 1):
        y = round(sqrt(radius_pow - x ** 2))

def ellipse_сanon(x_center, y_center, a, b):
    draw = []
    a2 = a * a
    b2 = b * b
    limit = round(a2 / sqrt(a2 + b2))
    for x in range(0, limit + 1):
        y = round(sqrt(1 - x * x / a2) * b)

        
    limit = round(b2 / sqrt(a2 + b2))
    for y in range(limit, -1, -1):
        x = round(sqrt(1 - y * y / b2) * a)


def cirlce_param(x_center, y_center, radius):
    if radius == 0:
        x_center, y_center
        return 
    step = 1 / radius
    t = 0
    while t < pi/4:
        x = round(radius * cos(t))
        y = round(radius * sin(t))
        t += step

def ellipse_param(x_center, y_center, a, b):
    if a > b:
        step = 1 / a
    else:
        step = 1 / b
    t = 0
    while t < pi/2:
        x = round(a * cos(t))
        y = round(b * sin(t))
        t += step

def circle_brez(x_center, y_center, radius):
    if radius == 0:
        return 
    x = 0
    y = radius
    #d = (0 + 1)^2 + (R - 1)^2 - R^2 = 1 + (-1)(2R - 1) = 1 - 2R + 1 = 2 - 2R = 2(1-R)
    d = 2 * (1 - radius)
    limit = round(radius/sqrt(2))
    while y >= limit:

        if d < 0: 
            x += 1
            d1 = d + y * 2- 1
            if d1 + d < 0: 
                d += x + x + 1
            else:  
                y -= 1
                d += 2 * (x - y + 1)
                

        elif d > 0:
            y -= 1
            d2 = d - x -x - 1
            if d2 + d < 0:
                x += 1
                d += 2 * (x - y + 1)

        else:
            x += 1
            y -= 1
            d += 2 * (x - y + 1)

def ellipse_brez(x_center, y_center, a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b

    # d = b^2 * (x + 1)^2 + a^2 * (y - 1)^2-a^2 * b^2 = b^2 - 2a^2 * b +a^2
    d = a2 + b2 - 2 * a2 * y

    while y >= 0:

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
            d2 = d + b2 * (-x - x - 1)
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

def circle_mid(x_center, y_center, radius):
    if radius == 0:
        x_center, y_center
        return 
    x = 0 
    y = radius
    # d = (x + 1)^2 + (y - 1/2)^2  - r^2 = 1 - 0.5 * (2r - 1/2) = 1.25 - r
    d = 1.25 - radius
    while x <= y:

        d += 2 * x + 1
        if d < 0: #верхняя
            x += 1

        else: #нижняя
            x += 1
            y -= 1
            d += -2 * y # корректировка

def ellipse_mid(x_center, y_center, a, b):
    x = 0
    y = b
    a2 = a * a
    b2 = b * b

    limit = round(a2 / sqrt(a2 + b2))


    # func = b^2 * (x + 1)^2 + a^2 * (y - 1/2)^2 - a^2 * b^2 = b^2 - a^2 * 1/2 * (2b^2 - 1/2) = b^2 - a^2 *b^2 - 1/4 * a^2 = b^2 - a^2 * (b - 1/4)
    func = b2 - a2 * (b - 0.25)

    while x <= limit:
        if func > 0:
            y -= 1
            func -= a2 * y * 2

        x += 1
        func += b2 * (2 * x + 1)
    
    func += 0.75 * (a2 - b2) - (a2*y + b2*x)

    while y >=0:
        if func < 0:
            x += 1
            func += 2 * b2 * x

        y -= 1
        func += a2 * (1 - 2*y)
        