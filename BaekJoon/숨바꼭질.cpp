#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

/*
1697 숨바꼭질
수빈이와 동생이 숨바꼭질
수빈이 위치 x 동생 위치 y
수빈이 이동방법: x-1 or x+1 or 2x.
몇초 뒤에 도달 가능한지.
*/
int x, y;
int visit[200001];
int dist[200001];

void bfs(int start) {
	queue<int> q;
	q.push(start);
	visit[start] = true;
	dist[start] = 0;
	while (!q.empty()) {
		int now = q.front();
		q.pop(); 
		if (now -1 > 0 ) {
			if (visit[now-1] == false) {
				q.push(now - 1);
				visit[now - 1] = true;
				dist[now - 1] = dist[now] + 1;
			}
			if (now + 1 < 200000) {
				if (visit[now + 1] == false) {
					q.push(now + 1);
					visit[now + 1] = true;
					dist[now + 1] = dist[now] + 1;
				}
			}
			if (now*2 < 200000) {
				if (visit[2 * now] == false) {
					q.push(now * 2);
					visit[now * 2] = true;
					dist[now * 2] = dist[now] + 1;
				}
			}
		}
		

	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	
	cin >> x >> y;

	bfs(x);
	cout << dist[y] << endl;
}
