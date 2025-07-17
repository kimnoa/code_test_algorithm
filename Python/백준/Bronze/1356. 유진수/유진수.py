from sys import stdin
from collections import deque
import time

def func1():
    numlist = list(stdin.readline().rstrip())
    num = list(map(int, numlist))
    for i in range(len(num)-1):
        a = 1
        b = 1
        A = num[0:i+1]
        B = num[i+1:]
        # print(A,B)
        for j in A:
            a *=j
        for j in B:
            b *= j

        if(a==b):
            print("YES")
            return
    print("NO")


func1()


