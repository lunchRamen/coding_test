#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
정수 삼각형

     1
	2  3
   4  5  6
  7  8  9  10
이런형태로 진행 해나가고,
제일 위는 필수 선택

그 아래서부터 이제 계속 두갈래길로 내려가는 형태.
왼쪽아래 or 오른쪽 아래.

(i,j) = i행 j열. = i행의 j번째 수.
-> (4,2) 4열 2행 -> 8.

dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+a[i][j] 
j가 처음과 끝인 경우는 경우가 1가지라 예외처리 해줘야함.
->안해줘도 됨.

i가 2인 경우까지는 경우가 1가지씩 밖에 없으니까 먼저 설정해주고 그다음부터 for문 돌리면 됨.

입력도 행은 1~n까진데
열의 경우 1이면 1 2면 2 ... n이면 n행 까지 있어서 j는 1~i까지로.
*/

int dp[501][501];
int a[501][501];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cin >> a[i][j];
		}
	}

	dp[1][1] = a[1][1];
	dp[2][1] = a[1][1] + a[2][1]; dp[2][2] = a[1][1] + a[2][2];


	for (int i = 3; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + a[i][j];
		}
	}

	int ans = 0;

	for (int i = 1; i <= n; i++) {
		ans = max(ans, dp[n][i]);
	}

	cout << ans << endl;

}
