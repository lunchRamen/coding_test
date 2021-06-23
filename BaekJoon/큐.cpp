#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

struct Queue {
	int data[10000];//배열
	int begin, end;//시작 끝
	Queue() {
		begin = 0, end = 0;//초기화
	}
	void push(int num) {
		data[end] = num;//queue는 0(begin)~end-1까지라서 end번째 index=빈공간 그래서 end번째 index에.
		end++;//end 인덱스 1증가
	}
	bool empty() {
		if (begin == end)//시작과 끝이 같으면 비었다
			return true;
		else return false;
	}
	int size() {
		return end - begin;//인덱스끼리 뺀값=원소의 갯수
	}
	int front() {
		return data[begin];//맨 앞=begin
	}
	int back() {
		return data[end-1];//맨 뒤=end-1(index 체계 생각)
	}
	int pop() {
		if (empty()) {
			return -1;
		}
		begin++;
		return data[begin - 1];//pop을 시키는 조건=비었는지 먼저 확인
		//안비었으면 begin을 1증가 시키고 data[begin-1]을 return
		//FIFO(먼저 들어가고 먼저 나간다) 일방통행 도로라고 생각하면 됨.
	}

};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	Queue q;
	
	int n;
	cin >> n;

	for(int i=0;i<n;i++) {
		string cmd;
		cin >> cmd;
		if (cmd == "push") {
			int num;
			cin >> num;
			q.push(num);
		}
		else if (cmd == "pop") {
			if (q.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << q.front() << '\n';
				q.pop();
			}
		}
		else if (cmd == "size") {
			cout << q.size() << '\n';
		}
		else if (cmd == "empty") {
			cout << q.empty() << '\n';
		}
		else if (cmd == "front") {
			if (q.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << q.front() << '\n';
			}
		}
		else if (cmd == "back") {
			if (q.empty()) {
				cout << -1 << '\n';
			}
			else cout << q.back() << '\n';
		}
	}
	return 0;
}
