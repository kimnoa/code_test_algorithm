def perfect():
    a = stdin.readline()
    count=0
    for i in a:
        if i=='(':
            count+=1
        elif i==')':
            if count == 0:
                return 1
            else:
                count-=1

    if count <1 and count>-1:
        return 0
    else:
        return 1



#input 속도 개선
from sys import stdin
#한 줄을 빠르게 입력 받음
# b= int(stdin.readline())
# a=list(map(int,stdin.readline().split()))
a = int(stdin.readline())
#b = int(stdin.readline())

for _ in range(a):
    b=perfect()
    if b==0:
        print("YES", end="")
    else:
        print("NO", end="")
    if _ <a-1:
        print()

