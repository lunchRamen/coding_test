class Solution:
    """
    피보나치 수열이 이전 3개의 원소의 합으로 바뀐 문제
    dp로 풀면된다.
    """
    def tribonacci(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
        return dp[n]
