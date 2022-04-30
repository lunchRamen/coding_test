"""
재귀로 구현하는게, 가장 깔끔.
s의 범위를 len(arr)부터 시작해서, 0이 될때까지 자동으로 재귀호출이 된다.
s의 범위를 탐색하면서, 인자로 받은 x,y를 start(시작)원소로 두고,
입력받은 n으로 2중 for문을 돌린다.

만약, arr[i][j]!=start라면 해당 범위 내 다른 원소가 존재한다는 뜻이고,
이건 압축이 불가능하기때문에 입력받았던 범위 n을 4등분해서 재귀호출한다.
그리고 if문 안에 return문을 넣는다.
왜냐하면 우리가 지금하는 재귀호출은 따로 조건에 따른 탈출문이 있는게 아니라,
n이 0이될때까지 끝까지 돌면서 압축하는걸 찾는것이기 때문.
고로, if문으로 재귀를 한정시키면 재귀호출된 comp문이 n이 0이될때까지 재귀호출하다가
return문을 만나든, answer[start]+=1을 하든 호출 반환되어 돌아오기때문.

그래서 comp(0,0,n)만 넣으면, 탐색이 완료된다.
"""

def solution(arr):
    answer = [0,0]
    
    n=len(arr)
    
    def comp(x,y,n):
        start=arr[x][y]
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=start:
                    nn=n//2
                    comp(x,y,nn)
                    comp(x+nn,y,nn)
                    comp(x,y+nn,nn)
                    comp(x+nn,y+nn,nn)
                    return
        answer[start]+=1
        
        
    comp(0,0,n)
    
    return answer