import sys
from queue import PriorityQueue

input=sys.stdin.readline

"""
문제를 풀려는 생각 자체는 맞았음.
다만 while문에서 매번 arr.sort()를 호출하는게
시간초과를 이끌어낸듯.
heapq나 PriorityQueue를 이용하면 해결됨.
"""

n=int(input())

s=0
arr=PriorityQueue()

for _ in range(n):
    arr.put(int(input()))

while True:
    if arr.qsize()==1:
        break
    a=arr.get()
    b=arr.get()
    s+=a+b
    arr.put(a+b)
print(s)