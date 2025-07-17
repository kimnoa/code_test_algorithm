from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy



def Fn(index, num_list,new_list): #depth는 new_list의 원소 수로 대체함

    #index는 이전에 넣은 문자의 인덱스

    N=len(num_list)
    D=len(new_list)
    step=0 #가능한 단계수

    # print(new_list_copy, depth)

    for idx in range(index+1,N+D-5): #이제 D+1번째 문자 넣음
        new_list.append(num_list[idx])

        if len(new_list)==6: #6개가 다 차면 출력
            print(' '.join(map(str, new_list)))
            # new_list.pop() #다시 원상복귀
            # step+=1

        else: #아직 6개가 안 되었으면 다음 단계
            Fn(idx,num_list,new_list)
            # step +=

        new_list.pop() #넣었던 것 제거s

    # return step #현재까지 가능한 단계 반환





def check2():
    while True:
        a = list(map(int, stdin.readline().split()))
        if a[0]:
            numlist=a[1:]
            newlist=[]
            Fn(-1,numlist,newlist)
            print()
        else:
            break



start=time.time()
check2()
end=time.time()


# print(f"{end-start: .8f} sec")





