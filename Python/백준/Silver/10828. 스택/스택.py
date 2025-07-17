from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)

a = int(stdin.readline())
# b = int(stdin.readline())





class Queue:
    Q=deque()

    def push(self, num):
        self.Q.append(num)

    def pop(self):
        if len(self.Q):
            print(self.Q.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.Q))

    def empty(self):
        if len(self.Q):
            print(0)
        else:
            print(1)

    def top(self):
        if not len(self.Q):
            print(-1)
        else:
            print(self.Q[-1])



def check(a):
    Q1=Queue()
    for _ in range(a):
        cmd= stdin.readline().split()

        if cmd[0]=='push':
            Q1.push(int(cmd[1]))

        if cmd[0]=='pop':
            Q1.pop()

        if cmd[0]=='size':
            Q1.size()

        if cmd[0]=='empty':
            Q1.empty()

        if cmd[0]=='top':
            Q1.top()











start=time.time()
check(a)
end=time.time()


#print(f"{end-start: .8f} sec")





