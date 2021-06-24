#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
add x:S에 x를 추가한다. x가 이미 있는경우 연산 무시.
remove x:x를 제거한다. x가 없는 경우 연산 무시.
check x:x가 있으면 1 없으면 0 출력
toggle x:x가 있으면 x를 제거, 없으면 추가.
all:s를 1~20까지 다 채운다.
empty:s를 공집합으로 만든다.
*/

/*
비트마스크를 이용하려는 이유: 정수 하나로 정수 배열을 표현하기위해서
ex) 570이란 수는 2진수들의 합으로 나타낼 수 있는데, 2^9 + 2^5 + 2^4 + 2^3 + 2^1로 나타낼 수 있음
그리고, 이 경우 이외에 2진수의 합으로 나타낼수 없기때문에 유일함.
이건 곧 a={9,5,4,3,1}로 생각 할 수 있기때문에, 정수 하나로 a배열을 표현 가능함.
->0~N-1까지 정수로 이루어진 집합을 나타낼때 사용.(1~N까지는 속도 공간 다 비효율적)

정수를 2진수처럼 다뤄서 배열처럼 쓰려면, 연산을 비트연산으로 사용해야함.
집합(정수값)이 S일때
i를 추가
=(s|(1<<i))
i를 검사
=(s&(1<<i))
i를 제거
=(s&~(1<<i))
i를 토글(0은 1로 1은 0으로->xor)
=(s^(1<<i))

이렇게 되는 이유
정수 x를 2진수처럼 다루는게 되기때문에
s랑 or(|)연산을 하면 s에 해당 수가 있든 말든 추가 가능.(해당 진수만 1로 만들고 or연산 하는거니까)
s랑 not and연산을 하면 s에 해당수가 있든 말든 제거 가능(해당 진수만 0으로 만들고 and연산 하는거니까)
s랑 and(&)연산을 하면 s에 해당 수가 있든 말든 검사 가능(해당 진수만 1로 만들고 and연산 하는거니까)
s랑 xor(^)연산을 하면 s에 해당 수가 있든 말든 0은 1로 1은 0으로 바꿀 수 있음.

*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int m;
	cin >> m;

	int s = 0;
	while (m--) {
		string str;
		cin >> str;

		
		//정수형 변수 하나로 배열을 나타낼 수 있다. -> 비트마스크의 장점.
		int x;
		/*
		문자 배열의 경우 비교함수가
		strcmp(문자배열,비교문자열)

		문자열의 경우 비교함수가
		str1.compare(비교문자열)
		*/
		
		if (!str.compare("add")) {
			//compare함수는 다른건 1이나 -1 같으면 0으로 반환하는데, c++에서 0은 false 나머지는 true니까
			//!(not)해줘야 해당 조건문에 걸릴수 있게 된다.
			cin >> x;
			//x--;
			s = (s | (1 << x));
			//s에 더해줄때 연산. s에 1을 x만큼 민 수(2^x)를 or(|)연산 해서 더 해준다.
		}
		else if (!str.compare("remove")) {
			cin >> x;
			//x--;
			s = (s & ~(1 << x));
			//s에 1<<x한 값을 뒤집은 값을 and연산 해줘서 해당 숫자(2^x)를 0으로 만든다.
		}
		else if (!str.compare("check")) {
			cin >> x;
			//x--;
			int res = (s & (1 << x));
			//res에 해당 숫자 (1<<x)가 들어있다면 0이 2^x가 출력될테니까, true로 나오고, 그러면 1
			//없으면 res가 0이 될테니까 0을 출력해준다.
			if (res) {
				puts("1");
			}
			else puts("0");
		}
		else if (!str.compare("toggle")) {
			cin >> x;
			//x--;
			s = (s ^ (1 << x));
			//toggle(xor)연산.
		}
		else if (!str.compare("all")) {
			s = (1 << 20) - 1;
			//범위 안 모든 수를 집합에 포함시키려는 연산.
			//(1<<n)-1하면 2진수의 모든 수가 1이되니까.
		}
		else if (!str.compare("empty")) {
			s = 0;
			//0으로 만들면 공집합 됨.
		}
	}
}
