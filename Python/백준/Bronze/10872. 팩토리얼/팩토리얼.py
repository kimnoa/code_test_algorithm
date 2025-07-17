from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
# sys.setrecursionlimit(100000)

a = int(stdin.readline())

def check2(a,total):
    if a<2:
        print(total)
    else:
        check2(a-1,total*a)



def check(a):
    total=1
    check2(a,total)



start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





