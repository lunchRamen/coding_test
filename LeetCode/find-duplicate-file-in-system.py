from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """
        파일의 "내용"이 중복되는 파일경로들을 arr로 묶어서 전달한다.
        그냥 문자열 자르기를 잘하면 됨.
        """
        dic = defaultdict(list)
        
        for path in paths:
            keywords= path.split(" ")
            keyword= keywords[0]
            for i in range(1,len(keywords)):
                temp = keywords[i].split("(")
                detail = keyword+"/"+temp[0]
                key = temp[1][:len(temp[1])-1]
                dic[key].append(detail)
        answer=[]
        for value in dic.values():
            if len(value)>=2:
                answer.append(value)
        return answer
        
