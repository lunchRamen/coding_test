from collections import defaultdict
class Solution:
    """
    문자의 빈도에 따라, 문자열을 정렬한다.
    -> input때문에 시간복잡도를 N으로 해줘야한다.
    각 문자열의 문자들의 빈도를 dict으로 저장한다.
    그 다음, key(문자)에 대해선 오름차순, value(빈도수)에 대해선 내림차순으로 정렳나다.
    그리고, 이걸 answer에 key*value만큼 추가해주면 된다.
    """
    def frequencySort(self, s: str) -> str:
        answer=""
        dic = defaultdict(int)
        for i in s:
            dic[i]+=1

        arr = sorted(dic.items(), key = lambda x:(-x[1],x[0]))
        
        for key,value in arr:
            answer+=key*value

        return answer
