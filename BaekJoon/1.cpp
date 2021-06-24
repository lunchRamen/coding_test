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
1로 이루어진 수 (1,11,111,1111,11111...) 중에서 나누어떨어지는 가장 작은 수 출력.
*/

int n;

int solve(int a) {
	int b = 1;
	int len = 1;

	for (int i = 0; i < n; i++) {
		b = b % a;
		if (b != 0) {
			b = b * 10 + 1;//b에는 이전 수를 나누는 나머지가 들어있다.
			len++;
		}
		if (b == 0) return len;
	}
	//while로 무한정 조건을 따지기 보단 for문으로 n번만큼만 따지면 정답이 무조건 나오기 때문에
	//for문을 써서 정답이 됐다.
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	
	while (cin >> n) {
		//cout << solve(n) << '\n';
		int num = 1;
		for (int i = 1;; i++) {
			num = num * 10 + 1;
			num %= n;
			if (num == 0) {
				cout << i << '\n';
				break;
			}
			//이렇게 for문의 조건식을 안써도 정답을 구하면 break문으로 빠져나오니까 이렇게 해도됨.
		}
	}
}
