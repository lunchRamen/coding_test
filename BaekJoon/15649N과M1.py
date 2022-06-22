import sys
from itertools import permutations

input=sys.stdin.readline

"""
permutation(순열) 문제.
"""


n,m=map(int,input().split())

arr=[i+1 for i in range(n)]

answer=list(permutations(arr,m))

for i in answer:
    print(*i)