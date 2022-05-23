import sys

input=sys.stdin.readline

"""
stack을 만들어, 0이 있다면 q.pop()
후에 sum(stack)
"""

t=int(input())
arr=[]
while t:
    n=int(input())
    if n==0:
        arr.pop()
    else:
        arr.append(n)
    t-=1

print(sum(arr))