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

def check2(a):
    if a==1:
        print(1)
        return
    num1=0
    num2=1
    temp=-1
    for _ in range(a):
        temp = num1 + num2

        num2 = num1
        num1 = temp
    print(temp)




def check(a):
    L=[]
    for i in range(a):
        L.append(list(map(int, stdin.readline().split())))

    L.sort(key=lambda a:[a[0],a[1]])
    # print(L)
    Result=[]
    c=100001
    for i in range(a-1,-1,-1):
        if L[i][1]<=c:
            c=L[i][0]

            Result.append(L[i])
    print(len(Result))










start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





