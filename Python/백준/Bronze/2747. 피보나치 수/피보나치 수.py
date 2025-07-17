from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)

a = int(stdin.readline())
# b = int(stdin.readline())


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
    ohm = {'black': [0, 1], 'brown': [1, 10], 'red': [2, 100], 'orange': [3, 1000], 'yellow': [4, 10000],
           'green': [5, 100000], 'blue': [6, 1000000], 'violet': [7, 10000000], 'grey': [8, 100000000],
           'white': [9, 1000000000]}

    num=ohm[stdin.readline().replace("\n",'')][0]*10 + ohm[stdin.readline().replace("\n",'')][0]
    mult=ohm[stdin.readline().replace("\n",'')][1]

    print(num*mult)


start=time.time()
check2(a)
end=time.time()


#print(f"{end-start: .8f} sec")





