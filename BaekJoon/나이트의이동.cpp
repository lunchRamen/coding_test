#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

/*
7562 나이트의 이동

나이트가 이동하는 경우의 수
가로 2칸 세로 1칸.
세로 2칸 가로 1칸.
*/

int dx[] = { 2,2,-2,-2,1,1,-1,-1 };
int dy[] = { 1,-1,1,-1,2,-2,2,-2 };
//나이트가 이동 가능한 모든 경로.
int a[300][300];
int d[300][300];

int startX, startY;
int endX, endY;
int n;

void bfs(int startX, int startY) {
	queue<pair<int, int>> q;
	q.push(make_pair(startX, startY));
	d[startX][startY] = 1;
	while (!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < n) {
				if (d[nx][ny] == 0) {
					d[nx][ny] = d[x][y] + 1;
					q.push(make_pair(nx, ny));
				}
			}
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	while (t--) {
		
		cin >> n;
		
		
		cin >> startX >> startY;
		
		cin >> endX >> endY;

		bfs(startX, startY);

		cout << d[endX][endY]-1 << endl;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				a[i][j] = 0;
				d[i][j] = 0;
			}
		}
	}
}
