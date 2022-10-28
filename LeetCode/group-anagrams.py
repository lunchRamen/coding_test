from collections import defaultdict,Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)
        """
        파이썬 자료구조 자체를 생각해내지 못했다.
        dict으로 각 문자열의 등장횟수를 세주고, 그걸로 어떻게 해야되겠다는 떠올랐는데 구현에 실패.
        딕셔너리에 들어갈 수 있는 값 = immutable한 값이면 자료구조도 가능(tuple,frozenset)한걸 알게되었고
        Counter로 iterable한 객체에 대해 dict형태로 만들어주는것또한 알게되었다.
        """

        for s in strs:
            dic[frozenset(Counter(s).items())].append(s)
        
        return dic.values()
