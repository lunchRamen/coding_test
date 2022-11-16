from collections import defaultdict

class Solution:
    
    """
    같은 행/열에 대해 인접한 리스트로 판별하여, 처리하는 로직. 전형적인 bfs/dfs로직이다.
    다만 궁금한 점은, class안에 다른 메서드로 만들면 통과가 안되고 메서드 내부에 로컬멤버를 할당해줘야 문제가 풀렸다.
    왜냐하면, 릿코드의 TC 검증 방식은 문제풀이 메서드를 반복 호출하는것이지, 객체를 반복 생성하는것이 아니기때문이다.

    문제 로직 자체는, 모든 stones를 돌면서, 방문되지 않은 돌에 한해서 세어주고,
    각 행/열에 연결된 모든 돌들을 방문시킨다.

    이렇게 방문 안한 돌들만 세어준걸 전체 돌 갯수에서 빼주면, 지운 돌의 갯수가 나온다.
    """

    def removeStones(self, stones: List[List[int]]) -> int:
        graphX = defaultdict(list)
        graphY = defaultdict(list)
        visited = set()
        new_stone = 0       

        for x,y in stones:
            graphX[x].append(y)
            graphY[y].append(x)

        def dfs(x,y):
            if (x,y) not in visited:
                visited.add((x,y))

                for nextY in graphX[x]:
                    dfs(x,nextY)
                for nextX in graphY[y]:
                    dfs(nextX,y)

        for x,y in stones:
            if (x,y) not in visited:
                dfs(x,y)
                new_stone+=1

        return len(stones)-new_stone
    
