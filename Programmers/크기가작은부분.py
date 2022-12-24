"""
0번~len(t)-len(p)+1까지 순회하면서
temp 문자열을 [i:i+len(p)]까지 잘라내며 int형 값을 비교한다.
"""
def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        temp = t[i:i+len(p)]
        if int(temp)<=int(p):
            answer+=1
    return answer
