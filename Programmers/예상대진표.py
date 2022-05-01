import math
"""
a,b를 통해서 구하고자 하는 것
= a와 b 사이의 차가 1인 경우.

a+1 == b 에 대해서 사전에 고려해줘야할 것 3가지
1. a<b인 상태여야한다.
2. a는 홀수, b는 짝수여야한다.
3. 이겼을때에 대한 경우를 math.ceil(n/2)로 해줘야한다.(무조건 올림)

이렇게 하면 풀림.
"""
def solution(n,a,b):
    answer = 1
    
    if a>b:
        temp=a
        a=b
        b=temp
        
    while True:
        if a+1 == b:
            if a%2==1 and b%2==0:
                break
        a=math.ceil(a/2)
        b=math.ceil(b/2)
        answer+=1
    return answer