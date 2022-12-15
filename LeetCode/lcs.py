"""
전형적인 LCS문제.
dp를 len(s1)+1 , len(s2)+1로 만든 다음,
i==0 or j==0일때는 0으로 마진값을 잡고,
s1[i] == s2[j]일때는 dp[i-1][j-1]+1을
다를때는 max(dp[i-1][j],dp[i][j-1])를 해준다.
같을때는 대각선 +1을 해주는 이유는, s1의 i-1번째까지, s2의 j-1번째까지 최장 연속 수열의 값이 저장되어있고
그 값에 현재 일치하는 문자까지 +1를 해주기때문이고
다를때는 s1의 i-1번째까지와 s2의 j번째까지, s1의 i번째가지와 s2의 j-1번째까지 구한 LCS값 중 최대값이, dp[i][j]의 최대값으로 할당되어야한다.
왜냐하면, LCS는 "연속되지 않아도"되기때문에, 이전 최대값들 중 최대값을 할당받아야하기때문.

이렇게 한 dp의 마지막 원소를 return 해주면 된다.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if i==0 or j==0:
                    dp[i][j] = 0 
                elif text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[len(text1)][len(text2)]
