from itertools import permutations
"""
eval이란 함수를 이번에 처음 앎.
문자열로 주어진 어떤 수식연산이든
return 해줄 수 있다.
그렇다는건?
우리가 정한 연산자 순위대로
연산자를 탐색한 다음,
연산자를 찾았으면 해당 연산자에 대해 연산하고 다시 연산하면 된다.
"""
#Divide and Conquer version
# def calc(operator,n,expression):
    
#     if n==2:
#         return str(eval(expression))
#     if operator[n]=="*":
#         res=eval("*".join([calc(operator,n+1,e) for e in expression.split("*")]))
#     elif operator[n]=="+":
#         res=eval("+".join([calc(operator,n+1,e) for e in expression.split("+")]))
#     elif operator[n]=="-":
#         res=eval("-".join([calc(operator,n+1,e) for e in expression.split("-")]))
#     return str(res)
        
# def solution(expression):
#     answer = 0
#     arr=permutations(["*","+","-"],3)
    
#     for operator in arr:
#         res=int(calc(operator,0,expression))
#         answer=max(answer,abs(res))
#     return answer


#stack version
"""
이게 더 직관적.
expression이랑 우선순위가 정해진 연산자 배열을 보내면, 계산을 하는데
일단 expression을 숫자,연산자 순으로 쪼개준 array를 만든다.

for문을 주어진 우선순위 연산자 문자열 3개에 대해 돌린다.
그다음 스택을 만들고, array를 다 pop시킬때까지 while문을 돌린다(len(array)!=0)
array.pop(0)을 한 다음, 이게 연산자면 stack에 있는거랑 array.pop(0)을 하나 더한거랑 연산을 해준다.
아니라면 stack에 넣고.
이렇게 되면 숫자 연산자 숫자 ... 연산자 숫자기때문에 while문의 연산은 무리없이 진행된다.

또한, 우선순위 연산자가 우리가 정해진대로 움직이기때문에

3가지의 연산자를 돌면서
array를 항상 다 돈다.
그래서 stack에 해당 연산자가 아니면 그냥 넣고
해당 연산자라면, array.pop(0)과 stack.pop()을 연산한 결과값을 넣는다.
-> 연산자 하나씩 돌때마다 array가 stack에 맞게끔 갱신되어 저장된다.
->이래도 문자열 길이 자체가 매우 짧으니 가능한 일.

이렇게 계속 진행하다보면, 연산 결과값 하나만 남게 된다.
그걸 return해주면 되고, 이 값들을 배열에 모아뒀다가 max값을 return하면 된다.

여기서 체크해야할 점은, stack이 끝에서 분기 종료가 일어나지 않는이상
stack에 남아있는 원소들을 비워내는 용도로
array.append(tmp)를 해줘야한다.
"""
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))
    
def calculate(exp,op):
    array=[]
    tmp=""
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack
            
    return abs(int(array[0]))

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)