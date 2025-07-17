def naci(n):
    a=0
    b=1
    if (n==1):
        print(0,1)
        return
    if (n==0):
        print(1,0)
        return
    for i in range(n-1):
        t=a+b
        a=b
        b=t
    print(a,b)
    
count = int(input())
for c in range(count):
    num = int(input())
    naci(num)
