#include <iostream>
#include <stdio.h>

using namespace std;

int arr[1001] = { 0 };
int dp[1001] = { 0 };

int max(int a, int b) { return a > b ? a : b; }
int main() {
	int n;
	cin >> n;
	int length = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if ((arr[i] < arr[j]) && (dp[i] < dp[j] + 1)) dp[i] = dp[j] + 1;
		}
	}
	for (int i = 0; i < n; i++) length = max(length, dp[i]);
	cout << length << endl;
}
