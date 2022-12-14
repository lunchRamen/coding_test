class Solution {
    /*
    dp문제.
    인덱스를 2개 연속해서 방문하면 안된다는 조건 하에, 배열의 합의 최대값을 return하는 문제.
    인접하면 안되기때문에, i를 기준으로 i-2, i-1에 대한 최대값들과 비교해서 bottom up으로 dp를 푼다.
    i-2를 기준으로는 i-2까지 최대합 + nums[i]
    i-1를 기준으로는 dp[i-1]
    왜 i-2에만 max를 때리냐면 덜 털었음에도 더 많은 돈을 가진 경우가 있을 수 있기때문.
    i-1에는 안하는 이유는, 어차피 현재 nums와 조합 
    */
    public int rob(int[] nums) {
        if (nums.length == 1){
            return nums[0];
        }
        int[] dp = new int[nums.length];

        dp[0] = nums[0];
        dp[1] = nums[1];
        for (int i=2;i<nums.length;i++){
            int[] temp = Arrays.copyOfRange(dp,0,i-1);
            dp[i] = Math.max(Arrays.stream(temp).max().getAsInt()+nums[i], nums[i-1]);
        }
        return Math.max(dp[nums.length-2],dp[nums.length-1]);
    }
}
