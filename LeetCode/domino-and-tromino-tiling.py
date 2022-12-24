class Solution:
    """
    dp로 규칙을 찾아야한다.
    왜인지 정확히는 모르겠는데, 로직 자체는
    dp[i-1] + dp[i-2]*2 + dp[i-3] + dp[i-4]이다.
    내 생각에는 dp[i-3]도 *2를 해줘야할거같은데, 왜 그런진 모르겠음.
    """
    def numTilings(self, n: int) -> int:
        if n <=3:
            if n==1:
                return 1
            if n==2:
                return 2
            if n==3:
                return 5
        dp = [0 for _ in range(n+1)]

        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        dp[4] = 11

        for i in range(5,n+1):
            dp[i] = (dp[i-1] + dp[i-2]*2 + dp[i-3] + dp[i-4])%1000000007
            
        
        return dp[n]
