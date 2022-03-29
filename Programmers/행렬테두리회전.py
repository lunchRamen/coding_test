"""
생각 자체는 정확히 했음. 테두리만 돌려주면 되니 오른쪽 아래 왼쪽 위로 범위마다 탐방하면서
지금 원소를 다음 원소에 덧씌우고 다음원소를 저장해뒀다가 다시 써먹으면 된다.
그리고 원소를 덧씌우는 과정에서 이 문제에서 요구하는건 swap이 아닌, 덧씌우기라
변수가 하나가 아닌 두개가 필요함.
과정: 다음 원소를 임시 저장. 다음 원소 자리에 저장해둔 현재원소를 덧씌움.
      저장해둔 원소(move)에 임시저장 해뒀던 다음원소를 넣어주는걸 반복.

주의해야할 점.
행렬은 2차원 x,y 좌표평면과 헷갈리면 안됨.
우리가 생각하기에 좌우 움직임은 x축 이동, 상하 움직임은 y축 이동이라고 생각하지만
행렬에 있어선 좌우 움직임은 열이동 상하 움직임은 행이동이다. 이것만 유의하고 풀었다면
훨씬 쉽게 풀었을 것.

그래서 오른쪽 이동은 열이동 아래쪽 이동은 행이동 왼쪽 이동은 열이동 위쪽이동은 행이동으로
내가 생각했던 x축,y축,x축,y축 이동과 정반대여서 시계 반대방향의 결과가 나왔음.

좌우=행이동
상하=열이동 주의하자.
"""

def solution(rows, columns, queries):
    answer = []
    arr=[[0 for j in range(columns)] for i in range(rows)]
    
    start=1
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j]=start
            start+=1
    
    for query in queries:
        x1=query[0]-1
        y1=query[1]-1
        x2=query[2]-1
        y2=query[3]-1   #배열 index체계에 맞추기위해서 -1씩해줌.
        
        temp=[] #각 query를 통한 이동한 원소들 중 최소를 추리려고 만든 배열
        # moveRight=arr[x1][y1]
        # moveDown=arr[x2][y1]
        # moveLeft=arr[x2][y2]
        # moveUp=arr[x1][y2]
        moveRight=arr[x1][y1]
        moveDown=arr[x1][y2]
        moveLeft=arr[x2][y2]
        moveUp=arr[x2][y1]
        
        #아래 for문은 "반시계"방향으로 한칸씩 회전하는 것. 나는 시계방향을 의도했는데..왜?
        # for i in range(x1,x2):
        #     store=arr[i+1][y1]
        #     arr[i+1][y1]=moveRight
        #     moveRight=store
        #     temp.append(arr[i+1][y1])
        # for i in range(y1,y2):
        #     store=arr[x2][i+1]
        #     arr[x2][i+1]=moveDown
        #     moveDown=store
        #     temp.append(arr[x2][i+1])
        # for i in range(x2,x1,-1):
        #     store=arr[i-1][y2]
        #     arr[i-1][y2]=moveLeft
        #     moveLeft=store
        #     temp.append(arr[i-1][y2])
        # for i in range(y2,y1,-1):
        #     store=arr[x1][i-1]
        #     arr[x1][i-1]=moveUp
        #     moveUp=store
        #     temp.append(arr[x1][i-1])
        
        # print(arr)
        # answer.append(min(temp))
        for i in range(y1,y2):
            store=arr[x1][i+1]
            arr[x1][i+1]=moveRight
            moveRight=store
            temp.append(arr[x1][i+1])
        for i in range(x1,x2):
            store=arr[i+1][y2]
            arr[i+1][y2]=moveDown
            moveDown=store
            temp.append(arr[i+1][y2])
        for i in range(y2,y1,-1):
            store=arr[x2][i-1]
            arr[x2][i-1]=moveLeft
            moveLeft=store
            temp.append(arr[x2][i-1])
        for i in range(x2,x1,-1):
            store=arr[i-1][y1]
            arr[i-1][y1]=moveUp
            moveUp=store
            temp.append(arr[i-1][y1])
            
    return answer
