#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cstring>

using namespace std;

/*
17425 약수의 합.
테스트 케이스 안에서 코드를 짠다.
*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//int t;
	//cin >> t;
	//while (t--) {
	//	int n;
	//	cin >> n;
	//
	//	int sum = 0;
	//	for (int i = 1; i <= n; i++) {
	//		sum += (n / i) * i;
	//	}
	//	cout << sum << '\n';
	//} 시간초과뜸.
	vector<long long>d(1000001, 1);
	//1백만까지의 수에 대한 약수의 합을 다 저장할거임.
	//테스트케이스가 많기때문에, 이 케이스마다 시간복잡도를 따져 계산하면 시간초과가 떠서.

	for (int i = 2; i <= 1000000; i++) {
		for (int j = 1; i * j <= 1000000; j++) {
			d[i * j] += i;
		}
	}//d[i]=f[i] O(nlogn)
	//->d의 인덱스에 해당되는 수의 약수를 다 구해서 저장.
	
	vector<long long> s(1000001);
	for (int i = 1; i <= 1000000; i++) {
		s[i] = s[i - 1] + d[i];
	}//s[i]=g[i] O(N)
	//s[1]~s[1000000]까지 모든단계에 더해감.
	//항상 전단계가 채워져있기때문에 가능.
	//->s의 인덱스에 해당되는 수까지의 범위의 각 숫자들의 약수의 합.

	//d를 모두 구하는 부분.

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		cout << s[n]<<'\n';
	}
	//입출력하는 부분. 
}
