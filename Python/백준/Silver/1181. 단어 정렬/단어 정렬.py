from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy

a = int(stdin.readline())
# b = int(stdin.readline())


def check1():
    letters = list(0 for _ in range(a))
    for i in range(a):
        letters[i]=stdin.readline().replace("\n",'')
    letters = list(set(letters))
    letters.sort(key=lambda x:[len(x),x])

    print('\n'.join(letters),end='')





#실행 부분
# start=time.time()
check1()
# end=time.time()

