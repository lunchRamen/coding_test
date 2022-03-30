"""
촌수계산 bfs버전.
기본적인 생각 자체는 dfs와 동일.
다만 deque를 이용해서
deque에 (node,cnt)를 넣어서
해당 노드가 p2라면 break
아니라면 해당 노드와 연결된 노드들에 대해
0이 아니고 방문하지 않은 노드들의 경우
방문 표시를 해주고,
q.append((i,cnt+1))를 해준다.
"""

import sys
from collections import deque

input=sys.stdin.readline
num=-1
def bfs(start,cnt):
    global num
    q=deque()
    q.append((start,cnt))
    visit[start]=1

    while q:
        idx,cnt=q.popleft()
        
        if idx==p2:
            num=cnt
            break
        for i in person[idx]:
            if i==0:
                continue
            if visit[i]==1:
                continue
            visit[i]=1
            q.append((i,cnt+1))


    

n=int(input())

p1,p2=map(int,input().split())
m=int(input())

person=[[0] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    person[a].append(b)
    person[b].append(a)

bfs(p1,0)
print(num)