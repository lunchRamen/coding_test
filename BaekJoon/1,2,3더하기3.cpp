#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

long long mod = 1000000009LL;
long long dp[1000001] = { 0 };

//뭔가 큰 숫자로 mod연산을 한다? int형 대신 long long형을 써서 overflow를 방지하자.
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	dp[0] = 1;
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 1000000; i++) {
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
		dp[i] %= mod;
		/*if (i -1>= 0) dp[i] += dp[i - 1];
		if (i -2>= 0) dp[i] += dp[i - 2];
		if (i -3>= 0) dp[i] += dp[i - 3];
		dp[i] %= mod;	*/
	}

	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;
		cout << dp[n] << endl;
	}
}
