#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
rgb거리
N개의 집.거리는 선분(1차원 배열)
1번~N번까지의 집이 있음.
집은 빨 초 파 중 하나로 칠해야됨.

색을 칠할때 연속해서 칠하면 안됨.
->i번째 집을 칠할때 i-1번째의 색깔 말고 사용.

1~N까지의 집들에 대해 각각의 집들에 R G B 페인트를 칠하는데 필요한 비용을 입력받는것.
*/
int a[1001][3];
int dp[1001][3];
//dp[i][j] -> i번째 집을 j로 칠할때 1~i번째 집을 칠하는데 드는 비용의 최소값.
//0=R 1=G 2=B로 하자.

//dp[i][0]=min(dp[i-1][1],dp[i-1][2])+a[i][0];
//dp[i][1]=min(dp[i-1][0],dp[i-1][2])+a[i][1];
//dp[i][2]=min(dp[i-1][0],dp[i-1][1])+a[i][2];

//a[i][j] =i번 집을 색 j로 칠하는 값의 최소값.
int min(int a, int b) { return a < b ? a : b; }
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> a[i][j];
		}
	}
	dp[1][0] = a[1][0]; dp[1][1] = a[1][1]; dp[1][2] = a[1][2];
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 3; j++) {
			dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + a[i][0];
			dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + a[i][1];
			dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + a[i][2];
		}
	}

	cout << min(min(dp[n][0], dp[n][1]), dp[n][2]) << endl;

}
