class RollingDice:
    Map = []
    x=-1
    y=-1
    r=-1
    c=-1
    turn=-1
    end=0
    move=0

    def cleaner(self):
        while self.end==0:

            _x=0
            _y=0
            if self.Map[self.y][self.x]==0:
                self.Map[self.y][self.x]=-1
                self.move+=1

            elif self.Map[self.y-1][self.x]==0 \
                or self.Map[self.y+1][self.x]==0 \
                or self.Map[self.y][self.x-1]==0 or \
                self.Map[self.y][self.x+1]==0:

                self.turn= (self.turn+3)%4
                if self.turn%2:
                    _x=2-self.turn
                else:
                    _y=self.turn-1

                if self.Map[self.y+_y][self.x+_x]==0:
                    self.x+=_x
                    self.y+=_y
            else:
                if self.turn%2:
                    _x=2-self.turn
                else:
                    _y=self.turn-1

                if self.Map[self.y-_y][self.x-_x] == 1:
                    self.end=1

                else:
                    self.x-=_x
                    self.y-=_y



#input 속도 개선
from sys import stdin
#한 줄을 빠르게 입력 받음
# b= int(stdin.readline())
a=list(map(int,stdin.readline().split()))
# a = int(stdin.readline())
#b = int(stdin.readline())
b=list(map(int,stdin.readline().split()))

Robot=RollingDice()
Robot.y=b[0]
Robot.x=b[1]
Robot.turn=b[2]

for _ in range(a[0]):
    Robot.Map.append(list(map(int,stdin.readline().split())))

Robot.cleaner()
print(Robot.move,end="")