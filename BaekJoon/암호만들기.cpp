#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
암호 만들기 재귀버전

L개의 알파벳으로 이루어진 단어 출력.
C개만큼 입력받은 알파벳들의 조합으로.
단어가 되는 조건
1개 이상의 a e i o u 모음
2개 이상의 자음.
이 조건을 코드로 표현하는게 중요함.

암호는 오름차순으로 정렬된 상태.

go(n,alpha,password,i)
n:만들어야하는 암호 길이
alpha:사용 할 수 있는 알파벳
password:현재까지 만든 암호
i:사용할지 말지 결정하는 인덱스

1.정답을 찾은 경우
password==n.
최소 한개의 모음과 2개의 자음에 대한 예외처리는 이따가 할 예정.

2.정답을 못찾은 경우.
문제의 조건 위배, 재귀함수로 구현 불가능.
인덱스(i)가 alpha의 크기까지 커질때.

3.다음 경우 재귀호출
i번째를 사용-> go(n,alpha,password+alpha[i],i+1)
사용x-> go(n,alpha,password,i+1).

시간복잡도: 2^n.

*/

bool check(string& password) {
	int ja = 0;
	int mo = 0;
	for (char x : password) {//for each형.
		//임시변수 x가 password를 다 순회한다.
		//순회할 배열과 형을 맞춰준 임시변수를
		//int x:arr 이런 형태로 맞춰주면 된다.
		if (x == 'a' || x == 'e' || x == 'o' || x == 'i' || x == 'u') {
			mo += 1;
		}
		else ja += 1;
	}
	if (ja >= 2 && mo >= 1) return true;
	else return false;
}

void solve(int l, vector<char>& alpha, string password, int i) {
	if (password.length() == l) {
		if (check(password)) {
			cout << password << '\n';
		}
		return;
	}
	//정답을 찾은 경우
	//이게 먼저 와야함. 왜냐?
	if (i == alpha.size()) return;
	//찾지 못한 경우.에서
	//l길이짜리 단어를 출력할때 마지막 알파벳을
	//포함 한 경우를 출력 못해줌.
	solve(l, alpha, password + alpha[i], i + 1);//vector에 저장된 i번째 알파벳을 포함하고 재귀호출
	solve(l, alpha, password, i + 1);//포함 안하고 재귀호출.
	/*
	solve(length,알파벳저장벡터,출력할문자열,벡터인덱스)로 해서
	출력할 문자열이 length와 같으면 자음은 2개 모음은 1개 이상인지 확인 한 후 문자열 출력. reutrn.
	인덱스가 알파벳저장벡터까지 도달한 경우도 return.끝까지 탐색했다는 의미니까.
	그 이외에는 재귀호출로 위에 두 경우를 만족할때까지 다음 함수를 호출해줘야함.
	->a t c i s w를 입력받았으면
	a c i s t w로 정렬되고
	
	여기서부터 solve함수가 시작.
	solve(4,alpha,password,i)
	->a를 o x
	->c를 o x
	->i를 o x
	->s를 o x
	여기서부터
	출력할 문자열의 길이가 4와 같고, check로 모음 1개 자음 2개이상이면 password를 출력하고 return.
	
	*/
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int l, c;
	cin >> l >> c;

	vector<char> alpha(c);
	string s;
	for (int i = 0; i < c; i++) {
		cin >> alpha[i];
	}
	sort(alpha.begin(), alpha.end());

	solve(l, alpha, s, 0);
}
