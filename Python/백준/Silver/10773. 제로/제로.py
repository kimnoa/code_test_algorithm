

#input 속도 개선
from sys import stdin
#한 줄을 빠르게 입력 받음
b= int(stdin.readline())

L=[]
total=0
for i in range(b):
    a = int(stdin.readline())
    if a ==0:
        total-=L.pop()
    else:
        L.append(a)
        total+=a
print(total, end='')


