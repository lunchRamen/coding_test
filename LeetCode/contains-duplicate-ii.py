from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        솔직히 최악의 시간복잡도가 O(N^3)이라 안될줄 알았는데, 됐다
        아마도 갯수가 2개 미만인 원소들을 거른게 큰것 같다.

        딕셔너리에 dic[key] = [등장횟수,[인덱스]]형태로 집어넣는다.
        그다음 등장횟수가 2이상인것들에 대해서만 절대값 조건문을 돌려서 있으면 True 없으면 False return.
        """
        dic = dict()

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=[1,[i]]
            else:
                dic[nums[i]][0]+=1
                dic[nums[i]][1].append(i)

        for value in dic.values():
            if value[0]>=2:
                for i in value[1]:
                    for j in value[1]:
                        if i==j:
                            continue
                        if abs(i-j)<=k:
                            return True
        return False
