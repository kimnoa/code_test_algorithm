from sys import stdin

n = int(stdin.readline())


# check(a,b)
count=0
title=666
while True:

    if str(title).find("666")>-1:
        count+=1
        # print(title)
        if count==n:
            print(title,end='')
            break
    title+=1


