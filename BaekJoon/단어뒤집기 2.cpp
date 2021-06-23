#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
단어 뒤집기와 다른점.
<>가 있으면 그대로 출력.
*/

void print(stack<char> &s) {//레퍼런스를 받음. 같은 메모리공간 공유.
	while (!s.empty()) {
		cout << s.top();
		s.pop();
	}//스택이 비워질때까지 다 출력하고 pop.
}

/*
for each문 혹은 switch문으로 어떻게 분기를 잡을지 정해줘야되는데
문제같은경우 tag라는 bool변수를 둬서
<가 시작될때부터는 tag를 true로 두고
>로 끝날때는 tag를 다시 false로 둬서
ch가 <면 그전까지 stack에 쌓아뒀던걸 모두 출력하고
if(tag)로 tag가 true인 동안은 그냥 cout<<ch로 한다.

else(ch가 <도 >도 아닌경우)
만약 띄어쓰기 문자라면 그 전까지를 stack에서 뱉어내고
이것도 아닌경우(그냥 문자열의 경우) stack에 문자들을 push한다.

여기서 중요한점 -> 문자에따라서 조건문 설정을 잘 해줘야한다.(순서가 중요)
*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	string str;
	getline(cin, str);
	bool tag = false;
	stack<char> s;

	for (char ch : str) {
		if (ch == '<') {
			print(s);
			tag = true;
			cout << ch;
		}
		else if (ch == '>') {
			tag = false;
			cout << ch;
		}
		else if (tag) {
			cout << ch;
		}
		else {
			if (ch == ' ') {
				print(s);
				cout << ch;
			}
			else s.push(ch);
		}
	}
	print(s);
	cout << '\n';

}
