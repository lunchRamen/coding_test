#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	cin.ignore();
	//숫자를 먼저 입력 받았을때 for문에서 string을 getline으로 받을때 줄단위로 받아서
	//첫번째 줄이 공백으로 남을수 있기때문에 ignore 처리를 해준다.

	for (int i = 0; i < T; i++) {
		string str;
		getline(cin, str);
		str += "\n";
		//문장의 마지막 단어는 띄어쓰기로 알수가 없으니까 마지막에 개행문자로 넣어서 조건식에 같이
		//처리하도록 함  -> 스킬.
		stack <char> s;
		for (char ch : str) {
			if (ch == ' ' || ch == '\n') {
				while (!s.empty()) {
					cout << s.top();
					s.pop();
				}
				cout << ch;
			}
			else s.push(ch);
		}
		//for each문으로 for문 임시변수 ch로 str을 모두 반복하게끔.
		//ch문자(=str의 한글자)가 띄어쓰기거나 개행문자라면 스택이 빌때까지 top을 출력하고 pop
		//if문 안에 ch를 출력한다=공백이나 줄바꿈 출력.
		//else(띄어쓰기나 개행 문자가 아니라면) 스택에 문자들을 집어넣는다.
	}

}
