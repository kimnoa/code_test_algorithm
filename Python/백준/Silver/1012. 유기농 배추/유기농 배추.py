from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)

a = int(stdin.readline())


def compare2(Q):
    worm=0
    while len(Q):
        worm+=1
        D=deque()
        D.append(Q.popleft())
        while len(D):
            sample=D.popleft()
            c1,r1=sample[0],sample[1]
            length=len(Q)
            for _ in range(length):
                S = Q.popleft()
                c2, r2 = S[0], S[1]
                if (abs(c2 - c1) == 1 and r1 == r2) or (abs(r2 - r1) == 1 and c1 == c2):
                    D.append(S)
                else:
                    Q.append(S)
    return worm





def check(a):
    for _ in range(a):
        col,row,count=map(int, stdin.readline().split())
        Q = deque()
        for _ in range(count):
            Q.append(list(map(int, stdin.readline().split()))) #한 줄씩 저장

        # print(area(Q))
        print(compare2(Q))

start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





