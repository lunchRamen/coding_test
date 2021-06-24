#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
ABCDE

첫번째줄에 사람 수 N
친구 관계 수 M 주어짐.

둘째줄부터 M개의 줄에 정수 a와 b
a와 b가 친구라는 뜻.

a->b->c->d->e인 관계를 만족하는지 확인
있으면 1 아니면 0

인접행렬
인접리스트
간선리스트

세개로 다 구현해볼 예정.

a->b는 간선리스트로 구현.
edges(간선리스트)에 들어있는 pair의 first를 a
second를 b로 두고 2중 for문으로 전수조사 해보면
a와 b를 잇고있는 간선리스트가 전부 나옴.

c->d도 간선리스트로 구현.
모든 간선 순회.(a->b와 동일)

b->c 인접행렬로 연결되어있는지 확인.

한 정점과 연결되어있는 모든 간선을 찾음.
->인접리스트로 구현. 
*/

bool a[2000][2000];
//인접 행렬
vector<int> g[2000];
//인접 리스트
vector<pair<int, int>> edges;
//간선 리스트

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		int from, to;
		//어디서부터 어디로
		cin >> from >> to;
		edges.push_back({ from,to });
		edges.push_back({ to,from });
		//간선리스트에
		//방향성 없는 간선을 방향성 있게 저장.
		a[from][to] = a[to][from] = true;
		//인접행렬에 간선 저장
		g[from].push_back(to);
		g[to].push_back(from);
		//인접리스트에 간선 저장.

		//이렇게 각각의 경우에 간선을 저장하는 방법이 다름.
		//다만 방향성이 없는 경우,이렇게 양쪽으로 받아서 저장해줌.
		//벡터의 경우 이렇게 저장하면
		//g[0]=1
		//g[1]=0,2
		//g[2]=1,3
		//g[3]=2,4
		//g[4]=3 이렇게 저장됨. 가중치면 pair형태로 저장하면 될듯?
	}

	m *= 2;//방향이 있는걸로 계산했으니까 간선의 갯수가 2배가 됨.
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < m; j++) {
			//a->b를 가르키는 
			int A = edges[i].first;
			int b = edges[i].second;
			//c->d
			int c = edges[j].first;
			int d = edges[j].second;

			//a b c d의 사람들중 같은 사람이 있는지 검사. 같은 사람이면 pass
			if (A == b || A == c || A == d || b == c || b == d || c == d) continue;
			

			//b->c(인접 행렬로 사람 찾기.)
			//b와c의 간선이 있는경우 1 없는경우를 0으로 정의했으니까
			//a[b][c]가 1이면 true니까 false로 바뀌고 넘어가고
			//a[b][c]가 0이면 false니까 !a[b][c]로 true만들어주고 해당경우 건너뜀
			if (!a[b][c]) continue;

			 
			//d->e
			//인접리스트 g의 d점에 연결된 모든 e에 대해서
			//a b c d와 e가 같지 않다면 1 출력.
			for (int E : g[d]) {
				if (A == E || b == E || c == E || d == E) continue;
				cout << 1 << endl;
				return 0;
			}
		}
	}
	cout << 0 << endl;//아니면 0출력
	return 0;
}
