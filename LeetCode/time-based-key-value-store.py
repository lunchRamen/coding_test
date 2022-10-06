from collections import defaultdict
class TimeMap:
    """
    get 구현이 중요했던 문제.
    문제에서 가장 중요하게 주어졌는데, set의 timestamp값은 증가한다는것.
    또한, dic[key]를 통해 들어있는 자료형은 "리스트" 라는것
    그러면 단순히 뒤집어서(O(N)) timestamp보다 lte한 값을 찾으면, 그걸 return해주고
    만약 다 돌았는데도 없다는것은, 가장 큰 timestamp보다 크다는것이라서 없어서 ""를 return해주면 됨.
    """

    def __init__(self):
        self.dic = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([value,timestamp])
        return
        

    def get(self, key: str, timestamp: int) -> str: 
        data = self.dic[key]

        if not data: return ""

        for value,t in reversed(data):
            if t<=timestamp:
                return value
        return ""
