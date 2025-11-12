from sys import stdin
from collections import deque
# import time
import copy


row_n, col_n = map(int,stdin.readline().split())
tile = [0 for _ in range(row_n)]
for i in range(row_n):
    tile[i] = list(map(int, stdin.readline().split()))
virus = []
wall = []
space = []
# choose walls with using "for" and find space with using BFS
# searching
for r in range(row_n):
    for c in range(col_n):
        a = tile[r][c]
        if a:
            if a>1:
                virus.append([r,c])
            else:
                wall.append([r,c])
        else:
            space.append([r,c])

#wall
space_n = len(space)
dir_4 = [[-1,0],[0,1],[0,-1],[1,0]]

# steps = 0 #check complexity

min_s2v = space_n #max value
for i in range(space_n-2):
    for j in range(i+1, space_n-1):
        for k in range(j+1, space_n):
            wall_added_tile = copy.deepcopy(tile)
            wall_added_tile[space[i][0]][space[i][1]] = 1
            wall_added_tile[space[j][0]][space[j][1]] = 1
            wall_added_tile[space[k][0]][space[k][1]] = 1

            change_space_to_virus = 0
            virus_q = deque(virus)
            while True:
                now_virus = virus_q.popleft()
                next_virus = []
                for dir_r, dir_c in dir_4:
                    # steps+=1
                    next_r = now_virus[0] + dir_r
                    next_c = now_virus[1]+dir_c
                    if 0<=next_r<row_n and 0<=next_c<col_n:
                        if wall_added_tile[now_virus[0]+dir_r][now_virus[1]+dir_c] == 0:
                            wall_added_tile[now_virus[0]+dir_r][now_virus[1]+dir_c] = 2
                            virus_q.append([now_virus[0]+dir_r,now_virus[1]+dir_c])
                            change_space_to_virus+=1
                if len(virus_q)<1:
                    break

            if change_space_to_virus < min_s2v:
                min_s2v = change_space_to_virus


print(space_n - min_s2v - 3)
# print(steps)





