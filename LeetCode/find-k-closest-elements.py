from collections import defaultdict
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
       
        """
       졍렬된 배열 arr
       주어진 정수 k,x
       
       x와 거리가 가까운순으로 k개를 배열형태로 return.
       
       문제에서는 이분탐색 혹은 Heap으로 풀라고 되어있었는데
       딕셔너리로 푸는게 익숙해서 풂.
       
       x와의 거리의 절대값을 key로, 각 element값을 value로 list를 만든다음
       answer에 더하는데, answer의 길이가 k가 넘으면 break걸어서
       k가될때까지 pop시킨다.
       """
        dic = defaultdict(list)
        
        for i in arr:
            dic[abs(i-x)].append(i)
            
        temp = list(dic.keys())
        temp.sort()
        answer=[]
        for i in temp:
            answer+=dic[i]
            if len(answer)>=k:
                break
        while True:
            if len(answer)==k:
                break
            answer.pop()
        answer.sort()
        return answer
