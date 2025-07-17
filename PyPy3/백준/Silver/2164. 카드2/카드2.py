from sys import stdin
from collections import Counter
import time
from collections import deque


a = int(stdin.readline())


def check(a):
    Q=deque([ i+1 for i in range(a)])
    while len(Q)>2:
        Q.popleft()
        Q.rotate(-1)
    print(Q[-1])

start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





