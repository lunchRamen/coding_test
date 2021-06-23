#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
입력받은 수를 팩토리얼 시켰을때 0의 갯수
->중요점: 10의 지수승마다 0이 하나씩 생김.
10의 지수승을 만드는 조건: 2와 5의 조합.
2'만'으로 구성된 수=2의 1승 2의 2승 ... n보다 작은 2의 k승. 을 n으로 나눈 값.
5'만'으로 구성된 수=5의 1승...n보다 작은 5의k승.을 n으로 나눈값.

5를 센 값이 당연히 더 작을테니, 5를 출력하면 끝.
*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int fiveCount = 0;
	int n;
	cin >> n;
	for (int i = 5; i <= n; i *= 5) {
		fiveCount += n / i;
	}
	cout << fiveCount << '\n';
}
