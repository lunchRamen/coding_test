"""
2단계로 나눔
1. 문자열의 0을 제거
2. 제거한 문자열의 길이를 토대로 2진수로 표현한걸 다시 s로 표시.

1의 경우 in을 통해 replace를 한개씩하면서 answer[1]를 올림.
그러고 len(s)를 이진수로 나타낸걸 문자열로 변환시킬때마다 answer[0]을 올림.
"""

def solution(s):
    answer = [0,0]
    
    while s!="1":
        while "0" in s:
            s=s.replace("0","",1)
            answer[1]+=1
        lenS=len(s)
        temp=""
        while lenS:
            temp+=str(lenS%2)
            lenS=lenS//2
        temp[::-1]
        s=temp
        answer[0]+=1
    return answer


solution("110010101001")