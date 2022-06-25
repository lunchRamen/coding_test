import sys


input=sys.stdin.readline

n,l=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()

"""
물을 막을때 적어도 그 위치에 좌우 0.5만큼 간격을 준다.

예를들어 테이프 길이가 2이고
물 새는곳이 1,2,100,101이라면

0.5~2.5까지 한개
99.5~101.5까지 한개 해서 총 2개가 든다.

-> 물샌곳 for문 돌면서 원소당 while문으로
    테이프 한개당 몇개까지 커버 쳐지는지 확인
"""

i=0
cnt=0

flag=False
while True:
    if flag:
        break
    start=arr[i]-0.5
    end=start+l
    j=i+1

    cnt+=1
    while True:
        if j>=len(arr):
            flag=True
            break
        if arr[j]>end:
            i=j
            break
        j+=1
print(cnt)