import sys
import bisect
from collections import deque,defaultdict

input = sys.stdin.readline
INF = sys.maxsize

sys.setrecursionlimit(10**5)
"""
단지번호붙이기와 동일한 문제라고 생각.
다만 다른점은, 직사각형이 주어지고 그 직사각형만큼 못쓰는 땅이라는 것.
->그리고 헷갈렸던게 계속 max로 값을 갱신해주려고 했는데, 그게 아니다.
    dfs가 끝날때까지 땅넓이를 1씩 늘려나가고, 다 끝나면 그걸 배열에 더해주면 된다.
"""


n,m,k = map(int,input().split())


arr = [[0 for _ in range(m)] for _ in range(n)]
visit = [[False for _ in range(m)] for _ in range(n)]
num_cnt = []

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())

    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j]=1

dx =[1,-1,0,0]
dy= [0,0,-1,1]
cnt=0
compare_cnt=0

def dfs(x,y):
    global compare_cnt
    
    visit[x][y]=True
    compare_cnt+=1

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and arr[nx][ny]==0:
            dfs(nx,ny)


for i in range(n):
    for j in range(m):
        if arr[i][j]==0 and not visit[i][j]:
            cnt+=1
            compare_cnt=0
            dfs(i,j)
            num_cnt.append(compare_cnt)
        
print(cnt)
num_cnt.sort()
print(*num_cnt)
