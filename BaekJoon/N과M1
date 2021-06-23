#include <iostream>

using namespace std;

/*
N과 M(brute force) brute force는 재귀와 비슷.
범위가 10이내면 -> 제일 큰 팩토리얼이여도 1초 이내 연산 가능하니까
brute force로 풀수 있음
n은 1~n까지의 수
m은 그중 m개를 골라 출력(중복은 제외)


*/
int n, m;
int a[10];
bool c[10];

void solve(int cnt) {
	if (cnt == m) {
		for (int i = 0; i < m; i++) {
			cout << a[i] << ' ';
		}
		cout << '\n';//코테에선 endl말고 '\n'를 쓰는걸 습관들이자.
		return;
	}
	for (int i = 1; i <= n; i++) {
		if (c[i] == true) continue;//중복 제거
		c[i] = true;
		a[cnt] = i;
		solve(cnt + 1);
		c[i] = false;
	}	
}
//풀이 방법 parameter는 현재 숫자 갯수를 받고, 파라미터가 m이면 a배열 출력.
//아니면 for문으로 재귀 돌림. 재귀는 cnt==m이 될때까지 돌아감.(중복은 제외)
int main(void) {
	
	cin >> n >> m;

	solve(0);

}
