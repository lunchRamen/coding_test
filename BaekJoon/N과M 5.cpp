#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
N과 M 5.

기존의 N과 M과 다른 점: M개를 출력하는데 입력받는 N이 1~N이 아니라 직접 입력받음.
*/

int a[10];
int b[10];
int c[10];

void go(int idx, int n, int m) {
	if (idx == m) {
		for (int i = 0; i < m; i++) {
			cout << a[i] << ' ';
		}
		cout << "\n";
		return;
	}
	for (int i = 0; i < n; i++) {
		if (c[i]) continue;
		c[i] = true;
		a[idx] = b[i];
		//내가 틀렸던 점
		//출력할 배열인 a배열도 a[i]로 받았다는거. a[i]가 아니라 a[idx]로 받아서
		//a[idx]=b[0] b[1]..b[n-1]에 대해서 go함수의 재귀호출이 일어나도록 했어야 됐는데
		//a[i]로 똑같이 해버리면 a배열이 고정이 안되고 같은 주기로 돌아가서 제대로 출력 안됨.
		go(idx + 1, n, m);
		c[i] = false;
	}
	//중복 체크하는 코드 if(c[i]) continue; c[i]=true c[i]=false.
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> b[i];
	}
	sort(b, b + n);

	go(0, n, m);



}
