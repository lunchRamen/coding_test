import sys

input=sys.stdin.readline

n,t=map(int,input().split())

arr=[[] for _ in range(n+1)]
cnt=0

"""
각각의 줄에 대해 스택을 만들고, 그 스택에 push/pop 할때마다 cnt를 1씩 증가시켜 cnt를 출력하면 되는 문제.
"""
for _ in range(n):
    a,b=map(int,input().split())
    while True:
        print(arr[a],cnt)
        if not arr[a]:
            arr[a].append(b)
            cnt+=1
            break
        if arr[a][-1]<=b:
            break
        arr[a].pop()
        cnt+=1
    if b in arr[a]:
        continue
    else:
        arr[a].append(b)
        cnt+=1


print(cnt)