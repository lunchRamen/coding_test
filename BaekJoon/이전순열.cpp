#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
이전 순열

다음순열(10972)문제에서 부등호만 다 바꿔주면 됨.
->입력받은 a배열 관련 부등호만 바꿔주면 됨. a배열 말고는 원래 부등호 유지.
  대소비교의 방향만 반대로 해주면 돼서 그럼.
*/

bool prev_permutation(int* a, int n) {
	int i = n - 1;
	while (i > 0 && a[i - 1] <= a[i]) i -= 1;
	//i>0은 그대로 a[i-1]>=a[i](내림차순 검사)에서
	//a[i-1]<=a[i](오름차순) 검사로 바꿈.
	if (i <= 0) return false;//그대로
	int j = n - 1;
	while (a[j] >= a[i - 1]) j -= 1;
	//a[j]<=a[i-1]에서 a[j]>=a[i-1]로 바꿈.
	//오름차순의 경우 작은거중에 큰거를 골라야돼서
	//a[j]가 작은경우에 j를 왼쪽으로 이동시켰는데
	swap(a[i - 1], a[j]);
	j = n - 1;
	while (i < j) {
		swap(a[i], a[j]);
		i += 1;
		j -= 1;
	}
	return true;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	int* a = new int[n];
	for (int i = 0; i < n; i++) cin >> a[i];

	bool t = prev_permutation(a, n);

	if (t) {
		for (int i = 0; i < n; i++) cout << a[i] << ' ';
	}
	else cout << -1;
	cout << '\n';
}
