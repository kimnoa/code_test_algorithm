from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)

a = int(stdin.readline())
# b = int(stdin.readline())

# a = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
# b = int(stdin.readline())
# a = list(stdin.readline().replace("\n",'').split())

# L=[0 for _ in range(9)]

# for i in range(9):
#     n = int(stdin.readline())
#     L[i]=n


def check(a):
    for i in range(a):
        if (i+1)%2:
            for j in range(2*a-1):
                if (j + 1) % 2:
                    print("*",end='')
                else:
                    print(" ",end='')
        else:
            for j in range(2*a):
                if (j + 1) % 2:
                    print(" ",end='')
                else:
                    print("*",end='')
        if i < a-1:
            print()


start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





