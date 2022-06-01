import sys

input=sys.stdin.readline

"""
문제를 너무 어렵게 생각함.
중앙값 -> 길이가 홀수일땐 idx//2 짝수일땐 (idx//2 + idx//2-1)/2를 하면 되는데,
우리는 홀수번째마다 중앙값을 얻고싶은거라 그냥 idx//2만 계속 해주면 된다.

다만 배열은 원배열, 하나씩 담으면서 홀수번째마다 중앙값을 구할 배열, 중앙값을 담을 배열
총 3개가 필요하고, 출력할때 *를 붙이면 배열없이 출력이 가능함을 유의.
"""

t=int(input())

for _ in range(t):
    n=int(input())
    repeatN=(n//10)+1
    arr=[]
    oddArr=[]
    answer=[]

    for _ in range(repeatN):
        temp=map(int,input().split())
        arr+=temp
    
    for i in range(len(arr)):
        oddArr.append(arr[i])
        if i%2==0:  #홀수번째인 경우
            oddArr.sort()   #정렬
            answer.append(oddArr[len(oddArr)//2])

    print((n//2)+1)
    
    for i in range(0,len(answer),10):
        print(*answer[i:i+10])


    
    
    
    

    
