#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
동물원
가로로 2칸 세로로 N칸인 우리가 있다.
이 우리엔 사자들이 살고 있는데, 사자들을 우리에 가둘 때
가로로도 세로로도 붙어있게 배치 X
->대각선으로만 배치 가능.

사자를 0마리부터 배치를 하는데
조건에 맞게끔 최대한 꽉 찰 때까지

하나의 가로에 대해서
안놓는거 왼쪽 오른쪽 3가지 경우 가능.
dp[n][0]=배치 x
dp[n][1]=왼쪽
dp[n][2]=오른쪽

앞에 놓인 경우 생각
dp[n][0]경우 ->dp[n-1][0],[1],[2] 다 가능
dp[n][1]경우 ->dp[n-1][0],[2] 가능
dp[n][2]경우 ->dp[n-1][0],[1] 가능

->dp를 2차원 배열로 설정할때는
뒷배열엔 방향,색깔등등 표시를 해줘야 할때 쓴다.
*/

int dp[100001][3];
int mod = 9901;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	dp[1][0] = 1; dp[1][1] = 1; dp[1][2] = 1;
	
	for (int i = 2; i <= n; i++) {
		dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2];
		dp[i][1] = dp[i - 1][0] + dp[i - 1][2];
		dp[i][2] = dp[i - 1][0] + dp[i - 1][1];
		
		dp[i][0] %= mod; dp[i][1] %= mod; dp[i][2] %= mod;
	}

	cout << (dp[n][0] + dp[n][1] + dp[n][2]) % mod << endl;
}
