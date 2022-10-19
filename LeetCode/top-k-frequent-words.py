class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        딕셔너리로 문자열의 빈도수를 저장
        빈도수는 내림차순 사전순은 오름차순으로 정렬
        앞에서부터 k개의 사전순을 return해준다.
        """
        dic = dict()

        for word in words:
            if word in dic:
                dic[word]+=1
            else:
                dic[word]=1

        arr = list(dic.items())
        arr.sort(key = lambda x:(-x[1],x[0]))
        answer=[]
        for i in range(k):
            answer.append(arr[i][0])
        return answer
