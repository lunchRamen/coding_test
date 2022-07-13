def solution(nums):
    answer = 0
    answerArr=[]
    pick=len(nums)//2
    
    dic=dict()
    for i in range(len(nums)):
        dic.setdefault(nums[i],0)
        dic[nums[i]]+=1
    while pick:
        for key,value in dic.items():
            if dic[key]>0:
                dic[key]-=1
                answerArr.append(key)
                pick-=1
                if pick==0:
                    break
                
        
    return len(set(answerArr))