#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int m, n;
	cin >> m >> n;

	vector<int> prime(1000001);
	vector<bool> visit(1000001);

	visit[0] = visit[1] = true;
	//2부터 visit 검사를 하니까 0과 1은 방문한걸로 설정해줘야 오류가 안남.(근데 쓸 일이 있나)

	for (int i = 2; i <= n; i++) {
		for (int j = i + i; j <= n; j += i) {
			visit[j] = true;
		}
	}

	for (int i = m; i <= n; i++) {
		if (visit[i] == false) cout << i << '\n';
	}
}
