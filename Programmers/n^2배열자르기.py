# 버전 1. n의 input(천만)을 고려하지않고 그냥 2중 for문으로 배열 생성 후 잘라서 시간초과남.
# for문 하나만 통해서 문제 해결이 가능해야함.
#  def solution(n, left, right):
#     answer = []
#     arr=[[0]*n for _ in range(n)]
#     arr[0][0]=1
    
#     temp=2
#     while temp!=len(arr)+1:
#         for i in range(temp):
#             for j in range(temp):
#                 if arr[i][j]==0:
#                     arr[i][j]=temp
#         temp+=1

#     for i in range(len(arr)):
#         answer+=arr[i]
#     print(answer)
#     answer=answer[left:right+1]
#     print(answer)
#     return answer

# 버전 2. 이전보다 점수가 높긴한데, 그래도 여전히 시간초과가 뜸.
#=> left행과 right행이 겹치면 하나의 행, 다르면 2개의 행만 구해서 answer로 만드는게 필요할듯.
# def solution(n, left, right):
#     answer = []
#     arr=[i+1 for i in range(n)]
    
#     for i in range(n):
#         if len(answer)>right:
#             break
#         for j in range(i,-1,-1):
#             arr[j]=arr[i]
#         answer+=arr
    
#     answer=answer[left:right+1]
            
#     return answer

"""
버전 3. 통과
left를 포함하는 시작행
right를 포함하는 종료행을 구해서
시작행~종료행까지만 계산해서 answer를 1차적으로 구성한다.
각 행마다 어떻게 구성되는지는 버전2를 통해 이미 로직을 구해놔서 그대로 적용.

그다음, [left:right+1]를 하면, 틀리게 나온다.
왜냐하면 우리는 전체 행을 구한게 아니라,
시작행~종료행까지의 부분 배열만 구한것이기 때문이다.

이렇게 되면 어떻게 되냐?
원래같았으면 종료행까지 한참 남았어야되는데,
right index를 포함하는 행까지만 구해서 원하는 부분 배열이 안됨.
-> left는 left%n으로 시작행에서 몇번째 인덱스인지를 구하고,
    right는 left로부터 몇번째까지를 구하는지만 설정해주면 되는데
    이것은 left+(right-left)를 해주면 되는데, 여기서 left는 나머지 연산을 한
    left가 아닌, 원래 left를 빼줘야함. 
"""

def solution(n, left, right):
    answer = []
    arr=[i+1 for i in range(n)]
    
    temp=n
    while left>=temp:
        temp+=n
    temp-=n
    start=temp//n
    while right>=temp:
        temp+=n
    temp-=n
    end=temp//n
    
    for i in range(start,end+1):
        for j in range(i,-1,-1):
            arr[j]=arr[i]
        answer+=arr
    temp=left
    left=left%n
    right=left+(right-temp)
    answer=answer[left:right+1]
            
    return answer