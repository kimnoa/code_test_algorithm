from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy

# a = int(stdin.readline())
# b = int(stdin.readline())



a = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
# b = int(stdin.readline())
c = list(stdin.readline().replace("\n",'').split())



def check1(A_list):

  counter = 0
  if 'a' in A_list:
    counter += 1
  if 'e' in A_list:
    counter += 1
  if 'i' in A_list:
    counter += 1
  if 'o' in A_list:
    counter += 1
  if 'u' in A_list:
    counter += 1
  counter2=len(A_list)-counter
  if counter>=1 and counter2>=2:
    print(''.join(map(str, A_list)))

def check2(index, num_list, new_list):

  N=len(num_list)
  D=len(new_list)

  for idx in range(index+1, N-a[0]+D+1):
    new_list.append(num_list[idx])
    if len(new_list)==a[0]:
      check1(new_list)


    else:
      check2(idx,num_list,new_list)

    new_list.pop()






def check():
  c.sort()
  check2(-1,c,[])




#실행 부분
start=time.time()
check()
end=time.time()


# print(f"{end-start: .8f} sec")
