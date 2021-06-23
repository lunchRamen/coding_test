#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int dp[1001];

int topdown(int n) {
	dp[1] = 1;
	dp[2] = 2;

	dp[n] = topdown(n - 1) + topdown(n - 2);
	return dp[n];
}
int bottomup(int n) {
	dp[1] = 1;
	dp[2] = 2;
	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
		dp[i] = dp[i] % 10007;
	}
	return dp[n];
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	topdown(n);
	bottomup(n);

	cout << dp[n] << '\n';
}
