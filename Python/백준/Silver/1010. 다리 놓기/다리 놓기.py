count = int(input())


for c in range(count):
    
    n1=1
    n2=1
    n3=1
    a,b = map(int, input().split())
    for i in range(a):
        n1*=(i+1)
    for j in range(b):
        n2*=(j+1)
    for k in range(abs(a-b)):
        n3*=(k+1)
    if n2>n1:
        t=n1
        n1=n2
        n2=t
        
    print(int((n1//n2)//n3))
        