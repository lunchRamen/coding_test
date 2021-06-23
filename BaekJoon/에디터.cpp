#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <stack>

using namespace std;


//N 10만개 + M 50만개의 최댓값.

//L=커서를 왼쪽으로 한캄 옮김
//D=오른쪽으로 한칸 옮김
//B=커서 왼쪽 문자 삭제
//P=문자를 커서 왼쪽에 추가.
//->커서 기준 왼쪽에 입력을 다 받고
//오른쪽에 명령어를 다 넣는다.

//L연산: 오른쪽 top
int main() {
	char a[600000];
	char* b = new char[];
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin >> a;
	stack<char> left, right;
	//커서 역할을 할 왼오 스택 생성
	int n = strlen(a);
	//n은 문자열 a의 길이.
	//#include <string>말고
	//#include <cstring>으로 쓸수 있다.
	//int n = sizeof(a) / sizeof(char);
	for (int i = 0; i < n; i++) {
		left.push(a[i]);
	}
	//첫번째 입력받은 문자열은
	//
	int m;
	cin >> m;
	for (int i = 0; i < m; i++) {
		char what;
		cin >> what;
		if (what == 'L') {
			if (!left.empty()) {
				right.push(left.top());
				left.pop();
			}//L연산(커서 왼쪽으로 한칸 이동)
		}
		else if (what == 'D') {
			if (!right.empty()) {
				left.push(right.top());
				right.pop();
			}//D연산(커서 오른쪽으로 한칸)
		}
		else if (what == 'B') {
			if (!left.empty()) {
				left.pop();
			}//B연산.커서 왼쪽 삭제
		}
		else if (what == 'P') {
			char c;
			cin >> c;
			left.push(c);
		}//P연산.커서 왼쪽에 문자 추가.
	}

	//출력을 어떻게 할지.
	while (!left.empty()) {
		right.push(left.top());
		left.pop();
	}//커서 왼쪽이 빌때까지
	//오른쪽에다 왼쪽꺼를 넣고 pop
	
	while (!right.empty()) {
		cout << right.top();
		right.pop();
	}//오른쪽이 빌때까지
	//top을 print하고 pop시킴
	//->결론적으로 문장 첫번째 글자부터 출력.

	cout << '\n';
}
