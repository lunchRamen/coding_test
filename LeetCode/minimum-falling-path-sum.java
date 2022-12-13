class Solution {
    /*
    가장 먼저 떠올렸던거는 matrix의 마지막 행까지 진행하면서 합을 비교하는 재귀를 떠올렸는데, TLE가 났고,
    이후에 문제 유형을 보니 DP였다.
    DP의 경우 1번째행부터는 이전행의 최소값 + 현재 matrix의 값으로 최소값을 갱신시키고, 마지막 행에 대해 최소값을 return하면 된다.
    주의할 점은 0번째, n-1번째에 대해선 3개를 비교해주면 IndexError가 난다는 점.
     */
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        int[][] dp = new int[n][n];

        for (int i=0; i<n; i++){
            dp[0][i] = matrix[0][i];
        }

        for (int i=1;i<n;i++){
            for (int j=0; j<n ; j++){
                if (j == 0){
                    dp[i][j] = matrix[i][j] + Math.min(dp[i-1][j],dp[i-1][j+1]);
                }
                else if (j == n-1){
                    dp[i][j] = matrix[i][j] + Math.min(dp[i-1][j], dp[i-1][j-1]);
                }
                else{
                    dp[i][j] = matrix[i][j] + Math.min(Math.min(dp[i-1][j-1], dp[i-1][j]), dp[i-1][j+1]);
                }
            }
        }

        int[] min_sum = dp[n-1];
        return Arrays.stream(min_sum).min().getAsInt();
    }
}
