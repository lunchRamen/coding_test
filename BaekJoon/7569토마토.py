import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

sys.setrecursionlimit(10000)

"""
처음에 떠올랐던건 bfs가 아니라
0이 있는지 체크하는 함수
익을수 없는지 체크하는 함수

이후 while문을 돌면서
0이 없을때까지 while을 돌면서 체크한 후, cnt를 구하는거였는데, 예시는 맞췄지만 정답은 아니였음
왜 틀렸는지는 모르겠다.

그래서 bfs로 구현하는걸 찾음.
"""



n,m,h = map(int,input().split())

arr = []


for _ in range(h):
    temp = []
    for _ in range(m):
        temp.append(list(map(int,input().split())))
    arr.append(temp)

#check_arr이 True로 나올때까지, dfs를 돌린다

dir_ = [[1,0,0],[0,1,0],[-1,0,0],[0,-1,0],[0,0,1],[0,0,-1]]

q = deque()
cnt = 0

def bfs():
    while q:
        x,y,z = q.popleft()

        for i in range(6):
            nx = x+dir_[i][0]
            ny = y+dir_[i][1]
            nz = z+dir_[i][2]

            if 0<=nx<h and 0<=ny<m and 0<=nz<n:
                if arr[nx][ny][nz]==0:
                    q.append([nx,ny,nz])
                    arr[nx][ny][nz] = arr[x][y][z]+1


for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k]==1:
                q.append([i,j,k])

bfs()

for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k]==0:
                print(-1)
                exit(0)
            cnt= max(cnt,arr[i][j][k])
print(cnt-1)
