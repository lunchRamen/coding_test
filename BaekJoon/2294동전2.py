import sys

input=sys.stdin.readline

"""
최적해를 찾는 조건
각 동전값에 대해 min(현재값, 현재값-현재코인값 +1) 을 찾으면 된다.
동전값에 대해 작은것 -> 큰것 순으로 탐색하기때문에, 최적해가 dp를 돌면서 찾아진다.
"""

n,k=map(int,input().split())

dp=[10001 for _ in range(10001)]

numList=[]

for _ in range(n):
    num=int(input())
    numList.append(num)

dp[0]=0

for num in numList:
    for i in range(num,k+1):
        dp[i]=min(dp[i-num]+1,dp[i])

if dp[k]==10001:
    print(-1)
else:
    print(dp[k])


# cnt=0 -> 이러면 최소값이 안나옴.
# for i in range(len(numList)):
#     if k<numList[i]:
#         continue
#     else:
#         a,b=k//numList[i] , k%numList[i]
#         if b==0:
#             cnt+=a
#             break
#         else:
#             cnt+=a
#             k=b
#             continue
# print(cnt)



