#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
쇠막대기

레이저는 ()(연속)으로
쇠막대기는 (  )로.

잘려진 쇠막대기의 갯수(길이 X)를 구하는 문제.
()->레이저가 나왔을때는 스택의 크기만큼 쇠막대기 갯수가 늘어난다.

쇠막대기를 n번 자른다 -> 잘려진 갯수는 n+1이다.

고로 )가 나왔을때 갯수를 +1해줘야된다.
*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	string str;
	getline(cin, str);
	int n = str.size();
	stack<int> s;
	int len = 0;
	int num = 0;

	//for(int i=0;i<n;i++) {
	//	if (str[i] == '(') {
	//		s.push(i);
	//	}
	//	else {
	//		if (s.top() + 1 == i) {
	//			s.pop();//레이저 쌍은 pop을 해줘야함.
	//			num += s.size();
	//		}
	//		else {
	//			s.pop();//쇠막대기가 끝난 경우에도 pop을 해줘야함.
	//			num += 1;
	//		}
	//	}
	//}
	for (char ch:str) {
		if (ch == '(') {
			s.push(len);
			len++;
		}
		else {
			if (s.top() + 1 == len) {
				s.pop();//레이저 쌍은 pop을 해줘야함.
				num += s.size();
			}
			else {
				s.pop();//쇠막대기가 끝난 경우에도 pop을 해줘야함.
				num += 1;
			}
		}
	}
	cout << num << '\n';

}
