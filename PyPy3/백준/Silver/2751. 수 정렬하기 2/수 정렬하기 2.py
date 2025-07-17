from sys import stdin
from collections import Counter
import time



a = int(stdin.readline())
# b = int(stdin.readline())




def check(a):
    L=[]
    for _ in range(a):
        L.append(int(stdin.readline()))
    L.sort()
    print(*L,sep='\n',end='')




check(a)

