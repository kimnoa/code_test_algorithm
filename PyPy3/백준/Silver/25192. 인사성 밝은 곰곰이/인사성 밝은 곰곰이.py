from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(1000000000)
# import copy

def prB():
    counter = int(stdin.readline())
    namelist=set()
    img=0
    enter = list("ENTER")
    for _ in range(counter):
        cmd = stdin.readline().rstrip("\n")
        for i in range(len(cmd)):
            if cmd == "ENTER":
                namelist=set()
            elif cmd not in namelist:
                img+=1
                namelist.add(cmd)
                # print(namelist)

    print(img,end='')




#실행 부분
start=time.time()
prB()
end=time.time()



#
#
