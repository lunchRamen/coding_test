class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        90도 rotate의 규칙을 알면 됨.
        2차원 배열을 90도 회전 시키면,
        회전 시키기 전 열이 회전시키고는 행이 된다.
        여기서 차이점은, 열의 역순으로 행의 값이 된다는 것.
        그래서 matrix의 열값들을 뽑아 행으로 만들고 (각 행의 열값들을 뽑아 temp로 만듬)
        그 후 temp의 각 행 배열을 역순으로 만든다.
        이후 matrix로 합체.
        """
        temp=[]
        
        for j in range(len(matrix)):
            temp.append([i[j] for i in matrix])
        
        for i in range(len(temp)):
            temp[i]=temp[i][::-1]
        
        for i in range(len(matrix)):
            matrix[i]=temp[i]
