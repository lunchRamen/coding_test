#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;
/*
16929 two dots
NxM인 게임판 위에서 진행.
각각의 칸은색이 칠해진 공이 하나씩 있음.
같은색으로 이루어진 사이클을 찾는 문제.

사이클:서로 다른 4개이상의 점이 인접해있고, 색이 같은 경우.

*/
char a[50][50];
int d[50][50];
int dist[50][50];

int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,1,-1 };

int n, m;

//dfs ver1
//x,y에 도착했고 nx,ny로 가려고 하고 다음 점에 색깔이 같으면 됨.
//이건 4개가 연속인경우. 4개가 사이클인 경우는 아님.
//예를들어 맨 오른쪽 2개, 맨 왼쪽 2개가 연속이여도 사이클을 갖진 않음.
//bool go(int x, int y, int cnt, char color) {
//	if (cnt == 4) return true;
//	for (int i = 0; i < 4; i++) {
//		int nx = x + dx[i];
//		int ny = y + dy[i];
//		if (0 <= nx && nx < n && 0 <= ny && ny < m) {
//			if (d[nx][ny] == 0 && a[nx][ny] == color) {
//				if (go(nx, ny, cnt + 1, color)) {
//					return true;
//				}
//			}
//		}
//	}
//	return false;
//}

//go ver2 x,y에 방문. 지금까지 방문한 점의 갯수가 cnt개.
//그래서 dist[x][y]에 cnt를 넣어줌.
//왜 첫번째 조건에서 return 값을 cnt-dist[x][y]>=4 로 뒀는가?
//d[x][y]는 이미 방문한 점인데?
//어떤 연속한 4개의 점이 있고, 그 점들이 같은 색일때
//0->1번째 점으로 갔는데 다시 0번째 점으로 돌아가도, cnt갯수가 올라감.
//왜냐면 코드를 4방향으로 가고, 같은 색이면 cnt+1로 다시 go문을 호출하니까.
//이걸 방지하기 위해서 cnt-dist[x][y]>=4조건을 쓴다.
bool go(int x, int y, int cnt, char color) {
	if (d[x][y]) return cnt - dist[x][y] >= 4;
	d[x][y] = true;
	dist[x][y] = cnt;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < n && 0 <= ny && ny < m) {
			if (a[nx][ny] == color) {
				if (go(nx, ny, cnt + 1, color)) return true;
			}
		}
	}
	return false;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);


	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}
	bool ans;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			ans = go(i, j, 0, a[i][j]);
			if (ans) {
				cout << "Yes" << endl;
				return 0;
			}
		}
	}
	
	cout << "No" << endl;
	return 0;
	
}
