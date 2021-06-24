#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
2529 부등호

k개만큼 부등호를 입력받는다.
k+1자리의 수에서
입력받은 부등호의 순서대로 수의 대소를
지키는 최대 , 최소 수를 구하는 문제.

**첫번째 자리수가 0인 경우도 인정.

brute force로 구해야함.
->정답을 찾은경우
  정답을 못 찾은 경우
  다음 재귀 호출.

정답을 찾은 경우:부등호의 조건을 다 만족한 수를 찾았을때
->이 경우 max와 min 두개 다 만들어둬서 비교후 저장해서 갱신하면 될 듯.

brute force로 풀어도 되지만
백트랙킹을 생각했다면 속도가 훨씬 더 빨라짐.
->백트랙킹은 문제마다 될수 있는지 아닌지 다르기때문에
문제를 보고 생각해봐서 구현해야함.
*/

int n;
char a[20];
vector<string> ans;
bool check[10];
bool ok(string num) {
	for (int i = 0; i < n; i++) {
		if (a[i] == '<') {
			if (num[i] > num[i + 1]) return false;
		}
		else if (a[i] == '>') {
			if (num[i] < num[i + 1]) return false;
		}
	}
	//string num에 대해 모든 인덱스를 검사할건데 a[i]가 <인데, num[i]가 num[i+1]보다 크다면
	//false >인데 num[i]가 num[i+1]보다 작아도 false. 아닌경우에만 true 반환.
	return true;
	//true 반환 했다-> num의 모든 자릿수에 대한 부등호와 숫자의 대소관계가 일치한다.
}
void go(int index, string num) {
	//index는 자릿수.
	//num은 각 자리 숫자를 문자열로 만들기위해 저장해두는 변수.
	if (index == n + 1) {
		//모든 자릿수 검사 한 경우
		if (ok(num)) {
			//정답이 맞는지 확인하고
			ans.push_back(num);
			//정답 벡터에 저장.
		}
		return;
	}
	for (int i = 0; i <= 9; i++) {
		//다음 재귀함수 호출할땐 0부터 9까지 항상 탐색.
		if (check[i]) continue;//i번째 수를 방문했다면 넘긴다.
		check[i] = true;//아니면 true로 바꾸고
		go(index + 1, num + to_string(i));//재귀를 돌린다.
		//다음 index에 대해 탐색하고, 문자열에는 i번째 '정수'를 문자열 형태로 전달할거니까
		//to_string(auto x)로 문자열 형태로 바꿔서 전달한다.
		check[i] = false;
		//위에 재귀가 끝났으면 방문여부를 다시 false로 바꾼다. 그래야 다음 재귀에 지장이 없음.
	}
}
//여기 함수들은 brute force로 구현.

bool good(char x, char y, char op) {
	if (op == '<') {
		if (x > y) return false;
	}
	if (op == '>') {
		if (x < y) return false;
	}
	return true;
}

void go(int index, string num) {
	if (index == n + 1) {
		ans.push_back(num);
		return;
	}
	for (int i = 0; i <= 9; i++) {
		if (check[i]) continue;
		if (index == 0 || good(num[index - 1], i + '0', a[index - 1])) {
			check[i] = true;
			go(index + 1, num + to_string(i));
			check[i] = false;
		}
	}
}
/*
위는 백트랙킹으로 구현. 매번 검사를 함. 다만 이렇게 다음 재귀의 조건으로 처리해주면
0부터 9까지 모든수에 대해 검사를 하는게 아니라, 부등호의 조건에 맞는 수만 num에 추가하고 검사하기때문에
속도가 훨씬 빨라진다.
good 함수 호출 횟수<<<<<<0~9까지에 대한 검사.
*/

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	//int k;
	//vector<char> v(k);
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	go(0, "");
	auto p = minmax_element(ans.begin(), ans.end());
	//여기에 최대값과 최솟값을 구해서 출력.
	cout << *p.second << endl;//최댓값이 second에 들어가있음.
	cout << *p.first << endl;//최솟값은 first에 들어가있음.

	/*
	auto 자료형: 어떤 함수로 인한 반환결과를 잘 모르겠을때 알아서 맞춰줌(심지어 벡터 배열 string이런경우도)
	min_element,max_element는 그냥 인자 하나만 전달 받아서 출력해줌. pair형태가 아님.
	minmax_element는 인자로 받는 iterator의 처음과 끝을 정해주면(꼭 begin,end일 필요 없음)
	처음부터 끝까지중 최솟값과 최댓값을 pair형태로 저장함. pair의 first에는 최솟값 second에는 최댓값 저장.
	그리고 해당 값들의 return이 포인터형태로 전달하기때문에, 출력할때도 자료형을 맞춰서 *를 붙여주는 것.
	*/
}
