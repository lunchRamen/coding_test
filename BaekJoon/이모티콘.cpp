#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>

using namespace std;

/*
14226 이모티콘

이모티콘 S개를 보낸다.

1개의 이모티콘은 이미 입력.
2~S개의 이모티콘은
1.이모티콘을 모두 복사하거나
2.클립보드에 있는 모든 이모티콘을 붙여넣기하거나
3.화면에 있는 이모티콘 중 하나를 삭제하거나
의 연산으로 진행.
모든 연산은 1초 걸림.

숨바꼭질이랑 다른점.
+-1이 아니라 -1 경우만 있고
복사의경우 해당 수*2로 이뤄짐.

1.복사.
->x*2가 클립보드에 복사됨.
2.붙여넣기
->2*x가 화면에 붙여넣어지고 클립보드는 비어있음.


내가 잘못 구현한 점
화면의 이모티콘///클립보드의 이모티콘으로 분리해서 생각해내는거까진 맞았는데,
클립보드를 화면에 복사한다고 클립보드가 0이 되는게 아니다!
->화면 이모티콘을 정점으로 봤을때, 정점 하나로 여러가지의 상태가 나와서
  경우를 나눠줘야한다.
해당 인자 2개를 1차원 배열로는 구현하기 힘들고, 2차원 배열로 구현해야하며
d[a][b]에서 a:화면 b:클립보드로 두고, 화면과 클립보드의 상태를 두개로 분리해서 봐야한다. 이 두가지
상태가 같지 않은 경우에만 bfs를 진행해줘야함.


우리가 bfs에서 주로 쓰는
check:해당 정점 방문여부
dist:방문했을때 거리,시간이 몇이냐.

이걸 합쳐서 dist로 만들수 o.
어떻게?
-1:방문하지 않음
<=0:방문함(그 값이 곧 거리,시간)
*/
int s;
int d[1001][1001];

//queue에 들어가는걸 
//pair로 짜서 현재 화면이모티콘 갯수를 first
//클립보드에 있는 이모티콘 갯수를 second로 둡시다.
//void bfs(int start,int clipBoard) {
//	queue<pair<int, int>> q;
//	//현재 화면이모티콘 1 클립보드 0
//	q.push(make_pair(start, clipBoard));
//	check[start] = true;
//	cnt[start] = 0;
//
//	while (!q.empty()) {
//		int x = q.front().first;
//		int y = q.front().second;
//		//복사
//		if (x * 2 < 2000) {
//			if (x == y) continue;
//			q.push(make_pair(x, x));
//			cnt[x] = cnt[x] + 1;
//		}
//		//붙여넣기
//		if (x * 2 < 2000) {
//			if (check[x+y] == false) {
//				q.push(make_pair(x + y, y));
//				check[x + y] == true;
//				cnt[x + y] = cnt[x] + 1;
//			}
//		}
//		//-1
//		if (x - 1 > 0) {
//			if (check[x - 1] == false) {
//				q.push(make_pair(x-1,y));
//				check[x - 1] = true;
//				cnt[x - 1] = cnt[x] + 1;
//			}
//		}
//	}
//}
void bfs(int start, int clipboard) {
	
	queue<pair<int, int>> q;
	q.push(make_pair(1, 0));
	d[1][0] = 0;
	//화면에 이모티콘 1개,클립보드 0.
	while (!q.empty()) {
		int x, y;
		x = q.front().first;
		y = q.front().second;
		q.pop();
		//복사
		if (d[x][x] == -1) {//화면에 x개 클립에 x개인 상태가 없었으면
			d[x][x] = d[x][y] + 1;
			q.push(make_pair(x, x));
		}
		//붙여넣기
		if (x + y <= s && d[x + y][y] == -1) {//화면에 x+y개 클립에 y개인 상태가 없었으면
			d[x + y][y] = d[x][y] + 1;
			q.push(make_pair(x + y, y));
		}
		//-1
		if (x - 1 >= 0 && d[x - 1][y] == -1) {//화면에 x-1개 클립에 y인 상태가 없었으면
			d[x - 1][y] = d[x][y] + 1;
			q.push(make_pair(x - 1, y));
		}
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	
	cin >> s;
	memset(d, -1, sizeof(d));
	bfs(1,0);

	//ans를 반복문 돌려서 찾는 이유
	//정답이 이모티콘이 s개일때의 최소값인데, 클립보드의 이모티콘이 몇개일때 최소값인지 몰라서
	//d[s][0~s]를 탐색해서 찾아준다.
	int ans = -1;
	for (int i = 0; i <= s; i++) {
		if (d[s][i] != -1) {
			if (ans - 1 || ans > d[s][i]) {
				ans = d[s][i];
			}
		}
	}
	cout << ans-1 << endl;
}
