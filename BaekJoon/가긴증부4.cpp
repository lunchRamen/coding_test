#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

int a[1001];
int dp[1001];
int idx[1001];

/*
가장 긴 부분 수열 4
LIS문제에서
LIS의 길이 뿐만 아니라 LIS에 포함된 배열의 원소들도 같이 추적 하고 싶다?
역추적(backtracking)을 해줘야함.

역추적 하는법?
입력받은 배열의 인덱스를 저장해놓은 index array를 하나 더 만든다.
이 인덱스배열에는 해당 dp가 갱신됐을때, 그 인덱스를 넣어놓는다.
이렇게 하나만 넣어놔도, 처음으로 돌아갈때까지 계속 역추적을 하기때문에 괜찮음.

그리고 역추적을 출력해줄때는 재귀함수를 사용하면됨.
역추적이 끝났을때 return 조건문 하나 만들어주고 LIS를 이루는 원소들의 인덱스를 저장해둔
idx배열에서 LIS의 맨 마지막(마지막 최대길이 구하는거에서)원소의 idx를 pointer로 해서

go함수를 재귀로 돌리면(p==-1이 될때까지) LIS를 구성하는 a배열의 원소들이 다 출력된다

p=4 -> idx[4] = 2 -> idx[2]=1 -> idx[1]=-1. 끝.
*/
void go(int p) {
	if (p == -1) return;
	
	go(idx[p]);
	cout << a[p] << ' ';
	
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	for (int i = 0; i < n; i++) {
		dp[i] = 1;
		idx[i] = -1;
		for (int j = 0; j < i; j++) {
			if (a[i] > a[j] && dp[i] < dp[j] + 1) {
				dp[i] = dp[j] + 1;
				idx[i] = j;
				//해당 인덱스를 idx배열에 넣음.
			}
		}
	}

	int max = dp[0];
	int p = 0;

	for (int i = 0; i < n; i++) {
		if (max < dp[i]) {
			max = dp[i];
			p = i;
		}
	}
	//이렇게만 해줘도 되는게 LIS를 만드는 가장 마지막 인덱스를 p로 가지면
	//위에 반복문에서 idx배열에 dp를 갱신하는 원소의 인덱스를 넣어두었으니까
	//연쇄적으로 따라감.

	cout << max << '\n';
	go(p);
	cout << endl;


}
