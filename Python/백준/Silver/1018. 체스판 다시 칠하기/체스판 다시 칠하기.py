from sys import stdin
from collections import Counter
import time



# a = int(stdin.readline())
# b = int(stdin.readline())

b = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
# b = int(stdin.readline())

# L=[0 for _ in range(9)]

# for i in range(9):
#     n = int(stdin.readline())
#     L[i]=n



def check(b):
    L=[]
    #입력
    for _ in range(b[0]):
        L.append(stdin.readline().replace('\n',''))

    #자르기

    Min=99999999
    for i in range(b[0]-7):
        for j in range(b[1]-7):
            cut = []
            total = 0
            count=0
            for ii in range(8):
                for jj in range(8):
                    count+=1
                    # print(ii+i,jj+j)
                    # print(L[ii+i][jj+j])
                    cut.append(L[i+ii][j+jj])


            for k in range(len(cut)):
                if (k//8+k%8)%2==0:
                    if cut[k]=='W':
                        total+=1
                else:
                    if cut[k]=='B':
                        total+=1
            Min=min(Min,total)
    #색칠-W
            total=0
            for k in range(len(cut)):
                if (k//8+k%8)%2==0:
                    if cut[k]=='B':
                        total+=1
                else:
                    if cut[k]=='W':
                        total+=1
            Min = min(Min, total)
    print(Min)







start=time.time()
check(b)




#     print(L[i], end='')
# # for i in range(9):
# #     print(count, end='')
#     if i<7-1:
#         print()

end=time.time()



