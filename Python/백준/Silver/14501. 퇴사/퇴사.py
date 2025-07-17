from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy

a = int(stdin.readline())
# b = int(stdin.readline())



def check2(index,counter, num_list, point, max_point):

  N=len(num_list)

  for idx in range(index+counter, N):
    if (idx + num_list[idx][0])<=N:
      point+=num_list[idx][1]

      result=check2(idx,num_list[idx][0],num_list,point,max_point)
      max_point = max(max_point, point,result)
      # print(point, max_point)

      point-=num_list[idx][1]
  return max_point





def check():
  graph=[]
  for _ in range(a):
    graph.append(list(map(int, stdin.readline().split())))
  # print(graph)
  maximum=0
  maximum=check2(-1,1,graph,0,maximum)
  print(maximum)







#실행 부분
start=time.time()
check()
end=time.time()


#print(f"{end-start: .8f} sec")

#
#
