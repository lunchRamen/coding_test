import bisect
class MyCalendarThree:
    """
    이분탐색으로 배열을 넣고, 이분탐색으로 검색을 한다.
    start,end배열에 입력받은 book 정보를 넣고,
    end배열을 기반으로 돌린다.
    돌리는 기준은, start배열에서 k와 제일 근접한 idx를 찾는 것
    left로 찾아야 k보다 작으면서 가장 큰걸 찾아준다.
    
    -> for문은 end 배열을 돌면서,
        end배열 원소마다 start배열과 원소를 통해, 해당 end[i]=k와 가장 가까운 start시간의 위치를 찾는다(ind)
        만약 해당 값이 start배열의 길이보다 크면 -> 끝까지 탐사했는데 없다는거니까 이전까지 중 max(ans)를 return
        아니라면 max(ans,ind-i)로 answer를 갱신
        ind-i인 이유는 (end와 가장 가까운 start위치)-(end의 위치)를 해야, 중간에 몇명이 중복되는지 알 수 있기떄문.
    """
    def __init__(self):
        self.start=[]
        self.end = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.start, start)    
        bisect.insort(self.end, end)
        ans = -1
        for i, k in enumerate(self.end):
            ind = bisect.bisect_left(self.start, k)
            if ind > len(self.start):
                break
            ans = max(ans, ind - i)
        return ans
