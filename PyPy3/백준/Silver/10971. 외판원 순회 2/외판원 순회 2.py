from sys import stdin
from itertools import permutations

n,cost=int(stdin.readline()),0
city,result=[],1000000*n
order=[i for i in range(n)]

for i in range(n):
    city.append(list(map(int,stdin.readline().split())))

for i in permutations(order,n):
    if(city[i[-1]][i[0]]!=0):
        for j in range(n-1):
            if(city[i[j]][i[j+1]]==0):
                cost=0
                break
            cost+=city[i[j]][i[j+1]]
        if(cost!=0):
            cost+=city[i[-1]][i[0]]
            #result=min(cost,result)
            if(result>cost):
                result=cost
    cost=0
print(result)