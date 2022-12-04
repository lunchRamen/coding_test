class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        """
        각 인덱스마다, 인덱스를 기점으로 0~i , i+1 ~ len(nums)-1 까지 평균을 구하고, 그 절댓값의 차가 가장 작은 "인덱스"를 return하는 문제.
        input이 10**5이니, 하나의 for문으로만 끝내야한다.
        -> i라는 분기점에 대해, 0~i까지의 합과, i+1이라는 분기점에 대해, i+1~len(nums)-1까지의 합을 저장해놓는 배열 2개를 준비한다.
        그 다음, 절대값 계산을 해서, 최소 평균 차이를 기억해놓는다.
        그 다음, 다시 반복문을 돌면서 해당 idx에서 최소값이 나온다면 그 값을 return.
        """

        temp = [0 for _ in range(len(nums)+1)]
        temp2 = [0 for _ in range(len(nums))]

        sum_nums = sum(nums)

        for i in range(1,len(nums)+1):
            sum_nums-=nums[i-1]
            temp[i]=sum_nums
        temp2[0]=nums[0]

        for i in range(1,len(nums)):
            temp2[i]+=nums[i]
            temp2[i]+=temp2[i-1]       
        
        answer = inf
        
        for i in range(len(nums)):
            if i == len(nums)-1:
                answer = min(answer,abs(temp2[i]//len(nums)))
                continue
            else:
                answer = min(answer, abs(temp2[i]//(i+1) - temp[i+1]//(len(nums)-(i+1))))
    
        for i in range(len(nums)):
            if i == len(nums)-1:
                if answer == abs(temp2[i]//len(nums)):
                    return i
            else:
                if answer == abs(temp2[i]//(i+1) - temp[i+1]//(len(nums)-(i+1))):
                    return i
