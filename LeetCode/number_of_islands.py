class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        전형적인 dfs문제.
        각 노드별로 1인것들을 끝까지 visit하고, return하는.
        헷갈렸던건 dfs에서 다음 노드로 넘어갈때는 visit[nx][ny]==False를 안해도 된다는점.
        왜냐? 어차피 다음노드에서 visit조건문으로 return을 하고, 만약 여기서 and로 걸게되면,
        해당 visit[nx][ny]==False로 인해 dfs를 방문했다고 표시 못한 노드가 중복되게 체크가 된다.
        """
        visit = [[False]*len(grid[0]) for _ in range(len(grid))]
        answer=0
        
        def dfs(grid,visit,x,y):
            dx=[1,-1,0,0]
            dy=[0,0,1,-1]

            if visit[x][y]==True:
                return
            else:
                for i in range(4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]):
                        if grid[nx][ny]=="1":
                            visit[x][y]=True
                            dfs(grid,visit,nx,ny)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1' and visit[i][j]==False:
                    dfs(grid,visit,i,j)
                    answer+=1
            
        return answer
