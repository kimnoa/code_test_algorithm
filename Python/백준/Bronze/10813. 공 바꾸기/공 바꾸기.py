from sys import stdin

# n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())

L=[(_+1) for _ in range(a[0])]

for i in range(a[1]):
    b,c = list(map(int, stdin.readline().split()))
    tmp=L[b-1]
    L[b-1]=L[c-1]
    L[c-1]=tmp

for i in range(len(L)):
    print(L[i], end='')
    if i<a[0]-1:
        print(" ", end='')
