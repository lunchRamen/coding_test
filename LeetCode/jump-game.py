class Solution:
    """
    cur_range를 갱신해나가며, 0이되면 더이상 앞으로 못가니 False
    len(nums)-2까지 갔고, cur_range>0이면 last_index까지 갈 수 있으므로 True

    cur_range-1을 nums[i]와 비교하는 이유는
    이전 cur_range에서 다음 칸으로 왔으므로. 한칸씩 빼줘야해서 그렇다.

    max로 현재 nums[i]와 cur_range-1를 갱신만 시켜주면 되는 이유는,
    0~nums[i]까지 점프를 할 수 있기때문.
    """
    def canJump(self, nums):
        cur_range = nums[0]
        for i in range(0, len(nums)-1):
            cur_range = max(cur_range - 1, nums[i])
            if cur_range == 0:
                return False
        return True
