#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	vector<int> arr(1000001);
	vector<bool> visit(1000001);
	int pn = 0;

	visit[0] = visit[1] = true;

	for (int i = 2; i <= 1000000; i++) {
		if (visit[i] == false) {
			arr[pn++] = i;
			for (int j = i + i; j <= 1000000; j += i) {
				visit[j] = true;
			}
		}
	}
	/*
	앞에서 있던 에라스트테네스의 체에서 소수 구하는것과 다른점은
	단순히 해당 숫자 방문 여부로 소수를 따지는게 아니라
	해당 숫자가 두 소수의 합으로 결정 되는지를 보는거기 때문에 arr(prime)배열에 대한
	설정도 같이 해주어야 한다.
	*/

	while (1) {
		int n;
		cin >> n;
		if (n == 0) break;
		else {
			//int a, int b;
			for (int i = 1; i <= n;i++) {
				if (visit[n - arr[i]] == false) {//만약 해당 숫자가 소수라면
					cout << n << " = " << arr[i] << " + " << n - arr[i] << '\n';
					break;
				}
			}
		}
	}

}
