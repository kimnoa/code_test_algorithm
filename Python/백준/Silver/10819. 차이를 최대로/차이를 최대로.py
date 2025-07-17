from sys import stdin

import time

N = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
idxlist = [False for i in range(N)]
newlist=[]
Max_result = -1

def check():
    total=0
    for i in range(N-1):
        total+=abs(numlist[newlist[i]]-numlist[newlist[i+1]])
    return total


def pick(Max_num):
    result=-1

    if len(newlist)==N:
        result = check()
        # print(result)
        return result#차이값 반환해야 함

    else:
        for i in range(N):
            if not idxlist[i]: #not use
                idxlist[i] = True
                newlist.append(i)
                result = pick(Max_num)
                Max_num=max(Max_num, result)
                newlist.pop()
                idxlist[i] = False

        return Max_num


def func1(): #재귀를 통하여 원소를 하나만 빼고 다음 함수로 남은 리스트 전송 반복
    print(pick(-1))


func1()


