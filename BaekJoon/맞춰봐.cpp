#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
1248 맞춰봐

A배열: -10~10까지의 숫자(최대 10개)
S배열: s[i][j]형태 -> a[i]~a[j]까지의 합. 합이 0보다 크면 + 작으면 - 같으면 0.

보통같았으면 A배열이 주어지고 s배열을 구하는 문제일텐데, 이번 문제같은 경우엔
역으로 S배열을 주고, A배열이 뭔지 물어보는 문제.

a배열의 각 index에 들어 갈 수있는 경우의 수:21가지(-10~10)
최대 10개까지 들어갈수있으니까 21^10가지가 된다. 조온나 큼. 시간초과.

여기서 s[i][i]의 역할로 시간을 단축시켜서 문제를 풀 예정.
s[i][i]는 i번째 하나만 놓고 + - 0인지 판별하는거라 +면 양수 -면 음수 0이면 0인걸 알 수있다.

양수는 1~10 음수는 -10~-1 0은 0. 밑이 반으로 줄어듬.

10^10.이것도 크긴함.

ex)
a= 3 -2 -1 5

i/j 0 1 2 3(인덱스 번호)
0   + + 0 +
1   x - - +
2   x x - +
3   x x x +
왜 i와j가 같아지기 전까진 x로 나오는가?
->s[i][j]의 정의를 i부터 j까지 1씩 더한 합인데
j가 i보다 작으면 식이 성립을 안하니까.

a에서 s를 만드는건 쉬운데,
s에서 a를 구하는건 어렵다.

21개의 숫자를 10개의 자리에 넣을수 있음.

21^10이 총 경우의 수. 매우 큰 수.

여기서 시간복잡도를 줄이는 방법
i=j인 경우.
해당 숫자가 + 0 -인지 판별 가능.

근데 이것도 10^10이라 너무 오래걸림.
*/


//bool ok;
//int ans[11];
//
//bool go(int index) {
//	if (index == n) {
//		//index가 n이면 0~n-1까지 탐색을 완료했으니까
//		//ok(맞는지 아닌지 결과 호출)
//		return ok();
//	}
//	for (int i = -10; i <= 10; i++) {
//		ans[index] = i;
//		if (go(index + 1)) return true;
//	}
//	return false;
//}


/*
첫번째 시도: 그냥 -10~10까지 모든수를 10자리 수에 채워넣어서 맞는 경우 나올때까지 계산
->21^10이라 시간초과

두번째 시도: s[i][i]의 경우 해당 i번째 index숫자 하나만 더한 결과값이라 해당 수가 + 0 - 인지 판단 가능.
이 숫자로 해당 숫자가 1~10인지 0인지 -1~-10인지 판단 가능.
->그래도 10자리 숫자에 넣으면 10^10이라 시간초과.

세번째 시도:앞에 부등호 문제에서 했던 백트랙킹 개념을 가져옴.
0번 인덱스부터 해당 인덱스의 부호를 결정했으면, 1번째 부호도 결정을 하고, 두 수의 합의 부호를 통해서

*/
int n;
int sign[10][10];
int ans[10];

bool check(int index) {
	int sum = 0;//합은 0
	for (int i = index; i >= 0; i--) {//인덱스부터 0까지
		sum += ans[i];//합은 ans 값들의 합.
		if (sign[i][index] == 0) {//만약 i index가 0인데 합이 0이 아니면 false return
			if (sum != 0) return false;
		}
		else if (sign[i][index] < 0) {
			if (sum >= 0) return false;
		}
		else if (sign[i][index] > 0) {
			if (sum <= 0) return false;
		}
	}
	return true;
}

bool go(int index) {
	if (index == n) return true;
	//index가 n이면 0~n-1번째 index까지 재귀가 끝났단거니까 return true
	if (sign[index][index] == 0) {
		//index index번째가 0이면 index번째 수는 0인게 확정
		ans[index] = 0;//해당 인덱스의 정답을 0으로 표시
		return check(index) && go(index + 1);//index가 맞는지 체크하고, index+1번째로 재귀
	}
	for (int i = 1; i <= 10; i++) {//아닌경우는 1~10까지
		ans[index] = sign[index][index] * i;//해당 인덱스의 정답을 1*i한 후에
		if (check(index) && go(index + 1)) return true;//맞는지 체크하고, 재귀 돌렸을때 다 true라면
		//true를 return 아니면 false return
	}
	return false;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	
	cin >> n;
	string s;
	cin >> s;
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i; j < n; j++) {
			if (s[cnt] == '0') {
				sign[i][j] = 0;
			}
			else if (s[cnt] == '+') {
				sign[i][j] = 1;
			}
			else if (s[cnt] == '-') {
				sign[i][j] = -1;
			}
			cnt += 1;
		}
	}
	//해당 문자열에서 0이면 0 양수면 1 음수면 -1 넣어서 돌리려고 부호에 맞는 대표 수를 넣음.
	go(0);
	for (int i = 0; i < n; i++) {
		cout << ans[i] << ' ';
	}
	cout << '\n';
	return 0;
}
