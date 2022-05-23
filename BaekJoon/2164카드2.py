import sys
from collections import deque

input=sys.stdin.readline

"""
1~N까지의 N장의 카드.
오름차순으로 카드가 위->아래로 있다.
"""


n=int(input())

q=deque([i+1 for i in range(n)])

while len(q)!=1:
    throw=q.popleft()
    insert=q.popleft()
    q.append(insert)

print(q.popleft())
