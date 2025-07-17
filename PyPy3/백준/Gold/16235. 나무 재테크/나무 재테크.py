from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(100000)

#data type
'''
N, M, K
A[r][c]
x1, y1, z1
x2, y2, z2
...

N,M,K : int
A[r][c] : int
x, y, z : int
'''
def answer():
    #input data
    N, M, K = map(int, stdin.readline().split())
    A = [list(map(int, stdin.readline().split())) for _ in range(N)]
    Tree = sorted([list(map(int, stdin.readline().split())) for _ in range(M)], key=lambda x: x[2])
    Tree = deque(Tree)
    Field = [[5 for _ in range(N)] for _ in range(N)]
    Dead = []
    
    # Tree.sort(key=lambda x: x[2])
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for _ in range(K):
        if len(Tree) == 0:
            break
        # spring
        # print(Tree, sep=' ')
        for i in range(len(Tree)):
            tree = Tree.popleft()
            if Field[tree[0]-1][tree[1]-1] >= tree[2]:
                Field[tree[0]-1][tree[1]-1] -= tree[2]
                tree[2] += 1
                Tree.append(tree)
            else:
                Dead.append(tree)
        # summer
        # print(len(Dead))
        for i in range(len(Dead)):
            dead = Dead.pop()
            Field[dead[0]-1][dead[1]-1] += (dead[2] // 2)
        # fall
        new_tree = deque()
        for tree in Tree:
            if not tree[2] % 5:
                for d in dir:
                    if 1 <= tree[0] + d[0] <= N and 1 <= tree[1] + d[1] <= N:
                        new_tree.append([tree[0] + d[0], tree[1] + d[1], 1])
        Tree.extendleft(new_tree)
        # winter
        for i in range(N):
            for j in range(N):
                Field[i][j] += A[i][j]

    print(len(Tree), end='')

answer()