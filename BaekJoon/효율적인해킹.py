import sys
from collections import deque,defaultdict

"""
문제 풀이.
bfs를 한번만 돌리는게 아니라, 모든 노드들에 대해서 다 돌림.
-> 매번 방문배열을 초기화 해줄 필요가 있음.
-> 또한, 우리가 구하고자하는 연결된 노드의 수를 q에 같이 넣을 필요가 없음
-> 나머지는 일반 bfs구현과 동일

1. 첫번째 노드를 q에 넣고, 방문 표시.
2. q.popleft()해서 배열과 연결된 것들 중 방문 안한것들에 대해 방문표시한 후, cnt+=1하고 q에 넣음.
3.cnt를 return해줌.

여기서 왜그런진 모르겠는데, 시간초과와 출력초과가 뜸.
예를 들어, maxCnt를 for문을 돌면서 정하는것과
max(answer[1])로 하는게 동일한 로직으로 동작하는데, 왜 전자는 통과하고 후자는 안되는지 모르겠다.
그리고 시간초과의 경우, 인접행렬 대신 인접리스트를 써도 안돼서 딕셔너리로 풀었다.
"""

def bfs(start):
    visit=[0 for _ in range(n+1)]
    q=deque()
    visit[start]=1
    q.append((start))
    
    cnt=1

    while q:
        idx= q.popleft()
        
        for i in arr[idx]:
            if not visit[i]:
                visit[i]=1
                cnt+=1
                q.append((i))
    return cnt

input=sys.stdin.readline

n,m=map(int,input().split())
arr=defaultdict(list)

for _ in range(m):
    x,y=map(int,input().split())
    arr[y].append(x)



answer=[]
maxCnt=0
for i in range(1,n+1):
    t=bfs(i)
    # if maxCnt<t:
    #     t=maxCnt
    answer.append([i,t])

maxCnt=max(answer[1])

for i,cnt in answer:
    if cnt==maxCnt:
        print(i,end=' ')