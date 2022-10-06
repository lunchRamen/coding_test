import sys
from collections import deque,defaultdict

input = sys.stdin.readline
INF = sys.maxsize

sys.setrecursionlimit(10000)

"""
visit함수를 딕셔너리로 대체.
만약 dic[alpha]가 있다면, 방문한것으로 판단.
여기서 헷갈렸었는데,
"백트랙킹"을 구현하기 위해(조건에 막혀서 이전 재귀로 돌아갔을때, 상태를 유지해주기위해)
조건에 맞으면 
dic[arr[nx][ny]]=1로 하고
dfs를 돌리고
del dic[arr[nx][ny]]를 해줘야 if arr[nx][ny] not in dic에 걸리지 않는다.
dic[arr[nx][ny]]=0이면 걸린다. (딕셔너리에선 0이 False가 되지않는다.)

"""


n , m = map(int,input().split())


arr = [list(input().rstrip()) for _ in range(n)]

dic = defaultdict(int)
dic[arr[0][0]]=1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
count_ = 1

def dfs(x,y,arr,dic,cnt):
    print(x,y,dic)
    global count_
    count_ = max(count_,cnt)

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if not arr[nx][ny] in dic:
                dic[arr[nx][ny]]=1
                dfs(nx,ny,arr,dic,cnt+1)
                del dic[arr[nx][ny]]
            

dfs(0,0,arr,dic,1)

print(count_)
