#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

/*
16947 서울 지하철 2호선

2호선은 51개의 역(정점)이 있고
양방향 간선이 51개인 그래프로 나타낼 수있다.

2호선은 순환선 1개 & 지선 2개.
순환선:다시 출발역으로 돌아 올 수 있는 노선
지선:순환선 역에서 시작하는 트리형태 노선(못돌아옴)

두 역 사이의 거리:간선의 개수.
A역과 순환선 사이의 거리: A와 순환선에 속하는 역 사이의 값중 최솟값.

1.순환선을 찾아야함.
2.순환선 이외의 정점에서 순환선까지 가는데 걸리는 거리 측정.

*/

/*
dfs+bfs로 구현해야함.


순환선의 조건: 3개이상의 정점을 dfs돌렸을때 cycle이 생기는 경우.
*/
//vector<int> v[3001];
//int check[3001];//0=방문안함 1=방문 2=사이클에 포함
//int cycle[3001];
//bool found;
//int n;
//
//void dfs(int start, int cur, int cnt) {
//	if (start == cur && cnt >= 2) {
//		cycle[cur] = true;
//		return;
//	}
//	check[cur] = true;
//	for (int i = 0; v[cur].size(); i++) {
//		int next = v[cur][i];
//		if (!check[next]) dfs(start, next, cnt + 1);
//		else if (start == next && cnt >= 2) dfs(start, next, cnt);
//
//		if (found) return;
//	}
//}
//
//int bfs(int start) {
//	queue<pair<int,int>> q;
//	bool visit2[3001] = { false };
//	q.push(make_pair(start, 0));
//	visit2[start] = true;
//	while (!q.empty()) {
//		int cur = q.front().first;
//		int cnt = q.front().second;
//		q.pop();
//		if (cycle[cur]) return cnt;
//		for (int i = 0; i < v[cur].size(); i++) {
//			int next = v[cur][i];
//			if (visit2[next]) continue;
//			q.push(make_pair(next, cnt + 1));
//			visit2[next] = true;
//		}
//	}
//}
//int main() {
//	
//	cin >> n;
//	for (int i = 0; i < n; i++) {
//		int x, y;
//		cin >> x >> y;
//		v[x].push_back(y);
//		v[y].push_back(x);
//	}
//	for (int i = 1; i <= n; i++) {
//		memset(check, false, sizeof(check));
//		dfs(i, i, 0);
//	}
//	for (int i = 1; i <= n; i++) {
//		if (cycle[i]) {
//			cout << 0 << ' ';
//			continue;
//		}
//		cout << bfs(i) << ' ';
//		//cycle이 아닌경우 거리 재는 bfs를 돌려서 출력
//	}
//	cout << endl;
//
//}

vector<int> v[3000];
int check[3000];//0:방문 x 1:방문 2:cycle.
int dist[3000];

int dfs(int x, int p) {
	//-2:사이클을 찾았고 x가  포함되지 않음
	//-1:사이클 못찾음
	//0~n-1:사이클 찾고 시작정점 인덱스 반환
	if (check[x] == 1) {
		return x;
	}
	check[x] = 1;
	for (int y : v[x]) {
		if (y == p) continue;
		int res = dfs(y, x);
		if (res == -2) return -2;
		if (res >= 0) {
			check[x] = 2;
			if (x == res) return -2;
			else return res;
		}
	}
	return -1;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x, y;
		cin >> x >> y;
		x--;
		y--;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	dfs(0, -1);
	queue<int> q;
	for (int i = 0; i < n; i++) {
		if (check[i] == 2) {
			dist[i] == 0;
			q.push(i);
		}
		else dist[i] = -1;
	}
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int y : v[x]) {
			if (dist[y] == -1) {
				q.push(y);
				dist[y] = dist[x] + 1;
			}
		}
	}
	for (int i = 0; i < n; i++) {
		cout << dist[i] << ' ';
	}
	cout << endl;
}
