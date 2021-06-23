#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>

using namespace std;

int arr[10001] = { 0 };
int result[10001] = { 0 };

int max(int a, int b, int c) {
	int sum = 0;
	if ((a > b) && (a > c)) sum = a;
	else if ((b > a) && (b > c)) sum = b;
	else if ((c > a) && (c > b)) sum = c;
	return sum;
}

int main(void) {
	int n;
	cin >> n;//포도주 잔의 갯수 입력 완료.

	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}//각 위치의 포도주 양 입력 완료.

	result[0] = arr[0];
	result[1] = arr[1];
	result[2] = arr[2]+arr[1];

	for (int i = 3; i <= n; i++) {
		result[i] = max(result[i - 1], result[i - 2] + arr[i], result[i - 3] + arr[i - 1] + arr[i]);
	}
	cout << result[n] << endl;
	
}
