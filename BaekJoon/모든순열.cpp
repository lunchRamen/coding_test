#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;


/*
모든 순열

처음 순열부터 마지막순열까지 출력.
*/

bool next_permutation(int* a, int n) {
	int i = n - 1;
	while (i > 0 && a[i - 1] > a[i])i -= 1;
	if (i <= 0) return false;
	int j = n - 1;
	while (a[j] <= a[i - 1]) j -= 1;
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
	int* a = new int[n];//n칸짜리 배열 a생성.

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for (int i = 0; i < n; i++) cout << a[i] << ' ';
	cout << '\n';

	bool t = next_permutation(a, n);

	while (t) {
		for (int i = 0; i < n; i++) {
			cout << a[i] << ' ';
		}
		cout << '\n';
		t = next_permutation(a, n);
	}
}
