#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

int n, m;

int a[1000][1000];
int d[1000][1000];

int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,1,-1 };

queue<pair<int, int>> q;

void bfs() {
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (a[nx][ny] == 0 && d[nx][ny] == -1) {
					d[nx][ny] = d[x][y]+1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> m >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
			d[i][j] = -1;

			if (a[i][j] == 1) {
				q.push(make_pair(i, j));
				d[i][j] = 0;
			}
		}
	}
	
	bfs();

	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		cout << d[i][j]<<' ';
	//	}
	//	cout << endl;
	//} d배열에 날짜는 잘 들어갔다.


	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			ans = max(ans, d[i][j]);
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] == 0 && d[i][j] == -1) {
				ans = -1;
			}
		}
	}
	
	cout << ans << endl;
	//int ans = 0;
	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		if (ans < d[i][j]) {
	//			ans = d[i][j];
	//		}
	//	}
	//}
	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < m; j++) {
	//		if (a[i][j] == 0 && d[i][j] == -1) {
	//			ans = -1;
	//		}
	//	}
	//}

	//cout << ans << endl;
}
