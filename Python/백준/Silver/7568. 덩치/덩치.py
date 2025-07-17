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
    Q=deque()
    newQ=deque()
    rank = deque()

    for _ in range(a):
        Q.append(list(map(int, stdin.readline().split())))

    #비교
    for i in range(a):
        r=1
        S=Q.popleft()
        for _ in range(a-1):
            S2=Q.popleft()
            if S2[0]>S[0] and S2[1]>S[1]:
                r+=1
            newQ.append(S2)

        newQ.append(S)
        Q=newQ
        rank.append(r)

    for i in range(a):
        print(rank[i], end='')

        if i < a-1:
            print(" ", end='')









start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





