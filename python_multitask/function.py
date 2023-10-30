import sys
from timeit import default_timer
from time import sleep
from multiprocessing import Pool

def calculating_sum_in_rows_without_multiprocessing(mas):
    sum2 = 0
    for row in mas:
        sleep(1)
        sum1 = 0
        for col in row:
            sum1 += col
        sum2 += sum1
    return sum2

def summation(x):
    return sum(x)

def calculating_sum_in_rows_with_multiprocessing(mas):
    sum2 = []
    with Pool(20) as p:
        sleep(1)
        sum2 += p.map(summation, mas)
    return sum(sum2)

def main():
    num_of_rows = int(input())
    num_of_columns = int(input())
    mas = []

    for i in range(num_of_rows):
        mas.append(list(map(int, input().split())))

    time = default_timer()
    sum_in_rows = calculating_sum_in_rows_without_multiprocessing(mas)
    print(sum_in_rows)
    print(default_timer() - time)

    time = default_timer()
    sum_in_rows = calculating_sum_in_rows_with_multiprocessing(mas)
    print(sum_in_rows)
    print(default_timer() - time)

if __name__ == "__main__":
    main()