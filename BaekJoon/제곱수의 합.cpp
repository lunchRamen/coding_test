#include <iostream>

using namespace std;

int dp[100001] = { 0 };

int min(int a, int b) { return a < b ? a : b; }

int main() {
	int n;
	cin >> n;

	int count = 0;
	
	//int i;
	//while (1) {
	//	i = 1;
	//	if (n == 0) break;
	//	while (1) {
	//		if ((i * i) > n) {
	//			n = n - (i - 1) * (i - 1);
	//			count++;
	//			break;
	//		}
	//		//if ((i * i) == n) {
	//		//	n = n - (i * i);
	//		//}
	//		i++;
	//	}
	//} 이건 Greedy 알고리즘. 큰거부터 먹어치우는건데 최단경로가 안나오는 경우가 더러 있다.
	//ex) 43의 경우 25 -> 9 -> 9 3번으로 되는데
	//내가 짠 코드의 경우 36->4->1->1->1 5번이 된다.

	for (int i = 0; i <= n; i++) dp[i] = i;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j*j <= i; j++) {
			dp[i] = min(dp[i], dp[i - j * j] + 1);
		}
	}
	//1부터 우리가 구하려고 하는 n까지 밑바닥부터 채워가니까
	//43을 입력했다면

		
	cout << dp[n] << endl;
}
