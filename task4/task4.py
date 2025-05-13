import sys
import statistics as st


if __name__ == '__main__':
    way = sys.argv[1]

    with open(way) as f:
        nums = list(map(int, f.read().split()))
        f.close()

    # вычисляем среднее геометрическое значение и округляем
    g_mean = round(st.geometric_mean(nums))

    # вычитаем из каждого элемента среднее значение и суммируем для определения количества шагов необходимых,
    # для приведения всех элементов к одному значению
    print(sum(map(lambda x: abs(x - g_mean), nums)))
