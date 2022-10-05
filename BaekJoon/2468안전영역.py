import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

sys.setrecursionlimit(10000)

"""
1~최대높이-1까지
각 높이에 대해 잠기는 지역을 설정해놓고,
안잠긴 지역으로 dfs or bfs를 돌린다

안잠긴 지역의 갯수의 최대를 업데이트 시킴.
범위는 0~최대-1까지.

아무 지역도 물에 잠기지 않을 수도 있다. 이거떔에 괜히 헷갈림.
"""



n=int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

max_num = 0

for i in range(n):
    max_num = max(max_num, max(arr[i]))

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(arr,visit,i,j):
    visit[i][j]=True

    for a in range(4):
        nx = i+dx[a]
        ny = j+dy[a]

        if 0<=nx<n and 0<=ny<n and not visit[nx][ny]:
            if arr[nx][ny]>0:
                dfs(arr,visit,nx,ny)


cnt =0
for num in range(max_num):
    temp = arr

    for i in range(len(temp)):
        for j in range(len(temp[i])): 
            if temp[i][j]<=num:
                temp[i][j]=0
    visit = [[False]*n for _ in range(n)]
    c=0
    for i in range(n):
        for j in range(n):
            if temp[i][j]>0 and not visit[i][j]:
                c+=1         
                dfs(temp,visit,i,j)
    cnt=max(cnt,c)
print(cnt)
