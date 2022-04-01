"""
올바른 문자열 함수
문자열을 균형맞게 나누는 함수를 만들어야한다고 생각하는거까진 좋았는데,
재귀함수 구현부분에서 막힘.
굳이 rec로 재귀함수를 따로 빼는거보단 solution함수 자체를 재귀로 구현하면 된다.

그리고, 설명에서 나온 단계대로만 구현해주면 정답이 나오는데, 그걸 내 기준으로 재정의해서
구현하려고 하니까 오히려 더 어렵게 느껴졌던것같다.

그리고 splitString의 경우
다른경우 따질 필요없이, 그냥 주어진 문자열을 돌면서
(이면 left+=1 )이면 right+=1하면서,
left==right이 되면
해당 i번째 index기준으로 u,v를 잘라주면 된다.
index니까 i+1로 나눠주면 됨.

"""
def checkCorrect(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            stack.pop()
    return True

def splitString(s):
    left,right=0,0
    for i in range(len(s)):
        if s[i]=="(":
            left+=1
        else:
            right+=1
        if left==right:
            return s[:i+1],s[i+1:]
        
def solution(p):
    #1번
    if p=="":
        return ""
    #2번
    u,v=splitString(p)
    #3번
    if checkCorrect(u):
        #3-1
        return u+solution(v)
    #4번
    else:
        temp=""
        #4-1
        temp+="("
        #4-2
        temp+=solution(v)
        #4-3
        temp+=")"
        #4-4
        for i in u[1:len(u)-1]:
            if i=="(":
                temp+=")"
            else:
                temp+="("
    #4-5
    return temp