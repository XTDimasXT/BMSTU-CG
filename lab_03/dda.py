def dda_line(x0, y0, x1, y1, line_colour):
    stepmode = False
    points = []
    steps = 0
    if x0 == x1 and y0 == y1:
        points.append([round(x0), round(y0), line_colour])
    else:
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        if dx >= dy:
            length = dx
        else:
            length = dy
        dx = (x1 - x0) / length
        dy = (y1 - y0) / length

        x = x0
        y = y0

        for i in range(0, int(length) + 1):
            if not stepmode:
                points.append([round(x), round(y), line_colour])
            elif round(x + dx) != round(x) and round(y + dy) != round(y):
                steps += 1
            x += dx
            y += dy

    if stepmode:
        return steps
    
    return points