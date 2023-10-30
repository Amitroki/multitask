import sys
from timeit import default_timer
from time import sleep
from multiprocessing import Pool


def calculating_sum_in_rows_without_multiprocessing(mas: list) -> int:
    """Считает сумму чисел в строке без параллельных вычислений"""

    sum2 = 0
    for row in mas:
        sleep(1)
        sum1 = 0
        for col in row:
            sum1 += col
        sum2 += sum1
    return sum2


def summation(x: list) -> int:
    """Суммирование элементов в 1 строке"""

    return sum(x)


def calculating_sum_in_rows_with_multiprocessing(mas: list) -> int:
    """Считает сумму чисел в строке при помощи параллельных вычислений"""

    sum2 = []
    with Pool(20) as p:
        sleep(1)
        sum2 += p.map(summation, mas)
    return sum(sum2)


def main() -> None:

    num_of_rows = sys.argv[1]
    num_of_columns = sys.argv[2]

    mas = []
    for i in range(int(num_of_rows)):
        mas1 = []
        for j in range(int(num_of_columns)):
            mas1.append(int(sys.argv[(i * int(num_of_rows) + j) + 3]))
        mas.append(mas1)

    time = default_timer()
    sum_in_rows = calculating_sum_in_rows_without_multiprocessing(mas)
    print("Result of calculation numbers in rows of matrix:", end=" ")
    print(sum_in_rows)
    print("Time of execution:", end=" "),
    print(default_timer() - time)

    time = default_timer()
    sum_in_rows = calculating_sum_in_rows_with_multiprocessing(mas)
    print("Result of calculation numbers in rows of matrix:", end=" ")
    print(sum_in_rows)
    print("Time of execution:", end=" "),
    print(default_timer() - time)
