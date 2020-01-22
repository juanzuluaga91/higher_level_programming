#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(n - 1):
        row = [1]
        if len(tri[i]) == 1:
            row += [1]
        else:
            row += [x + y for x, y in zip(tri[i], [0] + tri[i][:-1])][1:]
            row += [1]
        tri.append(row)
    return tri
