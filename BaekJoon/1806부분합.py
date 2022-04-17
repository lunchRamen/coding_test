import sys
input=sys.stdin.readline
n,s=map(int,input().split())


arr=list(map(int,input().split()))

cnt=100001
summary=0

smallPointer,bigPointer=0,0

while True:
    if summary>=s:
        cnt=min(cnt,bigPointer-smallPointer)
        summary-=arr[smallPointer]
        smallPointer+=1
    elif bigPointer==n:
        break
    elif summary<s:
        summary+=arr[bigPointer]
        bigPointer+=1

print(cnt) if cnt!=100001 else print(0)
