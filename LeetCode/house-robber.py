class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]

        dp[0]=nums[0]
        dp[1]=nums[1]

        for i in range(2,len(dp)):
            dp[i] = max(max(dp[:i-1])+nums[i],nums[i-1])
        return max(dp[len(nums)-1],dp[len(nums)-2])

