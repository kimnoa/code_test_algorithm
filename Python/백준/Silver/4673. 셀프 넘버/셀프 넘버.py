from sys import stdin

def func1(a):
    num = a
    count=0 #자릿수
    L=[]
    for i in range(1,10000):
        if 1<=i<=9:
            L.append(i*2)

        elif 10<=i<=99:
            L.append(i+i//10+i%10)

        elif 100<=i<=999:
            L.append(i+i%10+(i//10)%10+i//100)

        elif 1000<=i<=9999:
            L.append(i+i%10+(i//10)%10+(i//100)%10+i//1000)

    for j in range(1,10000):
        if j not in L:
            print(j, end='')
            if j<10000-1:
                print()


func1(1)






