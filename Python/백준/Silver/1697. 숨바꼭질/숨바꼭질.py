from sys import stdin
from collections import Counter
import time
from collections import deque

d = list(map(int, stdin.readline().split()))


def move(start,end): #a가 시작점, b가 끝점

    a=end
    b=start
    if a<=b:
        return b-a

    elif (a//2)<=b:
        c4 = abs(a-b)
        if a%2:
            c1=abs((a+1)//2-b)+2
            c2=abs((a-1)//2-b)+2
            return min(c1, c2,c4)
        else:
            c3=abs(a//2-b)+1
            return min(c3,c4)

    else:
        if a % 2:
            d1 = move(b,(a - 1) // 2) + 2
            d2 = move(b,(a + 1) // 2) + 2
            return min(d1,d2)
        else:
            return move(b,a//2)+1


def check(d):
    print(move(d[0],d[1]),end='')

start=time.time()
check(d)
end=time.time()






