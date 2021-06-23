#include <stdio.h>
#include <iostream>

using namespace std;

long long int dp[91] = { 0 };

int main() {
	int n;
	cin >> n;
	int sum = 0;
	
	dp[1] = 1;
	dp[2] = 1;
	//두번째까지 들어갈 값들 설정.

	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 2] + dp[i - 1];
	}
	cout <<dp[n] << endl;
}
