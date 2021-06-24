#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
수 이어쓰기 1

1~N까지의 수를 이어서 쓰면
ex) 1~10까지의 수 이어서 쓰기
12345678910 ->11자리가 나온다.

N이 1억까지니까 O(N)이면 1초내에 가능해서 brute force를 사용.
*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	long long num = 0;
	//for (int i = 1; i <= n; i++) {
	//	if (i <= 9) num+=1;
	//	if (i>=10 && i <= 99) num += 2;
	//	if (i>=100 && i <= 999) num += 3;
	//	if (i>=1000 && i <= 9999) num += 4;
	//	if (i>=10000 && i <= 99999) num += 5;
	//	if (i>=100000 && i <= 999999) num += 6;
	//	if (i>=1000000 && i <= 9999999) num += 7;
	//	if (i>10000000 && i <= 99999999) num += 8;
	//}

	/*while (1) {
		if (n > 9) num += 9;
		else if (n >=1 && n <= 9) {
			for (int i = 1; i <= n; i++) {
				num += 1;
				break;
			}
		}
		if (n > 99) num += 180;
		else if (n >= 10 && n <= 99) {
			for (int i = 10; i <= n; i++)  {
				num += 2;
				break;
			}
		}
		if (n > 999) num += 2700;
		else if (n >= 100 && n <= 999) {
			for (int i = 100; i <= n; i++) {
				num += 3;
				break;
			}
		}
		if (n > 9999) num += 36000;
		else if (n >= 1000 && n <= 9999) {
			for (int i = 1000; i <= n; i++) {
				num += 4;
				break;
			}
		}
		if (n > 99999) num += 450000;
		else if (n >= 10000 && n <= 99999) {
			for (int i = 10000; i <= n; i++) {
				num += 5;
				break;
			}
		}
		if (n > 999999) num += 5400000;
		else if (n >= 100000 && n <= 999999) {
			for (int i = 100000; i <= n; i++) {
				num += 6;
				break;
			}
		}
		if (n > 9999999) num += 63000000;
		else if (n >= 1000000 && n <= 9999999) {
			for (int i = 1000000; i <= n; i++) {
				num += 7;
				break;
			}
		}
		if (n >= 10000000 && n <= 99999999) {
			for (int i = 10000000; i <= n; i++) {
				num += 8;
				break;
			}
		}
	}*/

	for (int start = 1, len = 1; start <= n; start *= 10, len++) {
		int end = start * 10 - 1;//해당 자릿수의 끝
		if (end > n) {
			end = n;//n이 해당 자릿수 안에 포함된다는걸 이렇게 표현.
		}
		num = num + (long long)(end - start + 1) * len;
	}
	//위처럼 for문을 만들면 for문이 한번 돌때마다 10씩 곱해지기때문에
	//연산횟수 많이 줄어들고 len로 자릿수를 1씩 증가시키기 때문에
	//해당 자릿수의 끝-시작+1 *해당자릿수의 길이를 정답에 더하면 정답이 나옴.


	cout << num << endl;

}
