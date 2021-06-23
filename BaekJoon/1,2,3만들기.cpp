#include <iostream>

using namespace std;

/*
9095 1,2,3 더하기
정수 n이 주어졌을때 n을 1 2 3의 합으로 나타낼수 있는 경우의 수 반환
ex) n이 4인 경우
1 1 1 1
1 2 1
1 3
2 1 1
1 1 2
3 1
2 2
총 7개.

n이 10까지니까 n!이여도 문제가 없음 -> brute force로 풀어도 됨.
시간 단축은 dp로 풀어도 됨. 두 가지 모두로 풀어보기.
brute force를 재귀형태로 풀어도 됨.

1.재귀
solve(0)으로 두고 n이면 cnt+1 >n이면 return <n이면 solve(+1,+2,+3)해줌.

2.dp
1~10까지 직접 구해보면서 규칙성을 찾고, dp[k]엔 k번째 수에 대해 1,2,3으로 만들 수 있는 수의 총 집합을 넣는걸로.

*/

int n;
int cnt;

int dp[11];
//void solve(int start) {
//	if (start==n) {
//		cnt++;
//		return;
//	}
//	if (start > n) return;
//
//	if(start<n) {
//		solve(start + 1);
//		solve(start + 2);
//		solve(start + 3);
//	}
//} 재귀

int main(void) {
	int t;
	cin >> t;
	//while (t--) {
	//	cnt = 0;
	//	cin >> n;
	//	solve(0);
	//	cout << cnt << endl;
	//}
	dp[1] = 1;
	dp[2] = 2;
	dp[3] = 4;
	for (int i = 4; i <= 10; i++) {
		dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1];
	}
	while (t--) {
		cin >> n;
		cout << dp[n] << endl;
	}
}
