from sys import stdin
import time



a = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())


def check(a):
    #도화지
    L=[]
    for _ in range(100):
        L.append([0 for _ in range(100)])

    #검은 영역
    size=0
    for _ in range(a):
        b = list(map(int, stdin.readline().split()))
        for r in range(b[1],b[1]+10):
            for c in range(b[0],b[0]+10):
                if L[r][c]==0:
                    size+=1
                    L[r][c]=1

    print(size,end='')




start=time.time()
check(a)



end=time.time()
