def get_vector(dot1, dot2):
    return [dot2[0] - dot1[0], dot2[1] - dot1[1]]


def vector_mul(vec1, vec2):
    return (vec1[0] * vec2[1] - vec1[1] * vec2[0])


def scalar_mul(vec1, vec2):
    return (vec1[0] * vec2[0] + vec1[1] * vec2[1])


def check_polygon(cutter): 
    if len(cutter) < 4:
        return False

    if vector_mul(get_vector(cutter[1], cutter[2]), 
                  get_vector(cutter[0], cutter[1])) > 0:
        sign = 1
    else:
        sign = -1

    for i in range(3, len(cutter)):
        if sign * vector_mul(get_vector(cutter[i - 1], cutter[i]),
                             get_vector(cutter[i - 2], cutter[i - 1])) < 0:
            return False

    if sign < 0:
        cutter.reverse()

    return True


def get_normal(dot1, dot2, dot3):
    vector = get_vector(dot1, dot2)

    if vector[1]:
        normal = [1, - vector[0] / vector[1]]
    else:
        normal = [0, 1]

    if scalar_mul(get_vector(dot2, dot3), normal) < 0:
        normal[0] = - normal[0]
        normal[1] = - normal[1]

    return normal


def make_unique(sides):
    for side in sides:
        side.sort()

    return list(filter(lambda x: (sides.count(x) % 2) == 1, sides))


def is_dot_in_side(dot, side):
    if abs(vector_mul(get_vector(dot, side[0]), get_vector(side[1], side[0]))) <= 1e-6:
        if (side[0] < dot < side[1] or side[1] < dot < side[0]):
            return True
    return False


def get_sides(side, rest_dots):
    dots_list = [side[0], side[1]]

    for dot in rest_dots:
        if is_dot_in_side(dot, side):
            dots_list.append(dot)

    dots_list.sort()

    sections_list = list()

    for i in range(len(dots_list) - 1):
        sections_list.append([dots_list[i], dots_list[i + 1]])

    return sections_list


def remove_odd_sides(figure_dots):
    all_sides = list()
    rest_dots = figure_dots[2:]

    for i in range(len(figure_dots)):
        cur_side = [figure_dots[i], figure_dots[(i + 1) % len(figure_dots)]]

        all_sides.extend(get_sides(cur_side, rest_dots))

        rest_dots.pop(0)
        rest_dots.append(figure_dots[i])

    return make_unique(all_sides)


def is_visible(dot, f_dot, s_dot):
    vec1 = get_vector(f_dot, s_dot)
    vec2 = get_vector(f_dot, dot)

    if vector_mul(vec1, vec2) <= 0:
        return True
    else:
        return False


def get_lines_parametric_intersec(line1, line2, normal):
    d = get_vector(line1[0], line1[1])
    w = get_vector(line2[0], line1[0])

    d_scalar = scalar_mul(d, normal)
    w_scalar = scalar_mul(w, normal)

    t = -w_scalar / d_scalar

    return [line1[0][0] + d[0] * t, line1[0][1] + d[1] * t]


def sutherland_hodgman_algorythm(cutter_line, position, figure):
    cur_result = []

    dot1 = cutter_line[0]
    dot2 = cutter_line[1]

    normal = get_normal(dot1, dot2, position)
    prev_vision = is_visible(figure[-2], dot1, dot2)

    for i in range(-1, len(figure)):
        cur_vision = is_visible(figure[i], dot1, dot2)

        if prev_vision:
            if cur_vision:
                cur_result.append(figure[i])
            else:
                figure_line = [figure[i - 1], figure[i]]
                cur_result.append(get_lines_parametric_intersec(figure_line, cutter_line, normal))
        else:
            if cur_vision:
                figure_line = [figure[i - 1], figure[i]]
                cur_result.append(get_lines_parametric_intersec(figure_line, cutter_line, normal))
                cur_result.append(figure[i])

        prev_vision = cur_vision

    return cur_result