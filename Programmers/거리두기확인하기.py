"""
이 문제는 어차피 검사해야할 원소가 총 125개밖에 안되기때문에,
어떻게 풀지만 결정하면 된다.

처음에 생각했던 해결 방법은,

한명의 사람이 있었을때,
그 사람과 거리두기를 안지킬 경우의 수를 모두 검사해주는 함수
(checkPerson)을 하나 만든 다음, 전수 조사를 해주는 것.
예제는 통과했는데, 전체 TC를 통과하지 못했다.

개인적으로 2차원 배열이라 dfs,bfs로 푸는것도 좋겠지만
그것보다 직관적으로 풀 수 있는 방법이 위의 방법이라 생각했고,
다른 문제풀이 방법을 보다가
대각선을 따지는 것 또한 맨해튼거리(가로1+세로1)이기때문에

모든 노드에 대해
1.자기 원소가 p일때, 상하좌우에 p가 없거나
2.자기 원소가 o일때, 상하좌우에 p가 "1개"만 있거나
면, 거리두기를 지킨다.
-> 1번은 거리가 1인경우에 대한 처리
   2번은 거리가 2인 경우에 대한 처리이다.

1번의 경우 해당 노드가 P인데 상하좌우에 P가 또 있다?
거리가 1이므로 거리두기를 안지킴.

2번의 경우 빈테이블인데 상 하 좌 우 에 대해 P가 2개 이상이라면
맨해튼 거리가 2인
직선 혹은 대각선이 된다. 고로 둘 다 거리두기를 안지키기게 된다.
"""
def checkPerson(arr,x,y):
    if x+2<5:
        if arr[x+2][y]=="P":
            if arr[x+1][y]=="O":
                return False
    if x-2>=0:
        if arr[x-2][y]=="P":
            if arr[x-1][y]=="O":
                return False
    if y+2<5:
        if arr[x][y+2]=="P":
            if arr[x][y+1]=="O":
                return False
    if y-2>=0:
        if arr[x][y-2]=="P":
            if arr[x][y-1]=="O":
                return False
    if x+1<5 and y+1<5:
        if arr[x+1][y+1]=="P":
            if arr[x+1][y]=="O" or arr[x][y+1]=="O":
                return False
    if x-1>=0 and y+1<5:
        if arr[x-1][y+1]=="P":
            if arr[x-1][y]=="O" or arr[x][y+1]=="O":
                return False
    if x+1<5 and y-1>=0:
        if arr[x+1][y-1]=="P":
            if arr[x+1][y]=="O" or arr[x][y-1]=="O":
                return False
    if x-1>=0 and y-1>=0:
        if arr[x-1][y-1]=="P":
            if arr[x-1][y]=="O" or arr[x][y-1]=="O":
                return False
    

def solution(places):
    answer = []
    
    for place in places:
        arr=[]
        for row in place:
            temp=[]
            for char in row:
                temp.append(char)
            arr.append(temp)
        
        flag=True
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                cnt=0
                for k in range(4):
                    if i+dx[k]<0 or i+dx[k]>4 or j+dy[k]<0 or j+dy[k]>4:
                        continue
                    else:
                        if arr[i][j]=="P":
                            if arr[i+dx[k]][j+dy[k]]!="P":
                                continue
                            else:
                                flag=False
                        elif arr[i][j]=="O":
                            if arr[i+dx[k]][j+dy[k]]!="P":
                                continue
                            else:
                                cnt+=1
                    if cnt>=2:
                        flag=False
        if flag:
            answer.append(1)
        else:
            answer.append(0)
                        
    return answer