from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(1000000000)

def prB():
    N=int(stdin.readline())
    L=[0 for _ in range(N)]
    idx=-1

    for i in range(N):
        Str=stdin.readline().replace("\n",'')
        if Str[0]=="?":
            idx=i
        L[i]=Str

    if idx==N-1:
        Right=-1
    else:
        Right = L[idx+1][0]

    if idx==0:
        Left=-1
    else:
        Left = L[idx-1][-1]
    # print(L,Left,Right)
    M=int(stdin.readline())
    # R=[0 for _ in range(M)]
    for i in range(M):
        Str=stdin.readline().replace("\n",'')
        if Str not in L:
            if idx==0 and N==1:
                print(str(Str),end='')
                return

            elif idx ==0 and Str[-1] == Right:
                print(str(Str),end='')
                return
            elif idx == N-1 and Str[0] == Left:
                print(str(Str), end='')
                return
            elif Str[-1] == Right and Str[0] == Left:
                print(str(Str), end='')
                return



#실행 부분
start=time.time()
prB()
end=time.time()
