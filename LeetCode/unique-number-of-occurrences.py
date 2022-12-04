from collections import defaultdict
class Solution:
    """
    배열 arr에서, 각 숫자들의 "빈도수" 가 겹치는 경우가 생기는지 판단하는 문제.
    arr의 원소들을 dic의 key로, 빈도수를 value로 count해준다.
    그 다음, values만 따로 빼서, 이걸 set으로 만든 것과 비교했을때 길이가 같으면 True, 다르면 False return.
    """
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dic = defaultdict(int)

        for i in arr:
            dic[i]+=1
        
        arr = dic.values()
        setArr = set(arr)

        if len(arr)==len(setArr):
            return True
        else:
            return False
