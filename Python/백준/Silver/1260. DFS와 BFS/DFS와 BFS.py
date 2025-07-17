from sys import stdin
#from collections import Counter
import time
from collections import deque
import sys
sys.setrecursionlimit(100000)
import copy



def make_graph():

    node,edge,start_ = map(int, stdin.readline().split())

    #visit 생성
    visit = list([False for _ in range(node)])

    #graph 생성
    graph=deque([ [] for _ in range(node)])

    #edge 추가
    for _ in range(edge):
        left,right = map(int, stdin.readline().split())
        if right not in graph[left-1]:
            graph[left-1].append(right)
            graph[right - 1].append(left)

    #sort
    for i in range(node):
        element=graph.popleft()
        element.sort()
        graph.append(element)

    # print(graph) #확인용
    # print(visit)
    return graph, visit, start_



def DFS(Graph, Visit, Start):
    Stack=[]
    move=[Start]
    now = Start
    Visit[now-1]=True
    index=0
    while True:
        if index < len(Graph[now-1]): #check list range
            next_node = Graph[now-1][index]
            if not Visit[next_node-1]: #not visited
                Visit[next_node-1]=True
                Stack.append([now,index]) #현위치, index 저장
                now=next_node
                move.append(now)
                # print(move)
                # print(Visit)
                index=0

            else: #already visited
                index+=1 #next edge

        else: #이 노드의 모든 edge 이동 완료
            if len(Stack): #처음 위치가 아닌가?
                now,index=Stack.pop() #이전 위치로 이동
                index+=1
            else: #모든 노드 탐색 완료
                break

    print(' '.join(map(str,move)))

def BFS(Graph, Visit, Start):
    Queue=deque([Start])
    move=[Start]
    now = Start
    Visit[now-1]=True

    while True:
        # print(move)
        now=Queue.popleft()
        for next_node in Graph[now-1]:
            if not Visit[next_node - 1]:
                Visit[next_node - 1] = True
                Queue.append(next_node)  # 다음 위치 저장
                move.append(next_node)
            # print(Queue, move,Visit)
        if not len(Queue):
            break

        #다 넣으면 다음 노드로 이동
        # now=Queue.popleft()


    print(' '.join(map(str,move)),end='')





def check():
  graph, visit, start_ = make_graph()
  DFS(graph,copy.deepcopy(visit),start_)
  BFS(graph, visit, start_)


#실행 부분
start=time.time()
check()
end=time.time()

