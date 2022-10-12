import sys
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """
        삼각형의 조건 중 가장 긴변 < 나머지 두변의합 조건을 이용
        nums를 정렬한 다음 "뒤부터" 검사하면, 가장 둘레가 넓은 삼각형이 나옴.
        """
        nums.sort()

        answer = 0
        for i in range(len(nums)-1,1,-1):
            if nums[i-2]+nums[i-1] > nums[i]:
                answer= max(answer,nums[i-2]+nums[i-1]+nums[i])
            else:
                continue
        return answer
