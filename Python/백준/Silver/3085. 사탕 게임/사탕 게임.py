from sys import stdin
from collections import deque
import time



def check(field, row):
    Max = 1
    for i in range(row):
        row_score = 1
        for j in range(row-1):
            if field[i][j] == field[i][j+1]:
                row_score+=1
                Max = max(row_score, Max)
            else:
                row_score=1
        # Max = max(row_score,Max)


    for j in range(row):
        row_score = 1
        for i in range(row-1):
            if field[i][j] == field[i+1][j]:
                row_score+=1
                # print(*field, sep='\n')
                Max = max(row_score, Max)

            else:
                row_score=1

    return Max




def func1():
    row = int(stdin.readline())
    field = [0 for _ in range(row)]
    Max_score = 1
    for i in range(row):
        field[i] = list(stdin.readline().rstrip())
    # print(field)

    for i in range(row):
        for j in range(row-1):
            if field[i][j] != field[i][j+1]:
                temp = field[i][j]
                field[i][j] = field[i][j+1]
                field[i][j+1] = temp
                # print(field)
                Max_score= max(check(field,row),Max_score)

                temp = field[i][j]
                field[i][j] = field[i][j + 1]
                field[i][j + 1] = temp

    for j in range(row):
        for i in range(row - 1):
            if field[i][j] != field[i+1][j]:
                temp = field[i][j]
                field[i][j] = field[i+1][j]
                field[i+1][j] = temp

                Max_score = max(check(field, row), Max_score)

                temp = field[i][j]
                field[i][j] = field[i + 1][j]
                field[i + 1][j] = temp
    print(Max_score)







func1()


