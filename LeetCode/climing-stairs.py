class Solution:
    """
    기초적인 dp문제.
    i번째 계단을 올라 갈 수 있는 계단은
    i-1번째 계단까지 올라갈 수 있는 경우의수 + i-2번째 계단까지 올라 갈 수 있는 경우의 수
    이걸 첫번째 계단 = 1가지, 두번째 계단 = 2가지 부터 시작해서 bottop up으로 쌓아감.
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]

        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
