#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, string> p1, pair<int, string> p2) {
	return p1.first < p2.first;
}

int main() {
	int n;
	cin >> n;

	vector<pair<int, string>> v(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i].first >> v[i].second;
	}
	//first는 나이순, second는 등록순.
	
	stable_sort(v.begin(), v.end(),compare);
	//stable하다->중복된 값들의 순서가 변하지 않으면 stable
	//->나이가 같으면 등록된 순서로 출력한다=stable을 유지하고 출력한다.

	for (int i = 0; i < n; i++) {
		cout << v[i].first <<" "<< v[i].second << "\n";
	}
}
