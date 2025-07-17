from sys import stdin
from collections import Counter
import time



# a = int(stdin.readline())
a = list(map(int, stdin.readline().split()))




def check(a):
    L=[]

    # Index=[_ for _ in range(a)]
    for _ in range(a[0]):
        L+=(list(map(int, stdin.readline().split()))) #한 줄로

    counter = Counter(L)

    Max=max(counter)
    Min = min(counter)

    result_time=9999999999999
    result_floor=0
    inven=a[2]

    #블록 제거 후 쌓기
    for floor in range(Max, Min-1, -1):
        Pop=0
        Need=0
        for b in counter:
            if b>floor:
                Pop+=(b- floor)*counter[b]
            else:
                Need+=(floor-b)*counter[b]

        if Pop+inven>=Need:
            Time=Pop*2+Need
            if result_time>Time:
                result_time=Time
                result_floor=floor
    print(result_time,result_floor, end='')




start=time.time()
check(a)



end=time.time()
