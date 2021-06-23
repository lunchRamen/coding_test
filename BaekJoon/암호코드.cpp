#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>

using namespace std;

int mod = 1000000;

string str;
int dp[5001] = { 0 };

/*
여기선 string의 특징을 이용해서 문제를 푼다.
string은 입력받은 그대로 배열로 쓸 수 있고, 문자열로 입력받았지만
배열의 원소로 접근해서 문자 하나씩 받으면
아스키코드 값으로 계산해서
str[2]='5'라면
str[2]-'0'=5(실제 정수값 5) 가 되기때문에 문자로 받더라도 정수로 무리없이 계산이 가능하다.

*/
int main(void) {
	
	cin >> str;

	if (str[0] == '0') {
		cout << 0;
		return 0;
	}
	//문자열 시작이 0인경우 제외

	dp[0] = dp[1] = 1;
	//i=2부터 돌려야하니까 dp[0]과 dp[1]을 1로 초기화.

	for (int i = 2; i <= str.size(); i++) {
		//반복문을 문자열만큼 돌리고싶으면 str.size()로. 배열을 돌릴때 sizeof(arr)/sizeof(int)와 비슷.
		char a = str[i - 1];
		char b = str[i - 2];
		//i를 2부터 돌리니까 a와 b는 입력받은 정수 문자열의 i-1,i-2 번째로 둔다.
		//그리고 

		if (a == '0' && b == '0') {
			cout << 0;
			return 0;
		}
		//a와 b 모두 0이라면 0이 연속이니까 진행할수 없어서 0 출력하고 끝.

		if (a != '0') dp[i] = dp[i] + dp[i - 1];
		//a만 먼저 조건문을 건 이유는 a로 한자리수 판별. 한자리수인 경우 더함.
		if (b != '0') {
			//b도 0이 아니라면 b a 두자리수 판별. -> b*10 + a가 26보다 작으면 두자리수인 경우를 더함.
			int num = (b - '0') * 10 + (a - '0');
			if (num <= 26) dp[i] = dp[i] + dp[i - 2];
		}
		dp[i] = dp[i] % mod;
	}
	cout << dp[str.size()] << endl;

}
