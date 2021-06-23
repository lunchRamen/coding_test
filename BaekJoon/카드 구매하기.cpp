#include <iostream>

using namespace std;

int price[10001] = { 0 };
int dp[10001] = { 0 };

int max(int a, int b) { return a > b ? a : b; }
int main() {
	int N;
	cin >> N;
	
	for (int i = 1; i <= N; i++) {
		cin >> price[i];
	}
	//여기서 price[i]는 i개 카드팩의 가격.

	dp[1] = price[1];
	dp[2] = max(price[2], price[1] * 2);
	dp[3] = max(price[3], dp[2] + price[1]);

	for (int i = 4; i <= N; i++) {
		dp[i] = price[i];
		//일단 i개의 카드를 살때 최댓값을 i개 카드팩 값으로 설정해놓고(그래야 max 돌릴수 있으니까)
		for (int j = i-1; j >= 1; j--) {
			dp[i] = max(dp[i], price[j] + dp[i - j]);
			//price[i]+dp[0]~ price[1]+dp[i-1]까지 돌리면서 카드팩의 최댓값을 dp해간다.
			//dp[i]의 경우 dp[i-1]까지가 필요하니까 돌리는데 문제 없다.
		}
	}
	cout << dp[N] << endl;
}
