from sys import stdin

n = int(stdin.readline())
# arr = list(map(int, stdin.readline().split()))
# c = int(stdin.readline())

L=[]

for i in range(n):
    c = int(stdin.readline())
    if c not in L:
        L.append(c)
L.sort()
for i in range(n):
    print(L[i], end='')
    if i<n-1:
        print()
