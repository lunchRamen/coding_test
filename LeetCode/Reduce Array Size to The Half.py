class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrSize=len(arr)//2
        dic=dict()
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        dicArr=sorted(dic.items(),key=lambda x:-x[1])
        temp=0
        answer=0
        for i in dicArr:
            temp+=i[1]
            answer+=1
            if len(arr)-temp<=arrSize:
                return answer
        
