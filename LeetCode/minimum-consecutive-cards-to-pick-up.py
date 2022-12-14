from collections import defaultdict
"""
cards 배열이 주어졌을때, 같은 숫자가 2번 등장할때까지의 간격이 가장 좁은 경우를 return한다.

일단 dict으로 각 카드 숫자에 대해 위치값을 list형태로 집어넣는다.
만약, list의 길이가 모두 2 미만이라면 -> 쌍이 없으므로 -1를 return.
아니라면, dic.values를 탐색하며 두 간격사이가 최소인걸 memozation하여 return 한다.
"""
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:

        dic = defaultdict(list)

        for i in range(len(cards)):
            dic[cards[i]].append(i)
        
        if max(map(len,dic.values()))<2:
            return -1

        answer = inf

        for value in dic.values():
            for i in range(len(value)-1):
                answer = min(answer,abs(value[i]-value[i+1])+1)
        return answer
