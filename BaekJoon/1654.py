import sys

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start=1
end=arr[-1]

while start<=end:
    mid=(start+end)//2

    num=0
    for node in arr:
        num+=node//mid
    if num>=m:
        start=mid+1
    else:
        end=mid-1
print(end)