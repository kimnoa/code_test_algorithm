from sys import stdin
import time

n = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())

def check(n):
    _3=-1
    _5=0
    now=n
    for count in range(0,n+1,5):
        if (now-count)%3==0:
            _3=(now-count)//3
            _5=count//5
    print(_3+_5, end='')


start=time.time()
check(n)



end=time.time()

