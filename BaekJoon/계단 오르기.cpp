#include <iostream>

using namespace std;

int stairs[301] = { 0 };
int dp[301] = { 0 };

//int max(int a, int b,int c) {
//	int result = 0;
//	if (a > b&& a > c) result = a;
//	if (b > a&& b > c) result = b;
//	if (c > a&& c > b) result = c;
//	return result;
//}
int max(int a, int b) {
	return a > b ? a : b;
}

int main() {
	int n;
	cin >> n;
	int ans = 0;

	for (int i = 1; i <= n; i++) {
		cin >> stairs[i];
	}
	//dp[n] = stairs[n];//1
	//dp[n -1] = stairs[n] + stairs[n - 1];//1 2
	////다음꺼 이어지려면
	//dp[n - 2] = dp[n] + stairs[n - 2];//1 3( 2 3 은 안됨. 1을 무조건 밟아야 돼서)
	////dp[n-3] 4번째 계단부터 124	134 나뉨.
	////dp[n-4] 5번째는 1245 135 되는데 1345는 3개가 겹치니까 제외.
	////dp[n-5] 6번째는 12456 1246 1346 1356 되는데 12456은 3개가 겹치니까 제외.
	////-> 연속되게 3개 계단을 오르는 경우를 예외처리해줘야됨.
	////계단을 구할때 n+2는 모든 경우 퐘됨
	//

	////포도주처럼 

	//for (int i = n - 2; i >= 1; i--) {
	//	dp[i] = max(dp[i+1],dp[i+2] + stairs[i]);    
	//}
	//ans = max(dp[1], dp[2])+stairs[1];
	//cout << ans << endl; 
	////이거는 맨 윗 계단을 무조건 밟아야 되니까 윗계단을 밟고 밑으로 가는 top down 방식
	dp[0] = 0;
	dp[1] = stairs[1];
	dp[2] = stairs[1] + stairs[2];
	//2번째는 
	dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3]);


	for (int i = 4; i <= n; i++) {
		//if (i == n) {
		//	dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]);
		//	//i가 n일때는 해당 계단을 무조건 포함해야 돼서 n번째 계단을 포함하는 경우만 max 비교해주면 됨.
		//}
		//dp[i] = max(dp[i - 1], dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]);
		////			12	13	23
		////직접 손코딩해보면 보임. dp[i-1]은 이전꺼 2개 합한거고
		////dp[i-2]는 2번째 전꺼니까 이번꺼 해도되고
		////dp[i-3]은 2개 안골랐으니까 이전꺼랑 이번꺼 골라야됨.
		dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i]);
	}

	cout << dp[n] << endl;




}
