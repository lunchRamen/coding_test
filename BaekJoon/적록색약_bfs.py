import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(1000000)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

normal=0
odd=0

def bfs(x,y):
    q=deque()
    visit[x][y]=1
    rgb=arr[x][y]
    q.append((x,y))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<n) and (0<=ny<n):
                if visit[nx][ny]==1:
                    continue
                if visit[nx][ny]==0:
                    if arr[nx][ny]==rgb:
                        #bfs에선 재귀가 없으니, while q:안에서
                        #방문여부를 처리해줘야함.
                        visit[nx][ny]=1
                        q.append((nx,ny))


n=int(input())

arr= [list(input().rstrip()) for _ in range(n)]
visit=[[0]*n for _ in range(n)]


#일반 사람 dfs
    
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if visit[i][j]==0:
            normal+=1
            bfs(i,j)

visit=[[0]*n for _ in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]=="G":
            arr[i][j]="R"

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if visit[i][j]==0:
            odd+=1
            bfs(i,j)

print(normal,odd)