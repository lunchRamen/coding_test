#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
/*
스택 만들기.(포인터를 안쓰고 만들기)

스택의 주요기능
push pop top

empty,full -> 위에 기능을 이용하기위한 제한 조건들.
*/
struct Stack {
	int data[10000];
	int size;
	Stack() {//생성자로 초기화
		size = 0;
	}
	void push(int num) {//push는 data배열의 top에 넣는다. 인덱스체계라 size+1이 아니라 size다.
		data[size] = num;
		size++;
	}
	bool empty() {//empty는 비었으면 true 안비었으면 false. 비었는지 확인은 index(size)가 0에 있는지.
		if (size == 0) {
			return true;
		}
		else
			return false;
	}
	int pop() {//pop은 비었는지 확인. 비었으면 -1(0번 바로 밑) return
		if (empty()) {
			return -1;
		}
		else {//있는경우 size를 -1 data[size]를 return -> size를 -1 시키면 한칸 밑에를 가르키는데
			  //index체계는 -1로 생각해야되니까 data[size]를 return하면 맨 윗칸이 반환됨.
			size--;
			return data[size];
		}
	}
	int top() {
		if (empty()) {
			return -1;
		}
		else
			return data[size - 1];//이게 위에 pop은 size--후 data[size]고 여기선 data[size-1]을 하는 이유.
	}
};
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n;
	cin >> n;

	Stack s;

	while (n--) {
		string cmd;
		cin >> cmd;
		if (cmd == "push") {
			int num;
			cin >> num;
			s.push(num);
		}
		else if (cmd == "top") {
			cout << (s.empty() ? -1 : s.top()) << "\n";
			//3항 연산자로 empty가 true인지 -> 비어있는지 -> 비어있으면 -1 아니면 top반환.
		}
		else if (cmd == "size")
			cout << s.size << "\n";
		else if (cmd == "empty")
			cout << s.empty() << "\n";
		else if (cmd == "pop") {
			cout << (s.empty() ? -1 : s.top()) << "\n";
			if (!s.empty()) {
				s.pop();
			}
		}
	}
}
