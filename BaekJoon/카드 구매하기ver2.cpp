#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int P[10001];
int dp[10001];

int max(int a, int b) {
	return a > b ? a : b;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for(int i = 1; i <= n; i++) {
		cin >> P[i];
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i] = max(dp[i], dp[i - j] + P[j]);
		}
	}
	//이 조건 하나로 dp[i]는 1부터
	//모든 조건을 비교 할 수 있다
	//2중 for문을 사용함으로써 1~n까지 모든 dp를 채워 나가는데
	//1~i까지에 대한 dp[i]의 max를
	//dp[i](0)과 dp[i-j]+p[j]를 j가 1부터 i까지 도니까
	//dp[i-1]+p[j]~dp[0]+p[i]까지 max를 계속 비교해서 가장 큰 값을 dp[i]에 넣는다.

	cout << dp[n] << endl;
}
