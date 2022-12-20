from collections import deque
"""
기초적인 dfs/bfs 문제.
개인적으로 릿코드의 재귀동작방식을 잘 모르겠어서, bfs로 풂.
0번째방에 열쇠들을 넣고, 다른 방들을 방문해가며 방문여부를 체크한다.
모든 방을 방문 했다면 True 하나라도 False라면 False.
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visit = [False for _ in range(len(rooms))]

        q = deque()

        visit[0]=True
        for i in rooms[0]:
            q.append(i)

        while q:
            room = q.popleft()
            visit[room] = True

            for i in rooms[room]:
                if not visit[i]:
                    q.append(i)
        for i in range(len(visit)):
            if not visit[i]:
                return False
        return True
