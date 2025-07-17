from sys import stdin
import time



# a = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())


def check(a):
    e=1
    s=1
    m=1
    count=1
    while not (e==a[0] and s==a[1] and m==a[2]):
        e=e%15+1
        s = s % 28 + 1
        m = m % 19 + 1
        count+=1
    print(count, end='')


start=time.time()
check(a)


end=time.time()

