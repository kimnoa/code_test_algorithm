from sys import stdin
from collections import Counter
import time
from collections import deque


b = list(map(int, stdin.readline().split()))


def check(b):
    Q=deque([ i+1 for i in range(b[0])])

    print("<",end="")
    while len(Q)>1:
        for _ in range(b[1]-1):
            Q.rotate(-1)
        print(Q.popleft(),end=", ")
    print(Q.popleft(),end=">")




start=time.time()
check(b)
end=time.time()


#print(f"{end-start: .8f} sec")





