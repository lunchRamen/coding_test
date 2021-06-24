#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cstring>

using namespace std;

vector<int> v[100001];
int parent[100001];
//해당 인덱스에 값이 부모노드 번호.
int check[100001];
//인덱스 방문했는지 체크
int depth[100001];
//
int dist[100001];

void bfs(int root) {
	depth[root] = 0;//루트의 깊이는 0
	check[root] = true;//루트 방문 체크
	queue<int> q;
	q.push(root);//root를 q에 넣고
	parent[root] = 0;//root의 부모는 0(없다)
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int y : v[x]) {//v[x]의 모든 변수에 대하여 y로 탐색.
			if (!check[y]) {//방문 안했으면
				depth[y] = depth[x] + 1;//v에 있는 노드들은 자식노드니까 깊이+1
				check[y] = true;//방문 체크
				parent[y] = x;//y의 부모는 x 체크
				q.push(y);// y를 q에 push
			}
			//숨바꼭질에서 시간 갱신할때가 depth[y]=depth[x]+1
			//역추적할때가 parent[y]=x와 동일함.
		}
		//이게 입력받을때 v[x] v[y]로 받았지만, root가 정해지고 root부터
		//타고 내려오고, 방문여부로 중복을 막았기때문에 부모노드가 정해질수 있따.
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	for (int i = 0; i < n-1; i++) {//트리에서 node의 갯수를 입력받으면, 간선의 갯수는 n-1개.
		int x, y;
		cin >> x >> y;
		v[x].push_back(y);
		v[y].push_back(x);
	}
	bfs(1);
	for (int i = 2; i <= n; i++) {
		cout << parent[i]<<'\n';
	}
}
