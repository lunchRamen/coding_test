import sys
import bisect


input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
searchArr=list(map(int,input().split()))

arr.sort()

answer=[0 for _ in range(m)]
for i in range(len(searchArr)):
    if searchArr[i] in arr:
        answer[i]=1

for i in range(len(answer)):
    print(answer[i])