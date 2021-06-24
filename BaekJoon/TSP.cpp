#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
외판원 순회
traveling salesman problem(TSP)
완전탐색으로 푸는 대표적 문제.

n개의도시 입력
i번째 도시에서 1~n번째 도시로 가는데 가는 길이 있으면 그 길이. 없으면 0 입력.

어떤 도시든 그 도시부터 시작해서 다시 그 도시로 돌아오는데 필요한 최소값,
*/

int w[20][20];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) cin >> w[i][j];
	}

	//vector<vector<int>> v(n);

	//for (int i = 0; i < n; i++) {
	//	for (int j = 0; j < n; j++) {
	//		cin >> v[i][j];
	//	}
	//}
	vector<int> v(n);
	for (int i = 0; i < n; i++) v[i] = i;
	//벡터는 i번째 도시에서 어디로를 나타내주는 방향벡터로 씀.(=방문순서)
	//0~n-1번까지의 도시가 있고

	sort(v.begin(), v.end());

	int ans = 2147483647;//ans를 최대값으로 둬야 최소값을 구할수 있음.
	
	//while (next_permutation(v.begin(), v.end())) {
	//	int res = 0;
	//	for (int i = 0; i < n; i++) {
	//		for (int j = 0; j < n; j++) {
	//			res += v[i][j];
	//		}
	//	}
	//}

	do {//v[0]=0 ->v[1]=1 -> ... -> v[n-1]=n-1 -> v[0]=0 . 마지막엔 꼭 자기 자신으로 돌아와야함. 
		//여기서 0->1 1->2 2->3 .. n-2->n-1 n-1->0의 값들을 다 구하기 위해서
		bool ok = true;
		int sum = 0;
		for (int i = 0; i < n - 1; i++) {//이 for문을 써줌.
			if (w[v[i]][v[i + 1]] == 0) ok = false;//가는길이 없는게 아닌이상
			else sum += w[v[i]][v[i + 1]];//sum에 길에 값을 더해줌.
		}
		if (ok && w[v[n - 1]][v[0]] != 0) {//ok가 true이고(0~n-1번까지 가는 길이 다 있고) 마지막 n-1번째에서 0번째
										   //를 가는 값 또한 0이 아니라면
			sum += w[v[n - 1]][v[0]];//마지막으로 도하고
			if (ans > sum) ans = sum;//ans와 sum을 비교해서 sum이 더 작다면 sum을 ans에 집어넣는다.
		}
	} while (next_permutation(v.begin(), v.end()));//계속 다음을 구함.
	//어떻게 다음을 구하냐
	//1 2 3 4 1에 해당되는 값을 구하고선
	//1 2 4 3 1에 해당하는 값을 구하고
	//...해서 4 3 2 1 4에 해당되는 값까지 구하는 조건을 while(np(v.begin(),v.end())로 걸어놓음
	//이게 왜 1234~4321까지 커버해주는 조건인지는 잘 모르겠음.

	cout << ans << endl;
}
