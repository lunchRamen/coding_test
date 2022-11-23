from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        스도쿠가 맞는지 검사하는 로직.
        1.각 행은 1~9까지의 숫자를 1개씩만 가지고 있어야한다.
        2. 각 열 또한 동일.
        3. 3x3박스는 1~9까지 숫자를 가지고 있어야한다.

        각 비어있는 칸에 대해, 1~9까지의 숫자 중 1,2,3조건을 통해 숫자 1개가 들어가는지 검사. 들어갈 수 있다면, 통과
        안된다면 실패.

        나는 스도쿠를 아예 풀어야되는줄 알고, 각 숫자들을 입력했었는데, Note를 잘 읽어봤어야 됐음.
        그냥 주어진 스도쿠 숫자들로만 참/거짓을 판별하는 문제
        각 행/열/subtree를 기점으로 검색해서 2개이상의 숫자가 나오면, False 아니면 True.
        """

        def checkValid(board,x,y):
            row_dic = defaultdict(int)
            column_dic = defaultdict(int)
            subsquare_dic = defaultdict(int)

            for i in range(9):
                if board[x][i] != ".":
                    row_dic[int(board[x][i])]+=1
                if board[i][y] != ".":
                    column_dic[int(board[i][y])]+=1
                
            
            row_3 = x//3
            column_3 = y//3
            for i in range(row_3*3,row_3*3+3):
                for j in range(column_3*3,column_3*3+3):
                    try:
                        subsquare_dic[int(board[i][j])]+=1
                    except:
                        continue
            for i in range(10):
                if row_dic[i]>=2 or column_dic[i]>=2 or subsquare_dic[i]>=2:
                    return False
            return True
                    

        for i in range(len(board)):
            for j in range(len(board[i])):
                if not checkValid(board,i,j):
                    return False
        return True
