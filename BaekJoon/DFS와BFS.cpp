#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

/*
dfs와 bfs
*/

bool check[1001] = { false };
vector<int> b[1001];

void dfs(int x) {
	check[x] = true;
	cout << x << ' ';
	for (int i = 0; i < b[x].size(); i++) {
		int y = b[x][i];
		if (check[y] == false) {
			dfs(y);
		}
	}
}
void bfs(int x) {
	queue<int> q;
	check[x] = true;
	q.push(x);
	
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		cout << x << ' ';
		for (int i = 0; i < b[x].size(); i++) {
			int y = b[x][i];
			if (check[y] == false) {
				check[y] = true;
				q.push(y);
			}
		}
	}
}
/*
dfs와 bfs의 출력문 위치가 다른이유
dfs든 bfs든 출력하는 기준-> 해당 점을 방문했을때
해당 점을 방문할때가 dfs는 chech[x]를 true해줬을때고, bfs는 queue를 pop시켰을때다. 그래서 위치가 다른거.
bfs의 경우 q를 pop시켜야 for문이 돌면서 다음 점을 queue에 넣고 방문했다고 표시를 해주니까
*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, m, v;
	cin >> n >> m >> v;

	
	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x>> y;

		b[x].push_back(y);
		b[y].push_back(x);
	}

	for (int i = 1; i <= n; i++) {
		sort(b[i].begin(), b[i].end());
	}
	//작은 정점부터 방문하기위해 sort해줌.
	//b배열의 index에 있는 벡터들을 다 sort해줌.

	dfs(v);
	for (int i = 0; i < 1001; i++) {
		check[i] = false;
	}
	cout << endl;
	bfs(v);

}
