#include <iostream>
#include <stdio.h>

using namespace std;


int dp[1001][11] = { 0 };
int mod = 10007;

int main(void) {
	int n;
	int sum = 0;
	cin >> n;

	for (int i = 0; i <=9; i++) dp[1][i] = 1;

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j <= 9; j++) {
			//ex) dp[2][1]=dp[1][1~9] 이런식으로 더해주려면 for문을 하나 더.
			//해당 자릿수는 누적합. dp는 모두 0으로 초기화 해줬으니까
			//dp[i][j]는 그냥 자릿수 채우기용.
			//j에서 0을 추가 안하면->해당 자릿수만 검사.
			//j가 0부터 시작하는 이유->1의 자리부터 모두 검사하려고
			//dp[i][j]=dp[i-1][j...9]까진데
			//시그마(모든 조건의 합)은 +=로 나타내질수 있다.
			for (int k = j; k <= 9; k++) {
				dp[i][j] = dp[i][j] + dp[i - 1][k];
				dp[i][j] %= mod;
				//dp[2][7]=dp[2][7]+dp[1][7~9]
				//7이 오면 7~9까지 올 수 있다(전 숫자들에서 7~9까지
				//들어 올 수 있는 경우들 모두 합한 값)
			}
		}
	}
	for (int i = 0; i <= 9; i++) sum += dp[n][i];

	sum %= mod;

	cout << sum << endl;

}
