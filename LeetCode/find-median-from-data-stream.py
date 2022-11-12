from sortedcontainers import SortedList
"""
처음엔 정렬된 상태를 유지해야하니까, heap을 생각했다.
근데, heap으로 heappush를 하고 findMedian시 배열 상태를 확인해봤는데, 홀수인 경우에 대해 정렬이 되지 않더라.
왜 그런진 모르겠는데, 별짓을 다해도 정렬이 안됐음.
그래서, 배열을 추가할때마다 .sort()를 하면 당연히 N^2logN으로 시간초과가 날테니 다른 정렬 라이브러리를 찾아보던 중
SortedList를 찾았다. 이걸 쓰니 통과.
"""
class MedianFinder:

    def __init__(self):
        self.arr =  SortedList()
        self.arrLen=0
        

    def addNum(self, num: int) -> None:
        self.arr.add(num)
        self.arrLen+=1

    def findMedian(self) -> float:
        return self.arr[self.arrLen//2] if self.arrLen%2==1 else (self.arr[self.arrLen//2]+self.arr[self.arrLen//2-1])/2
