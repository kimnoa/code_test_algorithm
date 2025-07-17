from sys import stdin
import time



a = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
# b = list(map(int, stdin.readline().split()))
b = int(stdin.readline())

# L=[0 for _ in range(9)]

# for i in range(9):
#     n = int(stdin.readline())
#     L[i]=n



def check(a,b):
    #좌표 설정
    L=[]
    for _ in range(a):
        L.append([0 for _ in range(a)])

    if a==1:
        #숫자 1의 좌표
        q_r=0
        q_c=0
        L[0][0]=1

    else:
        now=1
        p_r= a//2
        p_c= (a-1)//2
        L[p_r][p_c] = 1

        if now == b:
            q_r = p_r
            q_c = p_c
        #제곱수를 기준으로 입력하기
        now+=1
        for i in range(2,a+1):
            if i%2==0:
                p_r-=1
            else:
                p_r+=1
            L[p_r][p_c]=now
            if now== b:
                q_r=p_r
                q_c=p_c
            now+=1

            #가로
            for _ in range(i-1):
                if i % 2 == 0:
                    p_c += 1
                else:
                    p_c -= 1
                L[p_r][p_c]=now
                if now == b:
                    q_r = p_r
                    q_c = p_c
                now+=1

            #세로
            for _ in range(i-1):
                if i % 2 == 0:
                    p_r += 1
                else:
                    p_r -= 1
                L[p_r][p_c] = now
                if now == b:
                    q_r = p_r
                    q_c = p_c
                now += 1

    #출력하기
    for _ in range(a):
        print(*L[_], sep=" ",end="\n")
    print(q_r+1, q_c+1, end='')


start=time.time()
check(a,b)



#     print(L[i], end='')
# # for i in range(9):
# #     print(count, end='')
#     if i<7-1:
#         print()

end=time.time()

#print(f"{end-start: .8f} sec")