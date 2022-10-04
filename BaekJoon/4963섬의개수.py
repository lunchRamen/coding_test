import sys

input = sys.stdin.readline
INF = sys.maxsize

"""
로직 자체는 바로 생각났는데
nx = x+dx[i]
ny = x+dy[i]로 해서 뻘짓거리 30분함.
"""

sys.setrecursionlimit(10000)

def dfs(arr,visit,x,y):
    dx = [1,1,1,-1,-1,-1,0,0]
    dy = [1,-1,0,1,-1,0,1,-1]
    
    visit[x][y]=True

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<len(arr) and 0<=ny<len(arr[0]):
            if arr[nx][ny]==1 and visit[nx][ny]==False:
                dfs(arr,visit,nx,ny)
    
while True:
    w,h = map(int,input().split())

    if w==0 and h == 0 :
        break
    arr = []

    for _ in range(h):
        arr.append(list(map(int,input().split())))
    
    cnt = 0
    visit = [[False]*w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j]==1 and visit[i][j]==False:
                cnt+=1
                dfs(arr,visit,i,j)
    print(cnt)
