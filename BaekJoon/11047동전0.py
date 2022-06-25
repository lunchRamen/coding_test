import sys


input=sys.stdin.readline

n,k=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
answer=0
while k:
    for coin in arr:
        if coin<=k:
            answer+=1
            k-=coin
            break

print(answer)