#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
6603 로또

49개의 수 중에서 6개를 고른다.

49개의 수 중에서 6개이상의 수 집합을 만들고
그 안에서 로또 번호를 뽑는게 전략중 하나.

갯수를 정하고, 번호를 정해야 한다.

k개의 수중에서 6개를 고른다? 순서와 상관x
선택과 관련된 문제.

순서를 이용해서 선택문제를 풀 수 있다.

입력받을 숫자배열과 선택할 선택배열 2개 배열을 만든다.

선택배열의 값이 1인 인덱스와 매칭되는 숫자배열만 출력한다.
이때 k의 값이 10이 넘어가면 시간초과가 뜨기때문에
선택배열의 중복에 대한 처리를 해줘야함.

이걸 순열 연산인 next_per perv_per에서 알아서 해줌.

근데 next대신에 prev를 쓴 이유?

*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int k = 1;

	while (k != 0) {
		cin >> k;

		vector<int> v(k);
		//vector<int> w(k);
		int w[12] = { 0 };
		for (int i = 0; i < k; i++) {
			cin >> v[i];
		}
		//뽑은걸 1 안뽑은걸 0으로 둬서 풀수 있다.
		//for (int i = 0; i < k - 6; i++) {
		//	w.push_back(0);
		//}
		for (int i = 0; i < 6; i++) {
			w[i] = 1;
		}
		
		do {
			for (int i = 0; i < k; i++) {
				if (w[i] == 1) cout << v[i]<<' ';
			}
			cout << '\n';
		} while (prev_permutation(w,w+k));
		//여기서 next가 아니라 prev를 쓴 이유
		//w배열에 1부터 넣었다.
		//그리고 순열은 오름차순부터 내림차순으로 진행된다.
		//근데 우리가 넣은건 1 6개, 0 6-k개.
		//이건 순서가 내림차순이다. 그것도 다 끝난 내림차순
		//고로 1을 순열처럼 돌리고 싶다면 prev로 돌려야한다.

		cout << '\n';

	}
}


