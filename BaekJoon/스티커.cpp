#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int arr[2][100001] = { 0 };
int sum[2][100001] = { 0 };

int max(int a, int b) {
	if (a < b) return b;
	else return a;
}

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;
		for (int j = 0; j < 2; j++) {
			for (int k = 0; k < n; k++) {
				cin >> arr[j][k];
			}
		}//여기까지 스티커 배열 입력 받기 완료.

		sum[0][0] = arr[0][0];//1행 1열
		sum[1][0] = arr[1][0];//2행 1열
		sum[0][1] = sum[1][0] + arr[0][1];//1행 2열
		sum[1][1] = sum[0][0] + arr[1][1];//2행 2열

		for (int i = 2; i < n; i++) {
			sum[0][i] = arr[0][i] + max(sum[1][i - 1], sum[1][i - 2]);
			sum[1][i] = arr[1][i] + max(sum[0][i - 1], sum[0][i - 2]);
			//두개 한꺼번에 같이 돌림.
			//해당 행렬에 들어가는 값은 해당 행렬의 값+ 그 전 대각선값이랑 그 전전 대각선중
			//큰값을 넣는다.
			//이렇게 1행 2행부터 시작되게 해서 전,전전 대각선 중 큰값 넣으면
		}
		cout << max(sum[0][n-1], sum[1][n-1]) << endl;//이렇게 최대값 취해주면
		//모든 경우 중 합이 가장 큰 경우로 출력된다.
		//배열이니까 인덱스 생각해서 내가 생각한 값 -1해줘야 내가 원하는 값이 출력된다.


	}


}
