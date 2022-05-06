"""
접근 자체는 맞았는데, "규칙"을 찾았어야 됐다.
왼 아래 오로 가면서 한개씩 빠져가고,

x와 y좌표로 삼각형 원소 좌표를 찾아가는데,

0~n-1까지 (5면 0,1,2,3,4)
그리고 i~n까지 돌아가는데

outer for문의 경우 총 돌아가야하는 달팽이 횟수
inner for문의 경우 한번 돌아갈때까지 왼쪽 아래 -> 아래 오른쪽 -> 오른쪽 위의 끝까지 가게끔하는 for문.

그래서 i의 나머지가 0이면 x를 1 더하고
1이면 y+=1
2면 x-=1 y-=1
그 이유는, i가 0이면 -> 0~n-1 (n개)
                1이면 -> 1~n-1 (n-1개)
이렇게 나아가서 마지막까지 역으로 되는 관계인데
이 경우에 맞게끔 삼각형 변을 매핑시키는게 3의 나머지 관계여서 그렇다.

0이면 처음이니까 왼쪽 아래
1이면 두번째니까 아래 오른쪽
2면 세번째니까 오른쪽 위 이걸 inner for문에서 반복해준다.
"""

def solution(n):
    start=1
    answer=[[0 for j in range(1,i+1)] for i in range(1,n+1)]
    
    x,y=-1,0
    
    for i in range(n):
        for j in range(i,n):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            else:
                x-=1
                y-=1
            answer[x][y]=start
            start+=1

    return sum(answer,[])