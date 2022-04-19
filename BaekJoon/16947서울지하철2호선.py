import sys
from collections import deque

input=sys.stdin.readline
sys.setrecursionlimit(100000)

"""
사이클을 찾는것(dfs)
사이클로부터 사이클이 아닌 노드까지의 거리(bfs)

이렇게 2단계로 풀어야함.
보통 첫번째 단계에서 현재단계,현재단계까지 걸리는 역의 갯수로 따져서
현재 역까지 2단계 이상이면 사이클이 형성될수 있는걸로 하는데,

나같은 경우 백준 풀이로 풀었다.
첫번째 노드를 입력하면, 해당 노드와 연결된 노드들이 재귀호출 된다.
그 노드는 방문한적 있는 노드가 있을때까지, 호출된다.
방문을 했다면, 사이클이 있다는 것이니까 해당 정점을 return
그래서 for문으로 재귀를 계속 호출하는데,
res의 return값이 0이상인것(=사이클인것)만 2로 해서 사이클임을 표시
아니라면 그냥 초기값이 있게끔.

그다음 visit을 돌면서 dist에 사이클인 경우 0을 넣고, q에 넣는다.
사이클이 아니면, -1을 넣는다. (왜냐하면 사이클의 0과 구분되는 수가 필요하고,
어차피 dist[x]+1로 할거라 1부터 시작한다)
그래서 dist[x]가 -1인경우에 대해 bfs를 돌리면? 끝.
"""
def dfs(x,p):
    global visit
    global dist
    global arr

    if visit[x]==1: return x
    visit[x]=1

    for y in arr[x]:
        if y==p: continue
        res=dfs(y,x)
        if res == -2: return -2
        if res>=0:
            visit[x]=2
            if x==res : return -2
            else: return res
    return -1


n=int(input())

arr= [[]*(n+1) for _ in range(n+1)]

for i in range(n):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

visit=[0 for _ in range(n+1)]
dist=[0 for _ in range(n+1)]

dfs(1,-1)

q=deque()

for i in range(1,n+1):
    if visit[i]==2:
        dist[i]=0
        q.append(i)
    else:
        dist[i]=-1

while q:
    x=q.popleft()
    for y in arr[x]:
        if dist[y]==-1:
            q.append(y)
            dist[y]=dist[x]+1
print(visit)
print(dist)
print(*dist[1:])

