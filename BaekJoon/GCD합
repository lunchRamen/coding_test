#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;

	else return gcd(b, a % b);
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	int arr[101];
	long long sum = 0;

	for (int i = 0; i < t; i++) {
		sum = 0;
		int n;
		cin >> n;
		for (int j= 0; j < n; j++) {
			cin >> arr[j];
		}
		for (int j = 0; j < n-1; j++) {
			for (int k = j+1; k < n; k++) {
				sum += gcd(arr[j],arr[k]);
			}
		}
		cout << sum << '\n';
	}

}
