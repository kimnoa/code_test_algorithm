def perfect(num):
    if num == 1:
        return 0
    for _ in range(2,num):
        if num%_==0:
            return 0
    return 1

#input 속도 개선
from sys import stdin
#한 줄을 빠르게 입력 받음
b= int(stdin.readline())
# a=list(map(int,stdin.readline().split()))
a = int(stdin.readline())
#b = int(stdin.readline())
L=[]
c=0
total = 0
for n in range(b,a+1):
   if perfect(n):
        L.append(n)
        c+=1
        total+=n
if c == 0:
    print(-1, end="")
else:
    print(total)
    print(min(L), end="")


