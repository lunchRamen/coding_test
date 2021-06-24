#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cstring>
#define left _left
#define right _right

using namespace std;

/*
트리의 높이와 너비
1.같은 레벨에 있는 노드는 같은행
2.한 열에는 한 노드만
3.임의의 노드 왼쪽 subtree 노드들은 해당 노드보다 왼쪽열에
오른쪽 subtree는 오른쪽 열에 위치.
4.노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 비어있는 열이 없도록.

각각의 정점이 몇행 몇열에 있을지 추측 가능.

행:높이 열:인오더 방문 순서.(부왼오)


*/

struct Node {
	int left, right;
	int order, depth;
};
Node a[10001];
int left[10001];
int right[10001];
int cnt[10001];
int order = 0;

void inorder(int node, int depth) {
	if (node == -1) return;
	inorder(a[node].left, depth + 1);
	//왼쪽 자식 subtree 호출. depth+1해서
	a[node].order = ++order;
	//순서는 전역변수로 ++해준다.
	a[node].depth = depth;
	//subtree로 연결된 경우 깊이 갱신.
	inorder(a[node].right, depth + 1);
	//오른쪽 자식 subtree호출. depth+1
}//인오더:왼부오

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x, y, z;
		cin >> x >> y >> z;
		a[x].left = y;
		a[x].right = z;
		//인오더 방식:왼부오
		//x:노드 번호(부모) y:x의 왼쪽 자식노드(왼) z:x의 오른쪽 자식노드(오)
		//자식이 없으면 -1로 입력을 받는다.
		if (y != -1) cnt[y] += 1;
		if (z != -1) cnt[z] += 1;
		//우리가 손으로 풀었던 트리문제는
		//편하게 root=1로 뒀지만 root는 아무변수나 다 된다.
		//root의 특징:부모가 없다.
		//->위에 두개 if문: y,z의 값이 -1이 아니면?  해당 수에 1씩을 더해줘서 자식임을 표시.
	}
	int root = 0;
	for (int i = 1; i <= n; i++) {
		if (cnt[i] == 0) root = i;
	}//cnt[i]==0 ->부모를 세어봤는데 없으면? 그게 root니까 root=i.
	//->node번호가 순서대로 root부터 들어가는게 아니기때문에 위에처럼 따져준거.
	inorder(root, 1);
	//inorder시작(root의 값과, depth(root=1) 로 시작.)
	int maxdepth = 0;
	for (int i = 1; i <= n; i++) {
		//각 깊이마다 제일 왼쪽에 있는 노드와 오른쪽에 있는 노드를 구하고
		//최대 깊이를 구한다음에 정답의 최대값 구하기.
		int depth = a[i].depth;
		int order = a[i].order;
		if (left[depth] == 0) {
			left[depth] = order;
		}
		else {
			left[depth] = min(left[depth], order);
		}
		right[depth] = max(right[depth], order);
		maxdepth = max(maxdepth, depth);
	}
	int ans = 0;
	int ans_level = 0;
	for (int i = 1; i <= maxdepth; i++) {
		if (ans < right[i] - left[i] + 1) {
			ans = right[i] - left[i] + 1;
			ans_level = i;
		}
	}
	cout << ans_level << ' ' << ans << endl;
}
