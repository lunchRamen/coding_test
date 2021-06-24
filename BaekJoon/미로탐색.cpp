#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

int n, m;

int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };

int a[100][100];
int d[100][100];

void bfs(int x, int y) {
	queue<pair<int, int>> q;
	d[x][y] = 1;
	q.push(make_pair(x, y));
	while (!q.empty()) {
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (a[nx][ny] == 1 && d[nx][ny] == 0) {
					q.push(make_pair(nx, ny));
					d[nx][ny] = d[x][y] + 1;
				}
			}
		}
	}
}
int main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	
	
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &a[i][j]);
		}
	}

	bfs(0, 0);

	cout << d[n - 1][m - 1] << endl;
}
