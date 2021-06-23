#include <iostream>

using namespace std;

int dp[31] = { 0 };

int main() {
	int n;
	cin >> n;
	
	dp[0] = 1;
	dp[1] = 0;
	dp[2] = 3;
	//dp[3] = 3;

	for (int i = 4; i <= n; i+=2) {
		dp[i] = dp[i - 2] * 3;//먼저 3*2칸짜리로 풀수 있는거 구해놓고
		for (int j = 4; j <= i; j+=2) {
			dp[i] += dp[i - j] * 2;//n= 4 6 8...로 만들어지는 고유형태를 구함.
		}
	}
	cout << dp[n] << endl;
}
