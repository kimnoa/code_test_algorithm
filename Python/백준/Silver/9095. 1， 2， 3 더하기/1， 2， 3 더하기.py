from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy

a = int(stdin.readline())
# b = int(stdin.readline())



def check2(num,sub, counter):
    if num<sub:
        return 0
    elif num==sub:
        return 1
    else:
        new_counter = 0
        new_num = num-sub
        new_counter+=check2(new_num,1,new_counter)
        new_counter += check2(new_num, 2, new_counter)
        new_counter += check2(new_num, 3, new_counter)

    return new_counter



def check(a):
    new_b=0
    for _ in range(a):
        b=int(stdin.readline())
        c=0
        new_b=b
        print(check2(new_b,1,c)+check2(new_b,2,c)+check2(new_b,3,c))


    # numlist=a[1:]
    # newlist=[]
    # for r in range(0, len(numlist)-5):
    #     Fn(1,r, numlist)



start=time.time()
check(a)
end=time.time()


# print(f"{end-start: .8f} sec")





