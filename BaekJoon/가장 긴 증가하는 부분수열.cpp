#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <stdio.h>
#include <stack>
#include <vector>

using namespace std;

/*
가장 긴 증가하는 부분 수열.
수열이 주어졌을때, 가장 긴 증가하는 부분 수열 구하는 방법.

ex) 수열이 10 20 10 30 20 50 으로 주어지면

10 20 30 50이 가장 긴 증가하는 부분수열이고, 길이는 4여서 4를 출력하면 됨.

점화식을 세워보자.

첫번째 원소를 result 배열에 넣고, 두번째 원소와 비교.
크면 배열에 넣고, 아니면 다음 것 탐색.
-> 배열이 커지면 arr[i]의 값이 result배열의 모든 원소보다 큰 경우, result배열에 넣는다.

*/

//int arr[1001] = { 0 };
//int result[1001] = { 0 }; 
//int n;
//int max(int result[], int a) {
//	int count = 0;
//	int x = 0;
//
//	for (int i = 0; i < n; i++) {
//		if (result[i] > a) count++;//만약 result의 원소 하나라도 a보다 크다면 result에 추가 x
//	}
//	if (count == 0) x = a;
//	else x = 0;
//	return x;
//}
//int main(void) {
//	
//	cin >> n;
//	int len;
//
//	for (int i = 0; i < n; i++) {
//		cin >> arr[i];
//	}
//
//	result[0] = arr[0];
//	for (int i = 1; i < n; i++) {
//		int a=max(result, arr[i]);
//		if (a == arr[i]) result[i] = arr[i];
//	}
//	int length = 0;
//	for (int i = 0; i < n; i++) {
//		if (result[i] != 0) length++;
//	}
//	cout << length << endl;
//
//}
//내가 짠 코드는 입력받은 배열에서 result로 넘기는게 arr의 값을 그대로 넘겨준 다음
//result의 초기화를 다 0으로 해뒀기 떄문에 0이 아닌값이면 값이 들어있는거라
//if(result[i]!=0)조건으로 최장길이 부분수열의 길이를 출력했지만
//dp의 경우 dp[0]=1로 하고 모든 반복문 돌때 dp[i]=1로 만든 다음에
//max함수를 돌려서 비교하는 arr[i]가 result

int max(int a, int b) { return a > b ? a : b; }

int arr[1001] = { 0 };
int dp[1001] = { 0 };

int main(void) {
	int n;
	cin >> n;
	int length = 0;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}//수열 입력 완료

	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		for (int j = 0; j < i; j++) {
			if ((arr[i] > arr[j]) && (dp[i]<dp[j]+1)) dp[i] = dp[j] + 1;
		}
	}

	for (int i = 0; i < n; i++) length = max(length, dp[i]);
	cout << length << endl;
}
