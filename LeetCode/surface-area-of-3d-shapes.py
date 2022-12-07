class Solution:
    """
    2차원 배열 안에 원소가 각 정육면체의 높이이고, 각 정육면체끼리 인접해있다고 했을때, 총 면적의 넓이를 구하는 문제.
    일단 모든 정육면체는 다른 정육면체와 인접해있음.
    기본 면적 = 위,아래,옆 4면.
    여기서, grid[i][j]>=2가 된다면, 인접하는 면이 2개씩 생성된다. -> 2이상의 크기일때는 2씩 빼줘야함.
    grid[i][j]*6 - 2*(grid[i][j]-1) = 4*grid[i][j]+2가 나오게 됨.
    그 다음, 왼쪽 위 -> 오른쪽 아래로 내려가면서, 인접한 2면만 작은걸 빼주면, 모든걸 조사해서 면접의 넓이가 나온다.
    """
    def surfaceArea(self, grid):
        n, res = len(grid), 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    print(i,j)
                    res += grid[i][j] * 4 + 2
                if i:
                    res -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: 
                    res -= min(grid[i][j], grid[i][j - 1]) * 2
        return res
