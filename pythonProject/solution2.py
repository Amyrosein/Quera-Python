def get_func(ls):
    func_list = []

    def square_func(l):
        return l**2

    def circle_func(r):
        return r**2 * 3.14159265359

    def rectangle_func(w, l):
        return w * l

    def triangle_func(w, l):
        return (w * l) / 2

    for item in ls:
        if item == 'square':
            func_list.append(square_func)
        elif item == 'circle':
            func_list.append(circle_func)
        elif item == 'rectangle':
            func_list.append(rectangle_func)
        else:
            func_list.append(triangle_func)

    return func_list
