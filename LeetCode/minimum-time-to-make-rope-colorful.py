class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        arr = []

        """
        dp나 그리디로 풀라고 되어있는데, 그냥 빡구현으로 풀었다.
        색깔이 겹쳐있는 풍선의 경우, 같은것의 index까지 구한다음,
        그 중 max_needed_time을 구한다.
        max_needed_time빼고 나머지는 일단 arr에 추가한다.
        근데, max_needed_time이 여러개인 경우가 있다.
        그러면 그중 하나만 남기고 지워야한다.
        그래서 cnt로 max_needed_time갯수를 구한다음, 1개 빼고 다 추가한다.
        """

        i = 0
        while True:
            if i >= len(colors)-1:
                break
            idx = 0
            if colors[i]==colors[i+1]:
                idx = i+2
                while idx!=len(colors):
                    if colors[i]!=colors[idx]:
                        break
                    idx+=1
                max_num = 0
                for j in range(i,idx):
                    max_num = max(max_num,neededTime[j])
                for j in range(i,idx):
                    if neededTime[j]!=max_num:
                        arr.append(neededTime[j])
                cnt = 0
                for j in range(i,idx):
                    if neededTime[j]==max_num:
                        cnt+=1 #max_num과 같은게 총 몇개인지.

                if cnt>1:
                    for j in range(1,cnt):
                        arr.append(max_num)
            else:
                i+=1
                continue
            i=idx
        return sum(arr)
