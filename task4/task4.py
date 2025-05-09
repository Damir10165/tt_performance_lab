import statistics as st


if __name__ == '__main__':
    way = input()

    with open(way) as f:
        nums = list(map(int, f.read().split()))
        f.close()

    # вычисляем среднее значение и округляем
    mean = round(st.mean(nums))

    # вычитаем из каждого элемента среднее значение и суммируем для определения количества шагов необходимых,
    # для приведения всех элементов к одному значению
    print(sum(map(lambda x: abs(x - mean), nums)))
