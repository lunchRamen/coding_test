#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
14501 퇴사
N+1일째 되는날 퇴사를 하기위해서
N일동안 최대한 많은 상담을 하려고함.

N일동안 매일마다 1명의 상담을 받을 수 있고
상담에 걸리는 시간과 비용을 입력받음.

그래서 비용이 최대가 되게끔 하는.

여기서 포인트는 N+1일에 걸치는 경우
상담을 할 수 없음.


*/

int a[16][2];

/*
solve에서 만들어야 할 것
1. 정답을 찾은 경우
2. 정답을 못찾은,못찾는 경우
3. 다음 재귀 호출문.
->상담을 한다 안한다로 하면 될듯.
*/

int ans = 0;

void solve(int a[16][2], int n,int day,int price) {
	if (day > n+1) return;//범위 넘은 경우(다음 날짜가 정해진 날짜 N보다 클때.)

	if (day == n+1) {//0번째날부터 시작한 day와 n이 같으면
		if (ans < price) ans = price;
		return;//price의 최댓값을 찾아서 출력해준다.
	}

	solve(a, n, day + a[day][0], price + a[day][1]);
	//for문을 이용해서 i번째날을 선택했을때
	//day는 
	solve(a, n, day + 1, price);
	//i번째 날을 선택 안했을때.

	//for문을 써서 i로 맞춰주지 않아도, i번째날 상담을 한다는게
	//다음 상담을 시작할수 있는날은 a[day][0], 해당 상담값은 a[day][1]이니까
	//이렇게 재귀해주면 됨.
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++) {
		for (int j = 0; j < 2; j++) {
			cin >> a[i][j];
		}
	}

	solve(a,n,1,0);
	cout << ans << endl;

}
