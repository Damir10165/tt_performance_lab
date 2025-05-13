import sys


if __name__ == '__main__':
    # circle_way - путь к файлу с координатами и радиусом окружности
    # points_way - путь к файлу с координатами точек
    circle_way, points_way = sys.argv[1:]

    with open(circle_way) as cf:
        x_circle, y_circle, r_circle = map(float, cf.read().split())
        cf.close()

    with open(points_way) as pf:
        # записываем точки в список в виде строк: 'x y'
        points = pf.read().split('\n')
        pf.close()

    for p in points:
        x, y = map(float, p.split())
        # вычисляем часть уравнения окружности
        cp = ((x - x_circle) ** 2 + (y - y_circle) ** 2) ** (1 / 2)

        # сравниваем с радиусом
        if cp == r_circle:
            print(0)
        elif cp < r_circle:
            print(1)
        else:
            print(2)
