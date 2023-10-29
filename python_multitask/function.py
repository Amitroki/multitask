import sys
import time
import multiprocessing

def calculating_sum_in_rows_without_multiprocessing(mas):
    sum2 = 0
    for row in mas:
        sum1 = 0
        for col in row:
            sum1 += col
        sum2 += sum1
    return sum2

def main():
    num_of_rows = int(input())
    num_of_columns = int(input())
    mas = []
    
    for i in range(num_of_rows):
        mas.append(list(map(int, input().split())))
    sum_in_rows = calculating_sum_in_rows_without_multiprocessing(mas)
    print(sum_in_rows)

if __name__ == "__main__":
    main()