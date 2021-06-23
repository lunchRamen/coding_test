#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int gcd(int a, int b) {
	//재귀형태
	if (b == 0) {
		return a;
	}
	else
		return gcd(b, a % b);
	//유클리드 호제법 자체가 gcd(a,b)=gcd(b,a%b).

	//반복문 형태
	/*while (b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;*/
}
int lcm(int a, int b) {
	int temp = gcd(a, b);
	return a * b / temp;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int a, b;
	cin >> a >> b;

	int c=gcd(a, b);
	int d =lcm(a, b);
	cout << c << '\n' << d << '\n';
}
