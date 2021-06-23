#include <iostream>

using namespace std;

long long dp[101] = { 0 };

int main() {
	int T;
	cin >> T;
	dp[1] = 1;
	dp[2] = 1;
	dp[3] = 1;
	dp[4] = 2;
	dp[5] = 2;



	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;
		for (int i = 6; i <= 101; i++) {
			dp[i] = dp[i - 1] + dp[i - 5];
		}
		cout << dp[n] << endl;
	}
}
