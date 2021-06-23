#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

/*
괄호 문자열
(와 )가 쌍으로 닫히게끔.

( ( ( ) ) ) ( ( () ) () ) ).
*/
string valid(string s) {
	int cnt = 0;
	for (int i = 0; i < s.size(); i++) {//문자열의 크기만큼 돈다.
		if (s[i] == '(') {//(이면 cnt를 추가시킴
			cnt++;
		}
		else//아니면 cnt를 감소시킴
			cnt--;
		if (cnt < 0) return "NO";//cnt가 0보다 작다->)가 더 많다.
	}
	if (cnt == 0) return "YES";//cnt가 0이다 -> (와 )가 동일하다.
	else return "NO";//cnt가 0이 아니다 ->틀렸다.
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	while (t--) {
		string s;
		cin >> s;
		cout << valid(s) << "\n";
	}
}
