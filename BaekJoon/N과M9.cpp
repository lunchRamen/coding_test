#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

//중복되는 수를 입력으로 받음. 중복된 수들은 같은 수의 중복인 경우에만 출력 가능하고
//아니면 중복된 수를 한번만 출력하게끔.
//중복된 수는 걸러주면서, 자기 자신이 중복된 순서쌍일때만 출력해주는 변수를 하나 지정하는게 해결책.

int n, m;
int a[10];
int b[10];
bool c[10];

void solve(int cnt) {
	if (cnt == m) {
		for (int i = 0; i < m; i++) {
			cout << a[i] << ' ';
		}
		cout << '\n';
		return;
	}
	int check = 0;
	for (int i = 0; i < n; i++) {
		if (c[i] == true) continue;
		//check엔 출력배열인 a배열의 이전 원소가 들어가있으므로 현재 a[cnt]에 넣을 값이 a[cnt-1]이랑 겹치지 않으면
		//재귀를 진행.
		//7 9 에서 9 1 넘어갈때 괜찮은 이유는 7 9에서의 solve함수 자체가 끝났기때문.
		//9 1 9 7 9 9에선 sort로 정렬된 배열을 check로 탐색하는거라 인접한곳에 중복된 수가 있다는 점으로 확인하는거라
		//9는 고정으로 박혀있고 1 7 9를 인접배열로보고 탐색하는거라 출력됨.
		if (b[i] != check) {
			a[cnt] = b[i];
			check = a[cnt];
			c[i] = true;
			solve(cnt + 1);
			c[i] = false;
		}
	}
}

int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	sort(b, b + n);
	solve(0);
}
