#include <iostream>
#include <stdio.h>

using namespace std;

/*
연속합
2개이상의 부분수열 중 합이 최대가 되는 값.
*/
int arr[100001] = { 0 };
int dp[100001] = { 0 };

int max(int a, int b) {
	return a > b ? a : b;
}
int main() {
	int n;
	cin >> n;
	int answer = 0;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	dp[0] = arr[0];
	answer = dp[0];
	for (int i = 1; i < n; i++) {
		dp[i] = max(dp[i - 1] + arr[i], arr[i]);
		answer = max(answer, dp[i]);
	}
	cout << answer << endl;

}
