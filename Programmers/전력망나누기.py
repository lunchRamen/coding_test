from collections import deque

"""
dfs 혹은 bfs로 해도 되는데,
visit 배열을 매번 생성해주면 bfs로 해도 되는데,
input의 최대크기가 100으로 작으니 완탐해도 괜찮.

wires의 각 배열마다
한 점을 기준으로 다른점은 방문표시를 해놓고 bfs를 돌린다.
->이러면, 해당 점을 무조건 거쳐가야하는데 이걸 제외하고 돌려서
송전탑이 분리된것같은 효과를 낼 수 있다.

bfs는 해당 점을 기준으로 graph에 연결된 점들이 다 방문 될때까지
while q:를 돌면서 방문횟수를 1씩 증가시키고, 방문횟수를 return 한다.

해당 방문횟수 - (n-방문횟수 = 다른 송전탑의 연결갯수)가 answer보다 작으면 갱신.

그걸 return 해주면 된다.

그래프 문제를 더 연습해야한다.
-> 백준 dfs bfs graph를 더 풀자..
"""

def bfs(start,visit,arr):
    q=deque([start])
    result=1
    visit[start]=True
    
    while q:
        cur=q.popleft()
        
        for i in arr[cur]:
            if visit[i]==False:
                result+=1
                visit[i]=True
                q.append(i)
    return result
        

def solution(n, wires):
    answer = n
    arr=[[] for _ in range(n+1)]
    for u,v in wires:
        arr[u].append(v)
        arr[v].append(u)
    
    for u,v in wires:
        visit=[False for _ in range(n+1)]
        visit[v]=True
        result=bfs(u,visit,arr)
        
        if abs(result-(n-result))<answer:
            answer=abs(result-(n-result))
        
    
    return answer