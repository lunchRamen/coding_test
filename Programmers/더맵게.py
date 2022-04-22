from collections import deque
import heapq
"""
힙 카테고리 문제답게, deque로 안풀리고 heapq를 써야함.
Heap의 장점?
정렬된 상태의 완전 이진트리. 그래서 최대값, 최소값으로 정렬된 상태에서
삽입,삭제가 일어나면 비교가 O(logN)만큼만 일어나면 되기때문에 통과하는듯.

heapq의 사용법
heapq.heapify(list) = 인자로 넣은 리스트를 heap자료형으로 바꿔준다.
heapq.heappush(list,value) = list에 heapify된 값을 넣어준다.
heapq.heappop(list) = list에 최소값을 가져온다. 

주의해야할 점은, 먼저 heapify해놓고, heappush,heappop을 할것
그리고 왠진 모르겠는데, while문에서 heapify를 시작하면 효율성이 통과못함.

"""
def solution(scoville, K):
    answer = 0
#     scoville.sort()
#     q=deque(scoville)
    
    
#     while q:
#         flag=True
#         for i in range(len(q)):
#             if q[i]<K:
#                 flag=False
#                 break
#         #만약 모든 음식의 스코빌이 K이상이면
#         if flag:
#             break
        
#         p1,p2=q.popleft(),q.popleft()
#         mixP=p1+(p2*2)
#         q.append(mixP)
#         temp=list(q)
#         temp.sort()
#         q=deque(temp)
#         answer+=1
    heapq.heapify(scoville)
    while scoville:
        lenScoville=len(scoville)
        temp1=heapq.heappop(scoville)
        if temp1>=K:
            break
        elif temp1<K and lenScoville==1:
            answer=-1
            break
        temp2=heapq.heappop(scoville)
        temp=temp1+(temp2*2)
        answer+=1
        heapq.heappush(scoville,temp)
        
    return answer