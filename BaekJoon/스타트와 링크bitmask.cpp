#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int s[20][20];
/*
스타트와 링크 by bitmask
짝수인 N을 입력으로 받음
N*N 배열을 입력받음
해당 배열의 값은 s[i][j]와 짝을 지었을때 능력치
i와 j가 짝을 지었으면
시너지값은 s[i][j]+s[j][i]임.

각각의 사람을 1번팀 2번팀으로 나눠서 풀수 있어서 비트마스크로 풀 수 있음.
0번팀=스타트팀
1번팀=링크팀 으로 놓고 풀면 됨.

*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> s[i][j];
		}
	}

	int ans = -1;

	for (int i = 0; i < (1 << n); i++) {//0~n-1까지의 사람들에 대한 전수조사.
		//근데 사람들의 팀 소속 여부를 bitmask로 정할거니까 2^n-1까지해서 2진수 bit에 저장 할 예정.
		//00000(모두 스타트팀에 속하는 경우)~11111(모두 링크팀에 속하는경우)까지
		
		//int cnt = 0;
		//for (int j = 0; j < n; j++) {
		//	if (i & (1 << j))cnt += 1;
		//}
		//if (cnt != n / 2) continue;
		//cnt로 먼저 for문을 돌려봐서 0과 1이 절반씩 있는 경우가 아니면 pass함.


		//실제로 첫번째팀과 두번째팀에 팀원을 나누는 코드(이때부터 1이 n/2개 0이 n/2개 있다)
		vector<int> first, second;
		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) first.push_back(j);
			//i번째 집합에 j가 포함되어있으면 1번팀에 아니면 2번팀에
			else second.push_back(j);
			//00000~11111를 도는 코드에서 각 이진숫자마다 0~n까지 j가 포함되어있으면 1번팀에 아니면 2번팀에
			//1:first팀 0:second팀.
		}
		if (first.size() != n / 2) continue;//반으로 나눠진 경우가 아니면 넘긴다.

		//여기서부턴 first팀과 second팀 절반씩 나눠진 경우
		int t1 = 0;
		int t2 = 0;
		for (int l1 = 0; l1 < n / 2; l1++) {//l1과 l2각각 n/2씩 for문을 돌려서
			for (int l2 = 0; l2 < n / 2; l2++) {
				if (l1 == l2) continue;//i==j인 경우는 패스
				
				t1 += s[first[l1]][first[l2]];//t1에 s[i][j]를 더해줄건데 i는 first벡터에 1번인 사람들이 다 들어가 있을건데
				//차례대로 넣을 예정. 1,2 1,3 1,4 이런식으로 first벡터에 들어있는 모든 팀원들의 순서쌍만큼 더해줌.
				t2 += s[second[l1]][second[l2]];//second도 똑같이.
			}
		}
		int diff = t1 - t2;
		if (diff < 0) diff = -diff;
		if (ans == -1 || ans > diff) ans = diff;
	}
	cout << ans << endl;

}
