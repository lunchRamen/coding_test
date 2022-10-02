from itertools import combinations
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        output나오는 수 보니, 연산결과가 아니라 연산의 규칙을 찾아서, 저장하는 dp로 풀어야함.
        recursion + dp로 풀었다.

        (5,6,18)로 주어진 경우
        주사위가 1개 적을때, 구해지는 경우의 수는
        (4,6,12~17)의 총 6개 경우의 수이다. 이는 곧, (d-1,f,(target-f~ target-1))까지의 경우의 수가 된다
        이걸 d==0이 될때까지 반복하며, 만약 주사위가 0이 될때까지 target을 0이하로 만들었다면, 만드는 경우가 있다는거라 1.아니면 0.
        그 다음, 만약 (d,target)의 경우의 수가 있다면, memo에 적혀있는걸 바로 return해준다.
        만약 없다면, target-f ~ target까지 for문을 돌리면서
        top down방식으로 경우의수를 더해간다. 그 다음, 딕셔너리에 저장하고 해당 값을 return한다.
        이를 흐름으로 보면
        (5,18)
        -> (4,12~17)
        -> (3,6~11)
        -> (2,0~5)
        -> (1,-6~-1)
        -> (0,-12~-7)
        이 되면서
        d==0일때부터 return되며 올라간다.
        0일때는 다 음수이기때문에 
        d==0이 될때까지는 모든 주사위의 경우에 만들 수 있다는것이므로 1이 return되면서, 이게
        memo[(1,-6~-1)]로 저장된다.
        memo[(1,-6~-1)]은 다 6이됨.(왜냐하면 그 전에 target이 다 0이하니까)
        또한 여기도 다 0이하라서 더해간다.

        """
        memo = {}
        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for k in range(max(0, target-f), target):
                to_return += dp(d-1, k) #재귀 호출 되는 부분.
            memo[(d, target)] = to_return
            return to_return
        
        
        return dp(d, target) % (10**9 + 7)
