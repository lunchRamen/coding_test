#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
오큰수
해당 배열의 원소에 오른쪽에 있으면서 크면서 가장 왼쪽에 있는 수.

->정답은 주어진 배열 안에서만 발생된다.
->각각의 배열의 원소에 대해서 해당 원소가 오큰수가 되게하는
원소들을 찾는걸로 생각을 바꿈(역방향)

해당 원소가 오큰수다
->그 전까지 원소들에선 해당 원소보다 큰 값이 없었다.

스택에는 값을 push하는게 아니라 index를 넣는다.

오큰수 자체가 해당 원소보다 크면서 가장 가까운수
->배열의 원소를 배열의 stack값(=index)로 놓고
만약 arr[s.top()]<arr[i]라면
오큰수 조건을 만족하니까 ans벡터에 넣는다.
stack의 top을 인덱스로 해서 넣으면, 순서대로 넣어진다.

*/
//int arr[1000001] = { 0 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	vector<int> arr(n);
	//입력받은 수열
	vector<int> ans(n);
	//정답출력(들어갈 값은 수열의 값 or -1)

	//배열로 안두고 벡터로 둠
	//100만개 배열을 디폴트로
	//지정해두는게 부담되서 그런건가
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	stack<int> s;
	s.push(0);
	for (int i = 1; i < n; i++) {
		//벡터도 배열처럼 index체계라 -1 생각.(n포함X)
		//for문을 돌때 오큰수가 아니다?
		//stack에 넣는다.
		if (s.empty()) {
			s.push(i);
		}
		while (!s.empty() && arr[s.top()] < arr[i]) {
			ans[s.top()] = arr[i];
			s.pop();
		}//stack에서 for문의 arr[i]가 클때까지
		//정답배열에 해당 값을 오큰수로 추가하고
		//stack을 pop시킨다.
		s.push(i);
	}
	while(!s.empty()) {//위에 for문 돌면서 스택에 값이 남아있다?
		//해당 인덱스를 가진 수열은 오큰수가 없다.
		ans[s.top()] = -1;
		s.pop();
	}
	for (int i = 0; i < n; i++) {
		cout << ans[i] << '\n';
	}
	cout << '\n';

	return 0;
}
