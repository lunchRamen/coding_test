#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
11724 연결요소

*/
vector<int> n[1001];
bool check[1001];

void dfs(int x) {
	check[x] = true;
	for (int i = 0; i < n[x].size(); i++) {
		int y = n[x][i];
		if (check[y] == false) dfs(y);
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int v, e;
	cin >> v >> e;

	for (int i = 0; i < e; i++) {
		int x, y;
		cin >> x >> y;

		n[x].push_back(y);
		n[y].push_back(x);
	}

	int comp = 0;
	for (int i = 1; i <= v; i++) {
		//1~v까지 모든 정점에 대해서
		if (check[i] == false) {
			//i번째 정점을 방문 안했으면
			dfs(i);
			//dfs(i)돌리고
			comp += 1;
			//연결요소에 1을 더한다.
		}
	}
	//이게 왜 연결요소를 구하게 해주는가?
	//통상적으로 우린 연결그래프라고 가정하고
	//dfs(start)로 그냥 돌리는데 만약 연결요소가 2개 이상이라면
	//1~v까지 모든 점에대해 dfs로 임의의 정점 하나를 돌려보고
	//check[i]가 false인것에 대해 다시 돌려야 모든 정점을 순회하는거니까.

	cout << comp << endl;
}
