#include <iostream>
#include <stdio.h>

using namespace std;

/*
가장 큰 증가 부분 수열
이번에는 가장 큰 증가 부분 수열의 합을 구하는 문제.
*/
int arr[1001] = { 0 };
int dp[1001] = { 0 };
int max(int a, int b) {
	return a > b ? a : b;
}
int main(void) {
	int n;
	cin >> n;
	int sum = 0;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		dp[i] = arr[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if ((arr[i] > arr[j]) && (dp[i]<dp[j]+arr[i])) {
				dp[i] = dp[j] + arr[i];
			}
		}
	}

	for (int i = 0; i < n; i++) {
		sum = max(sum, dp[i]);
	}
	cout << sum << endl;
}
