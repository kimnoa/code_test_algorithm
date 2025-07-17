class RollingDice:
    Dice = [0,0,0,0,0,0]
    Map = []
    x=-1
    y=-1
    cmd=-1
    r=-1
    c=-1

    def outside(self,x1, y1): #이동 후 경계 밖인지 확인
        if x1<0 or x1>=self.c:
            return 0
        if y1<0 or y1>=self.r:
            return 0
        return 1

#=======================================
    def paint(self):

        if self.Map[self.y][self.x] ==0: #바닥 = 0
            self.Map[self.y][self.x] = self.Dice[5]
        else:
            self.Dice[5] = self.Map[self.y][self.x]
            self.Map[self.y][self.x]=0

#==========================================
    def swap_num(self):
        if self.cmd==1:#동쪽
            temp=self.Dice[0]
            self.Dice[0] = self.Dice[2]
            self.Dice[2]=self.Dice[5]
            self.Dice[5]=self.Dice[4]
            self.Dice[4]=temp

        elif self.cmd==2:#서쪽
            temp = self.Dice[0]
            self.Dice[0] = self.Dice[4]
            self.Dice[4] = self.Dice[5]
            self.Dice[5] = self.Dice[2]
            self.Dice[2] = temp

        elif self.cmd==3:#북쪽
            temp = self.Dice[0]
            self.Dice[0] = self.Dice[3]
            self.Dice[3] = self.Dice[5]
            self.Dice[5] = self.Dice[1]
            self.Dice[1] = temp

        elif self.cmd==4: #남쪽
            temp = self.Dice[0]
            self.Dice[0] = self.Dice[1]
            self.Dice[1] = self.Dice[5]
            self.Dice[5] = self.Dice[3]
            self.Dice[3] = temp

#===============================================================

    def moving(self):
        if self.cmd == 1: #동쪽
            if self.outside(self.x+1,self.y): #가능
                self.swap_num()
                self.x+=1
                self.paint()
                print(RD.Dice[0])
        if self.cmd == 2: #서쪽
            if self.outside(self.x-1, self.y):
                self.swap_num()
                self.x-=1
                self.paint()
                print(RD.Dice[0])
        if self.cmd == 3: #북쪽
            if self.outside(self.x,self.y-1): #가능
                self.swap_num()
                self.y-=1
                self.paint()
                print(RD.Dice[0])
        if self.cmd == 4: #남쪽
            if self.outside(self.x, self.y+1):
                self.swap_num()
                self.y+=1
                self.paint()
                print(RD.Dice[0])


#input 속도 개선
from sys import stdin
#한 줄을 빠르게 입력 받음
# b= int(stdin.readline())
# a=list(map(int,stdin.readline().split()))
# a = int(stdin.readline())
#b = int(stdin.readline())

#init
RD=RollingDice()
a=list(map(int,stdin.readline().split()))
RD.r=a[0]
RD.c=a[1]
RD.x=a[3]
RD.y=a[2]

#map init
for _ in range(RD.r):
    RD.Map.append(list(map(int,stdin.readline().split())))

#get cmd
clist= list(map(int,stdin.readline().split()))
for _ in range(a[4]):
    RD.cmd = clist[_]
    RD.moving()
