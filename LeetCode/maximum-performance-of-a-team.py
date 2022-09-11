class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        """
        performance = sum(speed) * min(efficiency)다.
        여기서, efficiency가 낮게되면, engineer를 추가해봤자 효율이 나오지 않는다.
        이걸 간과하고, 그냥 speed*efficiency가 최대인것만 구했다가, 정답이 나오지 않음.
        
        그렇다면, 어떻게 구해야하나?
        -> 우리는, "효율성이 높은 순서"로 speed의 합과 곱했을때의 결과인 performance를 갱신해나가야한다.
        이러려면, 효율성 순서로 for문을 한번 돌리고, speed로 for문을 한번 더 돌려야한다.
        근데, input을 보면 max TimeComplexity = O(NlogN)으로써,
        for문을 2개 돌리면 시간초과가 난다. -> O(logN)짜리 시간복잡도로 speed를 구해야한다.
        그래서 heapq가 필요함.
        
        로직은, 효율성순으로 내림차순 정렬한 arr을 다 돌면서
        list에 넣은 speed의 갯수가 k개 이상일때마다 pop,push
        미만이면 push하면서, 해당 원소를 넣었을때의 performance(speedSum*eff)와
        그 이전까지 performance의 최대값을 비교해서, performance를 갱신한다.
        
        이게 되는 이유는, 효율성이 높은순으로 performance를 갱신하기때문에,
        무조건 해당 engineer의 효율성이 최소라서 speedSum*eff가 performance가 되고,
        만약 해당 engineer의 효율성을 곱했을때 더 작다면, 해당 engineer를 배제하면 되기때문에.
        
        또한 speed의 경우 정렬되지 않았기때문에 arr를 돌면서 speedSum을 갱신하고,
        speedSum을 구성하는 engineer의 speed중 최소를 pop시키고, 지금껄 넣어봤을때
        갱신되는지 확인하면 된다.
        """
        arr = sorted(zip(speed,efficiency),key = lambda x:-x[1])
        print(arr)
        speedSum = 0
        performance = 0
        list_ = []
        for i in range(len(arr)):
            eff = arr[i][1]
            sp = arr[i][0]

            if len(list_)==k:
                speedSum -= heappop(list_)
            
            speedSum+=sp
            heappush(list_,sp)
            performance = max(performance, speedSum*eff)
            
            
        return performance%(10**9+7)
