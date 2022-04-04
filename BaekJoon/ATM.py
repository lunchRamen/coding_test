import sys

input=sys.stdin.readline

"""

"""

n=int(input())

arr=list(map(int,input().split()))

arr.sort()

temp=0
numSum=0
for e in arr:
    temp+=e
    numSum+=temp
print(numSum)