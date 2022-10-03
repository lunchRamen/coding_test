import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

"""
다익스트라

그게 2가지 부분
1.시작 노드부터, 연결된 노드의 가중치를 업데이트 함.
2.이후에 방문하지 않은 가장 작은 가중치를 정점의 갯수만큼 반복한다.

그래서 순서를 보면
k와 연결된 노드들의 가중치를 업데이트
이후에 v-1번(노드 k는 빼야하나)을 돌면서
"각 반복문마다 k~해당 노드까지 최소 가중치 노드"를 찾음(get_smallest_node) = now

이렇게 now노드를 찾으면, now노드에서 연결된 노드와, 그 가중치들의 배열을 다시 돌림.
그래서 (k~now까지 가중치)+ now-next가중치 < (k~next까지 가중치)라면,
now를 통해서 k~next를 가는게 더 최적해니까 업데이트를 시킴
-> 이래서 dp를 INF로 초기화시킴. 연결되어보지 않은곳이라면,
    해당 노드와 연결된 모든 노드들을 통해 거기까지 가는 최소가중치를 구해야하니까.
그래서 정답 return.


가장 작은 노드를 구해서, 하면 O(N)이라서, 아마 틀리는듯
heapq를 이용해서, O(logN)으로 낮춰서 하니 통과가 됨.

heapq의 경우 list를 priority Q로 만들어서, 
->(디폴트가 minHeap. pop시키면 idx가 우선순위를 가져서 가장 낮은순서대로 pop 됨.)

heapq에다가는 시작 정점을 넣고,
인접 노드부터, 각 start~인접노드까지 가는 가중치 합의 최솟값을 갱신시켜 나감.
q에는 개선된 가중치의 최적값만 들어갈테니, q가 비었다는건 모든 노드에 대해 가중치 최적화 작업이 끝났다는 것.
"""

v,e = map(int,input().split())
k = int(input())
dp = [INF]*(v+1)
graph = [[] for _ in range(v+1)]
visit = [False]*(v+1)

for _ in range(e):
    a,b,c, = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1,v+1):
        if dp[i]<min_val and not visit[i]:
            min_val=dp[i]
            idx = i
    return idx

# def dijkstra(start):
#     dp[start] = 0
#     visit[start]=True

#     for i in graph[start]:  #인접 노드만 먼저
#         dp[i[0]]=i[1]

#     for _ in range(v-1):    #방문하지 않은 인접노드 중 가장 작은 노드를 가져옴
#         now = get_smallest_node()
#         visit[now]=True

#         #dp = [연결된 노드 , 가중치]
#         for j in graph[now]:#해당 노드와 연결된 노드를 다시 돌림.
#             if dp[now]+j[1] < dp[j[0]]:# now까지 오는 가중치 + j까지 가는 가중치 < 이전에 기록된 j까지 가는 가중치
#                 dp[j[0]]=dp[now]+j[1]#업데이트.

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    dp[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # pop시킨 가중치가, dp[now]보다 크다 = 이미 최적화된 거리. ->이미 방문한 노드. = 건너뜀.
        if dp[now] < dist:
            continue
        
        #dp[now]가 더 크다면 -> 최적화되지 않음(k~now까지 가는 거리
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) #해당 최적해를 다시 heapq에다가 넣음.
dijkstra(k)
for i in dp[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
