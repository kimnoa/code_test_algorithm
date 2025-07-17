from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy


def check1():
    a = int(stdin.readline())
    while a:
        checker = 0
        a=list(str(a))
        for i in range(len(a)//2):
            if a[i]!=a[len(a)-i-1]:
                checker+=1
            if checker:
                break
        if checker:
            print("no")
        else:
            print("yes")

        a=int(stdin.readline())




#실행 부분
# start=time.time()
check1()
# end=time.time()
