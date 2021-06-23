#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <math.h>

using namespace std;

int gcd(int a, int b) {
	if (b == 0) return a;
	else return gcd(b, a % b);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int N, S;
	cin >> N >> S;

	int D = 0;

	vector<int> v(N);

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		if (S > x) v[i] = S - x;
		else v[i] = x - S;
	}//동생들 거리 입력 완료
	//수진이와 동생들 거리의 차로 갱신 완료.

	/*for (int i = 0; i < N-1; i++) {
		for (int j = i + 1; j < N; j++) {
			D = gcd(v[i], v[j]);
		}
	}*/
	//이렇게 2중 for문으로 짜면 입력 최대값때문에 시간초과뜸
	D = v[0];
	for (int i = 1; i < N; i++) {
		D = gcd(D, v[i]);
	}
	cout << D << '\n';


}
