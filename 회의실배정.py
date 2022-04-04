import sys

input=sys.stdin.readline

"""
회의실을 이용하는 시간이 짧은 순서대로 이어붙이기.
=
회의가 끝나는 시간이 빠른 순서 & 회의 시작시간이 빠른순서
(끝나는 시간이 같을 경우)

그래서 정렬된 배열의 첫 원소의 끝나는시간을 잡아놓고,
배열을 1~n까지 돌면서
해당 회의의 시작시간이 끝나는시간보다 같거나 크면
다음 회의예약을 그걸로 잡음(end_time=arr[i][1])
이러면 최단거리를 구할 수 있다.

"""

n=int(input())

arr=[]

for _ in range(n):
    arr.append(list(map(int,input().split())))

#끝나는 시간이 빠른 순서.
#끝나는 시간이 같을 경우 대비 더 많은 회의를 잡을 수 있는
#시작시간이 더 빠른 순서.
arr.sort(key=lambda x:(x[1],x[0]))

cnt=1
#끝나는 시간 저장.
end_time=arr[0][1]

#이미 정렬된 배열을 도는것이라 끝까지 돌면 총 가능한 회의갯수가 나옴.
for i in range(1,n):
    #만약 시작시간이 끝나는시간보다 같거나 크다면
    if arr[i][0]>=end_time:
        cnt+=1
        end_time=arr[i][1]
print(cnt)