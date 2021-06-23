#include <iostream>
#include <stdio.h>

using namespace std;
int dp[101][11] = { 0 };
int max2 = 1000000000;

int main(void) {
	
	int n;
	cin >> n;
	int sum = 0;

	for (int i = 1; i <= 9; i++) dp[1][i] = 1;
	//일단 n=1(한자리 수일때) 모두 1로 배정-> 1입력하면 9 출력

	for (int i = 2; i <= n; i++) {//십~n의 자리까지
		for (int j = 0; j <= 9; j++) {//숫자가 0~9까지 탐색
			if (j == 0) dp[i][0] = dp[i - 1][1] % max2;//j가 0이면 n-1자리는 무조건 1이 와야됨.
			else if (j ==9) dp[i][j] = dp[i - 1][8] % max2;//j가 9면 n-1자리는 무조건 8이 와야됨.
			else dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] % max2;//아닌경우에 +1 -1경우를 합해줌.
		}
	}
	for (int i = 0; i <= 9; i++) sum =(sum+ dp[n][i]) % max2;
	cout << sum << endl;

}
