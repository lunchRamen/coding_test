#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
외판원 순회 문제
모든 순서를 만들고 그중에서 합이 가장 작은 값을 도출하면 된다.
->순열로 풀 수 있는 이유는 입력값이 매우 작기 때문에.
*/

int w[20][20];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	vector<int> d(n);
	//d에는 방문 순서를 넣음.
	//d[0]->...d[n-1]에서
	//0~n-1번째까지 가는 도시 번호를 저장해놓음
	//-> w[d[i]][d[i+1]]이면
	//i번째에서 i+1번째로 갈때 길이 있는지.(0이 아닌지)
	//확인하고 맞다면 값을 sum에 더하는 작업.

	//왜? w[i][j]를 i번째 도시에서 j번째 도시로 갈때 드는 비용이라고
	//정의하고 입력값을 받았으니까.
	//0이면 가는 길이 없다고 했으니까

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> w[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		d[i] = i;
	}

	int ans = 2147483647;

	do {
		bool ok = true;
		int sum = 0;
		
		//선행 시작을 0~n-1까지 0->1 1->2 ... n-2->n-1에서 0인 값이 있으면
		//ok를 false로 만들고 아니면 sum에 해당 값을 더한다.
		for (int i = 0; i < n - 1; i++) {
			if (w[d[i]][d[i + 1]] == 0) ok = false;
			else sum += w[d[i]][d[i + 1]];
		}
		//만약 ok가 true이고(모든 길이 있고) n-1에서 0으로 가는길이 0이 아니라면(있다면)
		//sum에 w[d[n-1]][d[0]]을 더해주고 ans보다 작다면 ans에 sum을 넣어줌.
		//그래서 ans을 정수범위 최대값으로 설정해둠.
		if (ok && w[d[n - 1]][d[0]] != 0) {
			sum += w[d[n - 1]][d[0]];
			if (ans > sum) ans = sum;
		}
	} while (next_permutation(d.begin(), d.end()));
	//이걸 d의 시작부터 끝까지.
	//이렇게 되면 d벡터에는 0~n-1의 값이 각 인덱스에 들어가 있는데
	//0~n-1부터 n-1~0이 될때까지 도는건데,
	//do의 for문에서는 어차피 for문이 0~n-1까지만 도니까
	//순열을 따지는게 상관이 없는게 아닌가?
	//예를 들어서 1->2->4->3->1이랑
	//			  1->3->4->2->1이랑
	//분명 다른 값을 가지고 있을텐데 for문은 어차피 0~n-1까지 도니까
	//w배열의 가중치를 따지는게 의미가 없지 않나요?

	cout << ans << endl;
}
