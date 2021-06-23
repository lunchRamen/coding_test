#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int p[10001];
int dp[10001];

int min(int a, int b) { return a < b ? a : b; }

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> p[i];
		dp[i] = 1000 * 10000;
	}
	//dp[i]도 for문 돌려서 값을 채워 넣는 이유
	//->전역 배열의 경우 초기화가 0으로 되어있는데
	//이 경우 min을 돌리면 항상 초기화된 값이 들어갈 거기때문에
	//카드의 갯수의 최대(N<=1000)과 카드팩 값의 최대(<=10000)을 곱한 값을 dp[i]에 설정하면
	//dp[i]는 항상 최대값으로 설정되기 때문에 min을 돌리는데 지장이 없다.

	//for (int i = 1; i <= n; i++) {
	//	dp[i] = -1;
	//}

	//for (int i = 1; i <= n; i++) {
	//	for (int j = 1; j <= i; j++) {
	//		if (dp[i] == -1 || dp[i] > dp[i - j] + p[j])
	//			dp[i] = dp[i - j] + p[j];
	//	}
	//}
	//위 경우는 dp를 -1로 두는것인데 이걸 조건검사로 하고
	//위의 경우(dp를 안채워 넣었거나) dp[i]가 dp[i-j]+p[j]보다 클때(min조건)면
	//dp[i]를 갱신해주는 방법.
	//이 경우를 더 추천하는 이유는 이렇게 값을 구하는 문제가 아닌 경우의 수를
	//구하는 문제의 경우 0을 경우의 수로 세는 상황이 발생해서 그럼.

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i] = min(dp[i], dp[i - j] + p[j]);
		}
	}
	cout << dp[n] << endl;
}

