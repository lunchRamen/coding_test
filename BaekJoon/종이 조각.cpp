#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
14391 종이조각

최대 4x4정사각형에 각 칸에 숫자가 하나씩 들어가있음
그걸 1xn or mx1형태로 잘라서 숫자들의 총합이 최대로 되게끔 출력.

*/

int a[4][4];
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> a[i][j];
		}
	}
	
	/*
	각 칸을 가로로 합칠건지 세로로 합칠건지 결정
	*/

    int ans = 0;
    // 0: -, 1 : |
    for (int s = 0; s < (1 << (n * m)); s++) {
        int sum = 0;

        //가로가 얼마나 연속되는지 확인.
        //각 행마다 가로가 연속되는지 확인해줘야함.
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = 0; j < m; j++) {
                int k = i * m + j;
                if ((s & (1 << k)) == 0) {
                    cur = cur * 10 + a[i][j];
                }
                else {
                    sum += cur;
                    cur = 0;
                }
            }
            sum += cur;
        }


        for (int j = 0; j < m; j++) {
            int cur = 0;
            for (int i = 0; i < n; i++) {
                int k = i * m + j;
                if ((s & (1 << k)) != 0) {
                    cur = cur * 10 + a[i][j];
                }
                else {
                    sum += cur;
                    cur = 0;
                }
            }
            sum += cur;
        }
        ans = max(ans, sum);
    }
    cout << ans << '\n';
}
