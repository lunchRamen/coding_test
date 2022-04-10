import sys
from collections import deque,defaultdict

"""
간선의 갯수가 홀수=내가 이김
간선의 갯수가 짝수=내가 짐.

해당 트리는 방향성이 필요없다.
루트노드(1)만 dfs돌리면 거기에 연결된 모든 간선들의 갯수를 +1씩하며 돌면 된다.

근데 우리가 얘기하는 간선의 갯수는,
리프노드 -> 루트노드의 경우만이다. (중간 노드들은 고려X)
그래서 리프노드가 무엇인지 알고(len(arr[i])==1)
해당 리프노드 -> 루트노드까지 거리가 몇인지
(dfs를 통해 모든 노드들의 루트노드로부터의 거리를 저장해둠.)
distance[i]를 가져와서 answer에 더한다음,

answer가 짝수이면 내가 지고, 홀수이면 내가 이기는걸 출력하면 됨.

다만, input이 50만개이다보니, 처리해줘야할게 2가지 있었음.
하나는 재귀횟수 제한.
두번재는 input을 stdin으로 하는것.
"""

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

n=int(input())

arr=[[] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]
distance=[0 for _ in range(n+1)]

for _ in range(n-1):
    x,y=map(int,input().split())

    arr[x].append(y)
    arr[y].append(x)


def dfs(node):
    visit[node]=1
    for next in arr[node]:
        if not visit[next]:
            distance[next]=distance[node]+1
            dfs(next)

dfs(1)

answer=0
for i in range(2,n+1):
    if len(arr[i])==1:
        answer+=distance[i]

if answer%2==0:
    print("No")
else:
    print("Yes")
