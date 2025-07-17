from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(1000000000)
# import copy

# a = int(stdin.readline())
# b = int(stdin.readline())


# a = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
# b = int(stdin.readline())
# d= list(map(int, stdin.readline().split()))
# c = list(stdin.readline().replace("\n",'').split())

# L=[0 for _ in range(9)]

# for i in range(9):
#     n = int(stdin.readline())
#     L[i]=n


# class Forest:
#     Field=deque()
#     Tree=deque()
#     Bot = deque()
#     Dead = deque(0 for _ in range(100000))
#     Year=0
#     row=0
#     # col=0 #col=row
#     life=0
#     dead=0
#     dir = deque([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]])
#
#     def get_field_tree(self):
#         self.row, self.life, self.Year = map(int, stdin.readline().split())
#
#         self.Bot = deque(0 for _ in range(self.row))
#         self.Field = deque(0 for _ in range(self.row))
#
#         for i in range(self.row):
#             self.Bot[i] = deque(map(int, stdin.readline().split()))
#             self.Field[i] = deque(5 for _ in range(self.row))
#
#         self.Tree=deque(0 for _ in range(self.life))
#         for i in range(self.life):
#             self.Tree[i] = list(map(int, stdin.readline().split()))
#
#         self.Tree=deque(sorted(self.Tree, key=lambda x: x[2]))
#
#         # self.Bot= deque(deque(list(map(int, stdin.readline().split()))) for __ in range(self.row))
#         # self.Field=deque(deque([5 for _ in range(self.row)]) for __ in range(self.row))
#
#         # treedata = []
#         # for _ in range(self.life):
#         #     treedata.append(list(map(int, stdin.readline().split())))
#         # treedata.sort(key=lambda x:x[2])
#         # self.Tree.extend(treedata)
#
#
#
#     def spring(self): #양분 먹기 & 죽은 나무는 양분으로
#         New = deque()
#         newlife=0
#         for i in range(self.life):
#             tree1 = self.Tree[newlife] #tree 하나 가져오기
#             x,y,year = tree1
#             if self.Field[x-1][y-1]>=year:
#                 self.Field[x-1][y-1]-=year
#                 year+=1
#                 self.Tree[0][2]+=1
#                 # self.Tree.rotate(-1)
#
#                 if not year % 5:  # 번식하는 나무
#                     for j in range(8):
#                         dx, dy = self.dir[j]
#                         if 1 <= (x + dx) <= self.row and 1 <= (y + dy) <= self.row:  # in range
#                             self.Tree.appendleft([x + dx, y + dy, 1])
#                             self.life += 1
#                             newlife+=1
#
#                         # self.dir.append([dx,dy])
#                 # self.Tree.append(tree5)
#
#
#             else:
#                 self.Tree.popleft()
#                 self.Dead[self.dead] = [x,y,year]
#
#                 self.life-=1
#                 self.dead+=1
#         # print(self.dead)
#
#         self.Tree.extendleft(New)
#
#         #여름, 겨울
#         for j in range(self.dead):
#             self.dead-=1
#             x,y,year = self.Dead[self.dead]
#             self.Field[x - 1][y - 1] += (year // 2)
#
#         for r in range(self.row):
#             for c in range(self.row):
#                 self.Field[r][c] += self.Bot[r][c]
#
#
#         # newlife=0
#
#         # for i in range(self.life-1,-1,-1):
#         #     x,y,year=self.Tree[i]
#
#
#
#         if self.life: #생존한 나무가 있는가
#             return 1
#         else:
#             return 0
#
#
#     # def summer(self):
#     #     for _ in range(self.dead):
#     #         dead_tree = self.Dead.popleft()
#     #         x,y,year = dead_tree
#     #         self.Field[x-1][y-1]+=(year//2)
#     #
#     #     self.dead=0
#
#
#     # def fall(self):
#     #     New=deque()
#     #     # newlife=0
#     #
#     #     for i in range(self.life):
#     #         x,y,year=self.Tree[i]
#     #
#     #         if not year%5: #번식하는 나무
#     #             for j in range(8):
#     #                 dx,dy = self.dir[j]
#     #                 if 1<=(x+dx)<=self.row and 1<=(y+dy)<=self.row: #in range
#     #                     New.appendleft([x+dx,y+dy,1])
#     #                     self.life+=1
#     #                     # newlife+=1
#     #
#     #                 # self.dir.append([dx,dy])
#     #         # self.Tree.append(tree5)
#     #     self.Tree.extendleft(New)
#
#
#
#     #
#     # def winter(self):
#     #     for r in range(self.row):
#     #         for c in range(self.row):
#     #             self.Field[r][c]+=self.Bot[r][c]
#
#             # Field_row = self.Field.popleft()
#             # Bot_row = self.Bot.popleft()
#             # for __ in range(self.row):
#             #     num = Field_row.popleft()
#             #     num2 = Bot_row.popleft()
#             #     Field_row.append(num+num2)
#             #     Bot_row.append(num2)
#             # self.Field.append(Field_row)
#             # self.Bot.append(Bot_row)
#
# # def check2(Items,index,Max_size,Max_point,now_size,now_point): #이번에 index를 넣으려고 할 때,
# #     checker=0
# #     if now_size+Items[index][0]<=Max_size:
# #         now_size+=Items[index][0]
# #         now_point+=Items[index][1]
# #         Max_point = max(Max_point, now_point)
# #         for i in range(index+1, len(Items)):
# #             checker=check2(Items,i,Max_size,Max_point,now_size,now_point)
# #             # if not checker:
# #             #     break
# #             # else:
# #             Max_point = max(Max_point, now_point,checker)
# #         # now_point-=Items[index][1]
# #         # now_size-=Items[index][0]
# #
# #     # else:
# #         # return 0
# #     return Max_point
#
#
#
# def check1(L): #a,c,b,d
#     total=0
#     for i in range(len(L)-1):
#         total += abs(L[i]-L[i+1])
#     return total



#
# def check(): #a,c
#     new_list=[0 for _ in range(len(a))]
#     black_list=[]
#
#     idx=1
#     for x in range(a-1):
#         new_list[0]=c[x]
#         black_list.append(c[x])
#         for y in range(x+1,a):
#             new_list[a-1]=c[y]
#             black_list.append(c[y])
#
#             list2=[i for i in c if i not in black_list]
#             for _ in range(len(list2)):
#                 for id in range(len(list2)):
#                     if id
#
#
# def baseball():
#     for _ in range(a): #a번 문장을 받음

# def socks():
#     L = [0 for _ in range(10)]
#
#     for _ in range(5):
#         a = int(stdin.readline())
#         if L[a]:
#             L[a]+=1
#         else:
#             L[a]-=1
#
#     for b in range(10):
#         if L[b]:
#             print(b,end='')

def prB():
    counter = int(stdin.readline())
    namelist=set(["ChongChong"])
    # dancing=0
    # enter = list("ENTER")
    for _ in range(counter):
        c1, c2 = stdin.readline().split()
        if c1 in namelist or c2 in namelist:
            namelist.add(c1)
            namelist.add(c2)

        # print(namelist)




    print(len(namelist),end='')



# def prbD():
#     num=int(stdin.readline())
#     L = list(map(int, stdin.readline().split()))
#     R = list(map(int, stdin.readline().split()))
#
#     for i in range(num)

# def rec(index, List,newlist,K): #개수 return
#     checker=0
#     counter=0
#
#     for i in range(index,len(List)):
#         newlist.append(List[i])
#
#         if len(newlist)>1:
#             for j in range(len(newlist)-1):
#                 if not (newlist[j]+newlist[-1])%K:
#
#                     checker+=1
#                     break
#
#             if not checker:
#                 print(newlist)
#                 counter+=1
#     #다음 단계
#
#         counter+=rec(i+1,List,newlist,K)
#
#         newlist.pop()
#
#     return counter

# def prH():
#     row,col,cmd = map(int, stdin.readline().split())
#     L = [[0 for _ in range(col)] for __ in range(row)]
#     for i in range(cmd):
#         C,num,v = map(int, stdin.readline().split())
#
#         if C==1:
#             for j in range(col):
#                 L[num-1][j]+=v
#
#         else:
#             for j in range(row):
#                 L[j][num-1]+=v
#
#     for i in range(row):
#         print(' '.join(map(str,L[i])))









# def probE():
#     N,K = map(int, stdin.readline().split())
#     L=list(map(int, stdin.readline().split()))
#     total=rec(0,L,[],K)
#     print(total%(1000000007),end='')











#실행 부분
start=time.time()
prB()
end=time.time()


# print(f"{end-start: .8f} sec")

#
#
