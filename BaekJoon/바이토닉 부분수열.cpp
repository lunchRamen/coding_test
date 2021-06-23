#include <iostream>
#include <stdio.h>

using namespace std;

int arr[1001];
int dpL[1001];
int dpR[1001];
int dp[1001];

int max(int a, int b) { return a > b ? a : b; }

int main() {
	int N;
	cin >> N;
	int maxNum = 0;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	//가장 긴 증가하는 부분수열 돌리고 가장 긴 감소하는 부분순열 돌리고 두개 합한것중
	//가장 큰 값이 바이토닉 수열이 된다.(해당 값 기준 왼쫀은 증가 오른쪽은 감소니까)
	// <	<	<	<	<k>	>	>	>	> ->k기준 오른쪽으론 감소하는 부분순열.
	for (int i = 0; i < N; i++) {
		dpL[i] = 1;
		for (int j = 0; j <= i; j++) {
			if ((arr[i] > arr[j]) && (dpL[i] < dpL[j] + 1)) dpL[i] = dpL[j] + 1;
		}
	}
	for (int i = N - 1; i >= 0; i--) {
		dpR[i] = 1;
		for (int j = N - 1; j >= i; j--) {
			if ((arr[i] > arr[j]) && (dpR[i] < dpR[j] + 1)) dpR[i] = dpR[j] + 1;
		}
	}
	for (int i = 0; i < N; i++) {
		dp[i] = dpL[i] + dpR[i];
		if (maxNum < dp[i]) maxNum = dp[i];
	}
	cout << maxNum - 1 << endl;
}
