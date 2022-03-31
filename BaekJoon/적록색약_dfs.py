"""
nxn에 R G B 중 하나를 색칠.
해당 판은 몇개의 구역으로 나뉘어져있는데,
구역은 같은 색으로 칠해져있다.

같은색상이 상하좌우로 인접해있는 경우에 두 글자는 같은 구역에 속한다.
->
원래는 0인걸 1로 바꾸거나, 1인걸 0으로 바꾸는 행위만 존재했었는데,
이번엔 변수가 3개(R,G,B)이다.


-> 백준 예제만 뚫는다.
내가 놓친 부분이 분명히 있다는것.
-> 찾아보자.

-> 상하좌우 원소와 rgb를따져볼떄, 굳이 인자로 가져오는것이
아니라, dfs index인자를 통해 rgb를 구하고, 그게 nx,ny와 같으면
재귀호출을 해주면 됐다.

그리고 dfs호출을 해주는 조건이, "방문 안한 원소"를 기준으로
했어야 했음.
나는 처음에 색깔이 같은 원소로 dfs를 돌렸었는데, 이러면
다른 tc를 통과하지못하는듯.
"""

import sys

input=sys.stdin.readline
sys.setrecursionlimit(1000000)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

normal=0
odd=0

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return
    
    visit[x][y]=1
    rgb=arr[x][y]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if (0<=nx<n) and (0<=ny<n):
            if visit[nx][ny]==1:
                continue
            if arr[nx][ny]==rgb:
                dfs(nx,ny)

n=int(input())

arr= [list(input().rstrip()) for _ in range(n)]
visit=[[0]*n for _ in range(n)]


#일반 사람 dfs
    
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if visit[i][j]==0:
            normal+=1
            dfs(i,j)

visit=[[0]*n for _ in range(n)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j]=="G":
            arr[i][j]="R"

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if visit[i][j]==0:
            odd+=1
            dfs(i,j)

print(normal,odd)
