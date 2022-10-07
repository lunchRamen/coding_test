import sys
import bisect
from collections import deque,defaultdict

input = sys.stdin.readline
INF = sys.maxsize

sys.setrecursionlimit(10**5)
"""
벽을 부순 여부를 따지는 전역변수를 두고, 그거에 따라 달리 표현하려고 했는데,
백트래킹으로 해도 시간초과뜸
-> visit배열 자체를 다시 [2]로 해서 [0으로 갔을때 최단거리, 1로 갔을때 최단거리]를 저장하는 것.(동시에 구한다.)

-> 엄청 헤맸던 문제
문제때문에 아니라, 파이썬 리스트 생성시 참조값 문제

ex) arr= [[0]*m for _ in range(n)]
    arr= [[0 for _ in range(m)] for _ in range(n)]에서
    위에는 i번째 [0]들이 모두 같은 참조값을 가져 arr[i][0]~arr[i][m-1]중 하나만 바꿔도 i번째줄 모두가 바뀐다. ([0]의 참조값을 복사 = shallow copy)
    아래는 0을 m번 반복해서 할당하는거기때문에, 참조값이 다 다르다. -> deep copy는 아닌거같고, 그냥 객체가 새로 할당되는 방식. 위에는 참조값을 복사하는 방식.
"""


n,m = map(int,input().split())


arr = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
# visited = [[[0]*2]*m for _ in range(n)]
# print(visited)
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
# print(visited)
def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()
        
        # 목표지점 도달 시 해당 위치까지의 거리 리턴
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 현재 위치로 이동할 수 있고, 아직 방문하지 않았다면
                if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])
                
                # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif arr[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w + 1] = visited[x][y][w] + 1
                    q.append([nx, ny, w + 1])
    
    # 목표지점까지 도달하지 못한다면 -1 리턴
    return -1

print(bfs())
