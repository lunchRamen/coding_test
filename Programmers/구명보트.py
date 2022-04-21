from collections import deque
"""
구명보트는 한번에 최대 2명씩밖에 못탐.
-> 구명보트는 2명 혹은 한명이 탐
그래서 정렬한건 큐에 넣고,
앞 뒤를 비교해서 합한게 limit보다 작으면, 둘다 탈 수 있고
아니면 무거운 사람만 탈수 있다.
그리고 이 조건을 거칠때마다 보트는 1개씩 나감.
"""
def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    print(deq)
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer