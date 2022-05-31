import sys

input=sys.stdin.readline

n=int(input())

arr=[]

for _ in range(n):
    temp=list(map(int,input().split()))
    arr=arr+temp
    arr.sort(reverse=True)
    arr=arr[:n]

print(arr[n-1])