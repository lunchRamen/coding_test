#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

//int arr[101];

bool primeNum(int a) {
	//루트 n으로 소수 검사.
	if (a < 2) return false;

	for (int i = 2; i * i <= a; i++) {
		//i*i=n이 되어야 하니까 <가 아니라 <=가 되어야함.
		if (a % i == 0) return false;
	}
	return true;

}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;

	int count = 0;

	vector<int> arr(t);

	for (int i = 0; i < t; i++) {
		cin >> arr[i];
	}

	for (int i = 0; i < t; i++) {
		bool m = primeNum(arr[i]);
		if (m == true) count++;
	}
	cout << count << '\n';
}
