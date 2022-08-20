from collections import defaultdict

class Solution:
    """
    DP로 DP[i]에 i개의 충전소를 이용할때 주유할 수 있는 양의 최대값을 station마다 갱신시켜준다.
    갱신되는 조건은, j개의 충전소를 이용해서 채울 수 있는 최대값이, i번째 station의 충전양보다 클떄, (왜냐하면, j->i까지 한번에 올 수 있으니까)
    만약 해당 조건에 걸린다면, "j+1개의 충전소"를 갱신시켜줌.왜냐하면
    예를 들어, j번째 충전소에서 최대 연료량으로, i번째 station까지 갈 수 있다면
    j+1번째를 (이전에 갱신한 j+1번째까지 갈 수 있는 최대 연료량, j번째 + i번째 station의 연료량)중 큰값을 고르면 되기때문.
    왜냐하면, j개의 충전소를 이용했을 때 i번째 충전소까지 갈 수 있다면, j+1개의 충전소를 이용했을때를 갱신시켜줘야하기때문.
    
    중요하게 여겨야할 점은, i 인덱스는 i번째 충전소를 의미하지만 j 인덱스는 j개의 충전소를 이용했을때 가지는 최대값을 의미한다.
    그래서 position<=dp[j]라면, 
    j+1개의 충전소를 이용했을때 최대값을 dp[j+1](=이전까지 갱신해온 값) , dp[j]+fuel(충전소 한개 덜 이용했을때 + 현재 충전소 연료) 중 최대값을 고르면 되는것.
    그래서 각 충전소마다, j개의 충전소를 이용했을때 연료보다 충전소 위치가 작다면, j+1개의 충전소를 이용했을때 연료를 갱신해주는 것.
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = defaultdict(int)
        
        dp[0], n = startFuel, len(stations)
        
        for i in range(n):
            position, fuel = stations[i]
            
            for j in range(i, -1, -1):  #각 충전소를 지날때마다(i) 충전소의 갯수당 최대 충전할 수 있는 가솔린의 양을 dp에 업데이트함.
                if dp[j] >= position:
                    dp[j+1] = max(dp[j+1], dp[j]+fuel)
        for i in range(n+1):
            if dp[i] >= target:
                return i
            
        return -1
