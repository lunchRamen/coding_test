import sys

input=sys.stdin.readline

"""
dp[n][k]짜리 2차원 배열을 만든다.
이후 dp로 bottom up을 하는데
dp[i][j]는 무게가 j일때 최대의 가치를 담는다.

기본적인 dp설정.

j<weight (j가 현재 비교할 물건의 무게보다 작을때)
dp[i-1][j] (이전물건의 가치값을 그대로 가져옴.)
왜냐? 해당 무게의 가치값중 최대값을 dp로 채워가면서 왔기때문.

j>=weight (현재 비교할 물건의 무게랑 같을때부터)
max(dp[i-1][j-weight]+value,dp[i-1][j])
이전물건까지 조사한 해당 무게의 최대 가치값과,
현재 물건을 넣어준 상태에서,(value) 이전 물건까지 조사해봤을때
현재 물건을 뺀 무게에서의 최대값을 더해준다(dp[i-1][j-weight])

그래서 value+dp[i-1][j-weight]이 될때는
이전 물건까지의 dp에서 현재물건을 뺀 무게에 다른 값이 있을때.

dp[i-1][j]가 될때는 이전 물건까지 가치를 구한 값이
현재 물건의 가치보다 크고, 현재 물건을 뺀 무게에 해당하는 짐이 없을 경우이다.
"""

n,k=map(int,input().split())

product=[[0,0]]

for _ in range(n):
    w,v=map(int,input().split())
    product.append([w,v])

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

product.sort(key=lambda x:x[0])

for i in range(1,n+1):  #무게
    weight=product[i][0]
    value=product[i][1]
    for j in range(1,k+1):  #가치
        if j<weight:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight]+value)

print(dp[n][k])


