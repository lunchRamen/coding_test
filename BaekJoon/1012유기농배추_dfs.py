"""
아파트 단지처럼 무리를 지어있는게 몇무리나 있는지 묻는 문제.
무리를 확인 할 수 있는 방법
=visit배열을 만들어 놓은 다음, 다 0으로 만듬
그래서 arr[i][j]가 1인경우 -1로 바꾸고 상하좌우로 재귀.


"""

import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if arr[nx][ny]==1:
                arr[nx][ny]= -1
                dfs(nx,ny)
    

t=int(input())

while t:
    m,n,num=map(int,input().split())
    arr=[[0]*m for _ in range(n)]

    for _ in range(num):
        x,y=map(int,input().split()) #행 열
        arr[y][x]=1 #열 행
    group=0
    for i in range(n):#열
        for j in range(m):#행
            if arr[i][j]==1:
                dfs(i,j)
                group+=1
    print(group)
    t-=1

