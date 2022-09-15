from collections import defaultdict
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        answer = []
        """
        역시나 dict쓰는 문제.(2중 for문 안됨)
        일단 changed를 정렬하고, changed를 돈다
        
        val을 다양한 조건으로 dic에 값추가, 수정,삭제를 진행한다.
        만약 val/2(역으로보면 twice)가 dic에 이미 있다면,
        dic[val/2]를 -=1한다. -> 왜냐하면, changed를 정렬해서 무조건 값이 작은거부터 순회하기떄문.
        만약 val/2가 이전에 이미 dic에 추가되었고, 현재 다시 검색했을때 나온다면 -> twice되는 수가 현재값.
        그래서 dic[val]-=1했을때 0이됐다면 -> 짝을 찾은 수라서 dic에서 지운다.
        
        여기서 특이점이라고하면 answer.append는 val/2가 dic에 있다면 무조건 일어난다. 왜냐하면 2배가 된 수를 찾은거니까.
        다만, dic[val/2]를 -1 했을때 0이면 삭제하는건 val/2가되는 다른 수가 해당 조건문에 걸리지 않게 하기 위하여.(in은 값이 뭐든 있으면 찾으니까)
        그래서 val/2가 없다면, dic에 추가해서 진행.
        """
        if len(changed)%2 ==1:
            return []
        
        changed.sort()
        dic=defaultdict()
        
        for val in changed:
            if val/2 in dic:
                dic[val/2]-=1
                if dic[val/2] == 0:
                    del dic[val/2]
                answer.append(int(val/2))
            else:
                if val not in dic:
                    dic[val]=1
                else:
                    dic[val]+=1
        if len(answer)*2 == len(changed):
            return answer
        else:
            return []
                    
