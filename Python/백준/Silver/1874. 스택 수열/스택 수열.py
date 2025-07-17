from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy


def check1():
    num = int(stdin.readline())

    S = []
    top = -1
    now = 1
    result = []
    err = 0
    I = [0 for _ in range(num)]

    for a in range(num):
        I[a]=int(stdin.readline())

    for a in I:
        while len(S) == 0 or a != S[top]: #스택이 비거나 지금 필요한 것이 stack안에 없을 때
            if now > num: #다 넣었을 때
                err += 1
                break
            else:
                S.append(now)
                # top += 1
                now += 1
                result.append('+')
        if err > 0: #불가능한 경우
            break

        S.pop()#필요한 것이 스택 위에 있을 때
        # top -= 1
        result.append('-')

    if err > 0:
        print("NO", end="")
    else:

        print('\n'.join(result),end='')






# def check2(index,counter, num_list, point, max_point):









#실행 부분
# start=time.time()
check1()
# end=time.time()

