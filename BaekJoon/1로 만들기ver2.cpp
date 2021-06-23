#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
DP 기본 개념
->문제를 쪼개서 생각 한다.

직관적으로 1로 만들기 문제를 봤을때
if문 3개 걸어놓고
x가 3으로 나누어 떨어지면 -> 3으로 나누고
    2로 나누어 떨어지면 -> 2로 나누고
	아니면 -1하고
이런 경우로 생각하는데, 이러면 10의 경우 10 -> 9 -> 3 -> 1 로 3번이면 되는걸

10->5->4->3->2->1로 5번 연산을 하게됨.
이러면 DP로 어떻게 해결해야 하는가?

일단 dp문제는 해당 수열의 값을 table에 저장하는 memorization이 핵심이므로
항상 dp배열을 만들고, 여기에는 해당 인덱스 수열의 값을 넣는걸로 한다.

여기서는 구하고자 하는 값이 연산 횟수니까 dp[n]에 해당되는 값은 n을 1로 만드는데 필요한 연산 횟수.
*/

int dp[1000001];
int dp2[1000001];

int topDown(int n) {
	if (n == 1) return 0;
	//n이 1인경우 연산이 필요 없으니 0 return
	if (dp[n] > 0) return dp[n];
	//dp[n]에 값이 있는경우 그대로 return
	dp[n] = topDown(n - 1) + 1;
	//n을 연산하는데 필요한 횟수는 dp[n-1]에+1한 경우
	if (n % 2 == 0) {
		int temp = topDown(n / 2) + 1;
		if (dp[n] > temp) dp[n] = temp;
	}//n이 2로 나누어떨어지는 경우는 연산횟수가 topDown(n/2)+1이고 dp[n]이 temp보다 큰 경우
	 //연산횟수가 temp가 더 작단 뜻이니까 dp[n]에 temp를 넣는다.
	if (n % 3 == 0) {
		int temp = topDown(n / 3) + 1;
		if (dp[n] > temp) dp[n] = temp;
	}
	return dp[n];
}

int bottomUp(int n) {
	dp2[1] = 0;

	for (int i = 2; i <= n; i++) {
		dp2[i] = dp2[i - 1] + 1;//n이 2로도 3으로도 안나눠지는 경우
		if (i % 2 == 0 && dp2[i] > dp2[i / 2] + 1) dp2[i] = dp2[i / 2] + 1;
		if (i % 3 == 0 && dp2[i] > dp2[i / 3] + 1) dp2[i] = dp2[i / 3] + 1;
	}
	//bottom up의 경우 피보나치처럼 점화식을 못세우는 항들까지 dp를 배정해 놓고
	//i~n까지 for문 돌리면서 모든 dp[n]을 채워서 dp[n]을 반환하는 형식.
	//top down의 경우 재귀형식이라 dp를 호출하는게 아닌 본인 스스로를 다시 호출해야돼서
	//temp에 값을 넣어넣고 비교했다면
	//bottom up의 경우 dp를 순차적으로 채워넣기때문에 if문에서 &&로 한꺼번에 비교해서 dp[i]갱신 가능.
	return dp2[n];
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	dp[1] = 0;
	topDown(n);
	bottomUp(n);
	cout << dp[n] << '\n';
}
