from collections import deque
"""
전형적인 괄호문제.

괄호문제의 경우, stack으로 ({[의 경우 stack에 넣고, )}]의 경우 stack.top과 순서쌍이라면 pop 시킨다.
그렇게 모든 괄호에 대해 진행하고 난 후 , stack이 비어있다면 괄호가 올바른거고, 아니라면 올바르지 않은 것.

여기서 한번 꼬은것은, 주어진 문자열에서 괄호를 하나씩 회전 시켰을때 올바른경우/아닌경우로 나뉘어지는데 이에 대한 처리를 해줘야한다.
이것은 deque의 rotate함수를 통해서 해결.
"""
def solution(s):
    answer = 0
    
    temp=deque(s)
    temp.rotate(-1)
    
    if len(temp)%2 != 0:
        return 0
    
    while True:
        stack=[temp[0]]
        if "".join(temp)==s:
            for i in range(1,len(temp)):
                if not stack:
                    stack.append(temp[i])
                    continue
                if temp[i]=="[" or temp[i]=="{" or temp[i]=="(":
                    stack.append(temp[i])
                else:
                    if temp[i]=="]" and stack[-1]=="[":
                        stack.pop(-1)
                    elif temp[i]=="}" and stack[-1]=="{":
                        stack.pop(-1)
                    elif temp[i]==")" and stack[-1]=="(":
                        stack.pop(-1)
            if not stack:
                answer+=1
            break
        
        for i in range(1,len(temp)):
            if not stack:
                stack.append(temp[i])
                continue
            if temp[i]=="[" or temp[i]=="{" or temp[i]=="(":
                stack.append(temp[i])
            else:
                if temp[i]=="]" and stack[-1]=="[":
                    stack.pop(-1)
                elif temp[i]=="}" and stack[-1]=="{":
                    stack.pop(-1)
                elif temp[i]==")" and stack[-1]=="(":
                    stack.pop(-1)
        
        if not stack:
            answer+=1
        temp.rotate(-1)

        
    
    
    return answer