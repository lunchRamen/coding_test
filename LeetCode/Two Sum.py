class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=dict()
        answer=[]
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=i
        
        for i in range(len(nums)):
            if target-nums[i] in dic:
                if i != dic[target-nums[i]]:
                    answer.append(i)
                    answer.append(dic[target-nums[i]])
                    break
                

        return answer
