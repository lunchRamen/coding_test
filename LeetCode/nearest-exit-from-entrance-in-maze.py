import sys
from collections import deque
sys.setrecursionlimit(10**2)

class Solution:
    answer = 100001
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        가장 가까운 출구를 찾는 것.
        출구 = 각 변에 닿아있는지 = x=0 or y=0 or x=len(maze)-1 or y=len(maze[0])-1

        처음에 dfs로 풀었다가, return을 하면 전 상태로 함수가 되돌아가지 않더라.
        그래서 솔루션을 봤더니 다들 bfs로 풀었음. 여기서 또 의문인건,
        100x100짜리인데도 visit으로 방문여부 확인하면서 돌려보면 시간 초과가 남.
        왜 그런진 모르겠음.
        그래서 시간 복잡도 낮은 set으로 풀었다.
        백준, 프로그래머스와 릿코드 사이에 재귀호출 로직이 다른거같다..?
        """
        visit = {tuple(entrance)}
        dx = [-1,1,0,0]
        dy = [0,0,1,-1]

        q = deque()
        q.append([entrance[0],entrance[1],0])

        while q:
            x, y,cnt = q.popleft()
            if (x == 0 or x == len(maze)-1 or y == 0 or y == len(maze[0])-1) and ([x,y] != entrance):
                return cnt

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0<=nx<len(maze) and 0<=ny<len(maze[0]):
                    if maze[nx][ny]==".":
                        if (nx,ny) not in visit:
                            visit.add((nx,ny))
                            q.append([nx,ny,cnt+1])

        return -1
