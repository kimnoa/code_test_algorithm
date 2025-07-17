from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)

# a = int(stdin.readline())
# b = int(stdin.readline())

a = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
# b = int(stdin.readline())
# a = list(stdin.readline().replace("\n",'').split())

# L=[0 for _ in range(9)]

# for i in range(9):
#     n = int(stdin.readline())
#     L[i]=n


def check(a):
    A=[]
    for _ in range(a[0]):
        A.append(list(map(int, stdin.readline().split())))


    b = list(map(int, stdin.readline().split()))
    B=[]
    for _ in range(b[0]):
        B.append(list(map(int, stdin.readline().split())))

    for r in range(a[0]):
        for c in range(b[1]):
            total=0
            for i in range(a[1]):
                total+=A[r][i]*B[i][c]
            print(total, end='')
            if c < b[1]-1:
                print(" ",end='')
        if r < a[0] - 1:
            print()




start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





