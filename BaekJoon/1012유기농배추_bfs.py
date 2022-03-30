import sys
from collections import deque

input=sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    arr[x][y]=-1
    q.append((x,y))

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx<n) and (0<=ny<m):
                if arr[nx][ny]==1:
                    arr[nx][ny]=-1
                    q.append((nx,ny))

t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split())

    arr=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())
        arr[y][x]=1
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)
