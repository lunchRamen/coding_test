class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        matrix[n-1][0]부터 -> matrix[n-1][m-1]까지 -> matrix[0][m-1]까지 돌면서
        matrix내에 왼쪽상단이 같으면 넘어가고, 아니면 false를 return
        대각선 탐색하는 규칙만 알면 풀기는 쉽다.
        """
        n=len(matrix)
        m=len(matrix[0])

        for i in range(m):
            start = matrix[n-1][i]
            x = n-1
            y = i

            nx=x-1
            ny=y-1
            
            while True:
                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny]==start:
                        nx-=1
                        ny-=1
                    else:
                        return False
                else:
                    break
        for i in range(n-1,-1,-1):
            start = matrix[i][m-1]
            x = i
            y = m-1

            nx=x-1
            ny=y-1

            while True:
                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny]==start:
                        nx-=1
                        ny-=1
                    else:
                        return False
                else:
                    break
        return True
