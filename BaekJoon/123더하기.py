import sys

input=sys.stdin.readline

"""
정수 n을 1,2,3의 합으로 나타내는 경우의 수
-> 중복순열 허용.
"""

t=int(input())

dp=[0 for _ in range(11)]

dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,11):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

while t:
    n=int(input())
    print(dp[n])
    t-=1