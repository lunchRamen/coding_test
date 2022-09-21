class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        2중 for문은 안되고, 하나의 반복문으로 끝내야함.
        -> 일단 짝수인 배열의 원소들을 sum_으로 만들어 놓는다.
        그 다음, 4가지 경우를 따져보면 됨.
        1. 짝수였는데 짝수가 됨
        2. 짝수였는데 홀수가 됨
        3. 홀수였는데 짝수가 됨
        4. 홀수였는데 홀수가 됨.
        각 경우에 따라 처리를 해주면, for문 하나로 짝수인 합계들을 구할수 있따.
        """
        answer=[]
        sum_=0
        for i in range(len(nums)):
            if nums[i]%2 ==0:
                sum_ += nums[i]
        
        
        for val,idx in queries:
            if nums[idx] %2 ==0 and (nums[idx]+val)%2 ==0:
                answer.append(sum_+val)
                sum_+=val
                nums[idx]+=val
            elif nums[idx]%2 == 0 and (nums[idx]+val)%2 ==1:
                answer.append(sum_-nums[idx])
                sum_-=nums[idx]
                nums[idx]+=val
            elif nums[idx]%2 == 1 and (nums[idx]+val)%2 ==0:
                answer.append(sum_+nums[idx]+val)
                sum_+=nums[idx]+val
                nums[idx]+=val
            else:
                answer.append(sum_)
                nums[idx]+=val
        return answer
