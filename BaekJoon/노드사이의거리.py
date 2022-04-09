import sys
from collections import deque

input=sys.stdin.readline

"""
인접행렬로 하면 시간초과가 남.
왜 시간초과가 나는지 모르겠음.
-> 인접리스트로 다시 짠다.

dfs론 왜 구현이 안되는지 모르겠음. 동일한 로직으로 bfs구현하면 됨.

"""

answer=0

def bfs(start,end,visit):
    q=deque()
    q.append((start,0))
    visit[start]=1
    while q:
        v,d=q.popleft()
        print(v,d)

        if v==end:
            return d

        for dest,dist in arr[v]:
            if not visit[dest]:
                visit[dest]=1
                q.append((dest,dist+d))
    # global answer
    # if start==end:
    #     answer=distance
    #     return
    # # for i in range(1,n+1):
    # #     if arr[start][i]!=0:
    # #         if visit[i]==1:
    # #             continue
    # #         visit[i]=1
    # #         dfs(i,end,distance+arr[start][i],visit)

    # #인접행렬과 달리 배열의 값이 0인지 따질 필요가 없음. 해당 index에 있는것들은
    # #다 연결되고 거리값이 있는 값들이라서.
    # for dest,dist in arr[start]:
    #     if not visit[dest]:
    #         visit[dest]=1
    #         dfs(dest,end,distance+dist,visit)



n,m=map(int,input().split())

arr=[[] for _ in range(n+1)]


for _ in range(n-1):
    x,y,distance=map(int,input().split())
    arr[x].append([y,distance])
    arr[y].append([x,distance])
print(arr)
#[[[2, 2], [4, 3]], [[1, 2]], [[4, 2]], [[3, 2], [1, 3]]]
#        1              2         3            4
for _ in range(m):
    visit=[0 for _ in range(n+1)]
    answer=0
    x,y=map(int,input().split())
    print(bfs(x,y,visit))
