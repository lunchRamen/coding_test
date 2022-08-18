import sys


n,m=map(int,input().split())

arr=list(map(int,input().split()))

arr.sort()

start=1
end=arr[-1]

"""
적당한 벌목높이를 찾기위해 1~나무 최대높이에서
mid를 찾아가는 과정.

한번 mid가 갱신될때마다 나무들을 돌면서, 만약 해당 벌목 높이보다 크다면
합계에 추가해놓음.

합계가 m이상이면 -> 벌목 높이가 높아져야함.(start가 mid+1)
합계가 m이하라면 -> 벌목 높이가 낮아져야함.(end가 mid-1)

이걸 start>end가 될때까지 반복했을때 end값이 정답.
"""

while start<=end:
    mid=(start+end)//2

    sumLen=0
    for i in arr:
        if i>mid:
            sumLen+=i-mid
    if sumLen>=m:
        start=mid+1
    else:
        end=mid-1
print(end)