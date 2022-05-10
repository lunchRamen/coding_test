"""
지원서를 개발언어/직군/경력/소울푸드/점수로 나눈다.
=> info에 공백문자 기준으로 들어가 있음
query의 경우 해당 케이스에 맞는 지원자를 return해주는 것.

query의 조건과, info의 조건이 다 부합하는 경우의 수를 answer에 append해준다.

-> 정확성만 맞았다.
왜냐하면 info는 갯수가 5만, query는 10만이니까
2중 for문 돌리면 당연히 안됨.

->시간 복잡도를 줄일 수 있는 방법.
언어,직군,경력,소울푸드는 정해져있음. -> 이걸 배열로 만듬
그 다음, query에서 -도 없애서 저장한다.
그 다음, query의 길이가 1이면? -> 숫자밖에 없으니 info[-1]과 비교.
2 이상이라면 -> language, part, time, food 중 어떤거에 들어있는지 검사.
그게 info에도 들어있다면? 이걸로 이어나간다.
"""
# import bisect

# def solution(info, query):
#     answer = []
#     filter_info=[]
#     filter_query=[]
#     for i in info:
#         filter_info.append(i.split())
#     for q in query:
#         t=q.split()
#         while "and" in t:
#             t.remove("and")
#         filter_query.append(t)
    
#     for query in filter_query:
#         flag=True
#         cnt=0
#         for info in filter_info:
#             for i in range(len(query)-1):
#                 if query[i]=="-":
#                     continue
#                 if query[i] in info:
#                     flag=True
#                     continue
#                 else:
#                     flag=False
#                     break
#             if flag:
#                 if int(query[-1])<=int(info[-1]):
#                     cnt+=1
#         answer.append(cnt)
#     print(answer)
                            
#     return answer

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic=defaultdict(list)
    for i in info:
        i=i.split()
        # condition = 점수를 제외한 지원자의 상태
        # score = 지원자의 코테 점수
        condition=i[:-1]
        score=int(i[-1])
        
        #지원자의 상태를 문자열 하나로 만든 다음, 지원자와 매핑될 수 있는
        # "-"를 조합을 통해 넣는다.
        #이렇게 되면, query와 완벽하게 매칭되는 문자열을 O(1)로 찾을 수 있다.
        #공간복잡도는 고려사항이 아니고, 시간복잡도를 줄여주는 방법.
        for j in range(5):
            case=list(combinations([0,1,2,3],j))
            for c in case:
                temp=condition.copy()
                for idx in c:
                    temp[idx]="-"
                key=''.join(temp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()
        
    for q in query:
        q=q.replace("and ","")
        q=q.split()
        
        condition="".join(q[:-1])
        score=int(q[-1])
        cnt=0
        if condition in dic:
            l=dic[condition]
            idx = bisect_left(l,score)
            cnt=len(l)-idx
            # 비록 dic으로 접근속도를 높였다고 해도, 만약 query의 조건들이
            # 만들어놓은 dic의 모든 원소들에 계속 중복된다면? 10만의 제곱이 된다.
            # 이걸 아래처럼 for문으로 돌리면 2중 for문이 되어 안됨.
            # 이분탐색으로 logN만큼으로 시간 복잡도를 낮춰야, 성공할 수 있다.
            # 위에서 지원자의 상태에 따른 score를 정렬해놨으니, 이분탐색이 가능하고
            # 이분탐색에서 탈출한 idx를 l의 길이에서 빼면, 조건을 만족하는 지원자의
            # 수가 된다.
            # for i in range(len(l)):
            #     if l[i]>=score:
            #         idx=i
            #         break
            # cnt=len(l)-idx
        answer.append(cnt)
        
    return answer