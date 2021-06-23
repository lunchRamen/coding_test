#include <iostream>

using namespace std;

int dp[201][201] = { 0 };
int mod = 1000000000;
int main() {
	int n, k;
	cin >> n >> k;
	
	for (int i = 0; i <= n; i++) dp[1][i] = 1;
	//1개로 n을 만들수 있는 가짓수.= 어떤 수든 1가지.

	//2~n까지 for문 돌리면서 채워 넣을 예정
	//기본 틀 dp[k][n]=dp[k-1][0]~ dp[k-1][n]

	for (int i = 2; i <= k; i++) {
		for (int j = 0; j <= n; j++) {
			for (int m = 0; m <= j; m++) {
				dp[i][j] = dp[i][j]+dp[i - 1][m];
				dp[i][j] = dp[i][j] % mod;
			}
		}
	}
	//1. dp[i][j]=dp[i-1][m]으로 하면 오류가 난다.
	//왜냐하면 dp[i][j]=dp[i][j]+dp[i-1][m]을 해줘야 m=0~j까지 dp[i][j]가 갱신되기때문.
	//2. m=0~n까지가 아니라 m~j까지다.
	//왜냐하면 대입할 dp가 dp[i][j]이기 때문에 m을 0~n까지 돌리면 dp[i][j]의 j범위를 벗어나게 된다.
	//ex) dp[2][0...20]으로 0~20을 다 채워나가야하는데 0을 n까지하면 dp[2][0]부터 dp[1][20]값이 들어가게 됨
	//고로 j범위까지만 되는게 맞다.
	//3.큰수로 나누고 나머지를 구할때는 전역변수로 지정해주고 해당 변수로 나머지 연산을 하는게 낫다.
	//그리고 나머지 연산은 for문에 넣어서 따로 한줄 지정해주는게 매 연산마다 mod범위 밖인지 확인하기 좋다.




	cout << dp[k][n] << endl;
}
