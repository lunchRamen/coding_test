class Solution:
    def numSquares(self, n: int) -> int:

        """
        숫자가 주어졌을때, 제곱들의 합으로 맞춰질 수 있는 수가 주어진다.
        이때, 제곱의 수를 가장 적게써서 n을 만드는 경우?

        1~n까지 가장 적은 제곱수로 더하는값을 저장하는 dp를 만들면된다.

        1~n까지 i를 제곱시킨수를 검사해서, n보다 작으면 1로 초기화시키고, 아니라면 1~i까지 검사하면서 dp[i]의 최소값을 갱신시켜준다.
        이걸로는 최적화가 안돼서, 제곱시켜준 수를 배열로 저장해놓은 다음, 이 배열만 돌면서
        dp[i-j]+1로 최소값을 찾는 로직을 하면 답이 나옴.

        """
        dp: List[int] = [inf for _ in range(n+1)]
        square: List[int] = [1]

        dp[0]=0
        dp[1]=1
        
        for i in range(2,n+1):
            i_square:int = pow(i,2)
            if i_square<=n:
                square.append(i_square)
                dp[i_square] = 1

            for j in square:
                if i<j: break
                dp[i]=min(dp[i],dp[i-j]+1)
        return dp[n]
