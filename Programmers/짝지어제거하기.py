
"""
while - for문으로 풀면, 문자열 길이가 100만이라 당연히 오류가 남.
그래서 투포인터로 풀지, bfs로 풀지 생각을 해봤는데 마땅한 풀이방법이 생각 안나 검색함.
-> stack으로 풀었다.

stack에 s를 돌면서 원소들을 하나씩 넣어놓고 맞다면 pop, 다르다면 append하면서
한번만 돌면 다 검사가 되게끔.
-> 내가 우려했던 baabaa의 경우 aa가 pop되고 나서야 bb가 pop될 수 있는 조건에 대한
예외처리를 걱정했었는데, 그러지 않아도 되는게 어차피 for문을 한번 돌거고, b의 index는
짝지어서 pop되는 index뒤에 있기때문에 stack에만 넣어놓는다면 짝지어진 순서대로 pop된다.
"""

def solution(s):
    answer = 0
    arr=[]
    
    for i in range(len(s)):
        if not arr:
            arr.append(s[i])
        else:
            if arr[-1]==s[i]:
                arr.pop(-1)
            else:
                arr.append(s[i])
    if len(arr)==0:
        answer=1
    else:
        answer=0
    
    #아래 방식은 s가 100만이기때문에 당연히 엣지케이스에서
    #시간초과가 남.
    # while True:
    #     if len(s)==0:
    #         answer=1
    #         break
        
    #     flag=True
    #     for i in range(len(s)-1):
    #         if s[i]==s[i+1]:
    #             flag=False
    #     if flag:
    #         answer=0
    #         break
        
    #     for i in range(len(s)-1):
    #         if s[i]==s[i+1]:
    #             temp=s[i]+s[i+1]
    #             s=s.replace(temp,"")
    #             break
    return answer

print(solution("baabaa"))