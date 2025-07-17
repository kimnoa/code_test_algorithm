from sys import stdin

# n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())

L=[0 for _ in range(a[0])]

for i in range(a[1]):
    b = list(map(int, stdin.readline().split()))
    for j in range(b[0],b[1]+1):
        L[j-1]=b[2]

for i in range(len(L)):
    print(L[i], end='')
    if i<a[0]-1:
        print(" ", end='')
