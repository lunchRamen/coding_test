#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
차이를 최대로.
입력받은 수들의 차이의 절대값들의 합이 최대가 되게끔 하는 최대값을 출력.

->정렬하고 순열로 다 돌려서 각각 계산하고 max로 출력해도 정답이 나올만큼 입력수가 작음.
*/
int n;

int calculate(int* a) {
	int res = 0;
	for (int i = 1; i < n; i++) {
		res += abs(a[i-1]-a[i]);
	}
	return res;
}
bool next_permutation(int* a, int n) {
	int i = n - 1;
	while (i > 0 && a[i - 1] > a[i]) i -= 1;
	if (i <= 0) return false;
	int j = n - 1;
	//while (a[i - 1] <= a[j]) j -= 1;
	while (a[i - 1] >= a[j]) j -= 1;
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

	n = 0;
	cin >> n;

	int* a = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	sort(a, a + n);

	int ans = 0;
	bool t = next_permutation(a, n);
	do {
		int temp = calculate(a);
		ans = max(ans, temp);
		t = next_permutation(a, n);
	} while (t);

	cout << ans << endl;

}
