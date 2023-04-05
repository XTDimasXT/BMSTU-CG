from functions import *


def brensenham_float_line(x0, y0, x1, y1, colour='black', stepmode=False):
    points = []

    if x0 == x1 and y0 == y1:
        points.append([x0, y0, colour])
    else:
        dx = x1 - x0
        dy = y1 - y0

        sx = sign(dx)
        sy = sign(dy)

        dy = abs(dy)
        dx = abs(dx)

        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
        else:
            exchange = 0

        tg = dy / dx
        e = tg - 0.5
        x = x0
        y = y0

        xb = x0
        yb = y0
        steps = 0

        while x != x1 or y != y1:

            if not stepmode:
                points.append([x, y, colour])

            if e >= 0:
                if exchange == 1:
                    x += sx
                else:
                    y += sy
                e -= 1

            if e <= 0:
                if exchange == 0:
                    x += sx
                else:
                    y += sy
                e += tg

            if stepmode:
                if xb != x and yb != y:
                    steps += 1
                xb = x
                yb = y

        if stepmode:
            return steps
    
    return points


def brensenham_integer_line(x0, y0, x1, y1, colour='black', stepmode=False):
    points = []
    
    if x0 == x1 and y0 == y1:
        points.append([x0, y0, colour])
    else:
        dx = x1 - x0
        dy = y1 - y0

        sx = sign(dx)
        sy = sign(dy)

        dy = abs(dy)
        dx = abs(dx)

        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
        else:
            exchange = 0

        e = 2 * dy - dx
        x = x0
        y = y0

        xb = x
        yb = y
        steps = 0

        while x != x1 or y != y1:
            if stepmode == False:
                points.append([x, y, colour])

            if e >= 0:
                if exchange == 1:
                    x += sx
                else:
                    y += sy
                e -= 2 * dx
            if e <= 0:
                if exchange == 0:
                    x += sx
                else:
                    y += sy
                e += 2 * dy

            if stepmode:
                if xb != x and yb != y:
                    steps += 1
                xb = x
                yb = y

        if stepmode:
            return steps
        
    return points


def brensenham_smooth_line(canvas, x0, y0, x1, y1, fill='black', stepmode=False):
    global bg_colour
    
    points = []
    
    I = 100
    fill = get_rgb_intensity(canvas, fill, bg_colour, I)
    dx = x1 - x0
    dy = y1 - y0
    sx = sign(dx)
    sy = sign(dy)
    dy = abs(dy)
    dx = abs(dx)
    if dy >= dx:
        dx, dy = dy, dx
        steep = 1
    else:
        steep = 0 
    tg = dy / dx * I
    e = I / 2
    w = I - tg
    x = x0
    y = y0

    xb = x
    yb = y
    steps = 0

    while x != x1 or y != y1:
        if not stepmode:
            points.append([x, y, fill[round(e) - 1]])
        if e < w:
            if steep == 0:
                x += sx
            else:
                y += sy
            e += tg
        elif e >= w:
            x += sx
            y += sy
            e -= w

        if stepmode:
            if xb != x and yb != y:
                steps += 1
            xb = x
            yb = y

    if stepmode:
        return steps
    
    return points