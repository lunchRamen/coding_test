#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
사탕 게임

인접한 두칸을 고르는 방법의 갯수
->2* n^2가지.
첫번째칸부터 오른쪽 아래만 검사해줘도 전수조사와 같은 효과.


같은색으로 이루어진 행or열 고르기.
연속되는지 보려면->n^2.(행) 열도 n^2 -> 2*n^2.

->인접한 두칸 고르기 * 행 열 고르기 -> n^4.

최댓값: 50^4->그렇게 큰값이 아니라 그냥 코드때림.

근데, 시간복잡도를 줄일수 있는 방법이 존재하긴 함.
일단 swap을 안해준 상태의 a의 인접한 사탕의 최대갯수를 구하고,
하나씩 swap해서 구할때, 하나를 교환했으면 정답이 변할수 있는 곳들은
swap한 두개를 포함한 행 1개. swap한 사탕 중 하나를 포함한 열 1개. 또 다른 열 1개.
총 3줄의 ans값이 변할 수 있다.
->1행은 1열 2열 2행은 3열 4열 3행은 5열 6열...해서 검사하는 갯수를 n^2에서 3n으로 줄일수 있다.
*/

char a[51][51];

//check함수는 
//int check(vector<string> &a){
int check(char(&a)[51][51]) {
	//레퍼런스 타입으로 받아서 복사 안해도 됨. 같은 메모리 공유.
	//다만 check으로 a를 변형시켜주면, main의 vector a도 변형된다.
	//int n = a.size();
	int n = 51;
	int ans = 1;
	for (int i = 0; i < n; i++) {
		int cnt = 1;
		for (int j = 1; j < n; j++) {
			if (a[i][j] == a[i][j - 1]) {//오른쪽과 같은지(같은 행에 대해서)
				cnt += 1;//같다면 세주고
			}
			else {
				cnt = 1;//아니면 1로 초기화.
			}
			if (ans < cnt) ans = cnt;//정답보다 크다면 정답 갱신
		}
		cnt = 1;
		for (int j = 1; j < n; j++) {
			if (a[j][i] == a[j - 1][i]) {//아래와 같은지(같은 열에 대해서)
				cnt += 1;//같으면 세주고
			}
			else {
				cnt = 1;//아니면 초기화
			}
			if (ans < cnt) ans = cnt;//정답보다 크다면 정답 갱신.
		}
	}
	return ans;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	//vector<string> a(n);

	//for (int i = 0; i < n; i++) {
	//	cin >> a[i];
	//}//사탕의 색깔 저장 완료.

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> a[i][j];
		}
	}

	int ans = 0;

	for (int i = 0; i < n; i++) {//(i,j)에 대해서 오른쪽,아래를 비교하기로함.
		for (int j = 0; j < n; j++) {
			if (j + 1 < n) {//오른쪽
				swap(a[i][j], a[i][j + 1]);//바꾸고
				int temp = check(a);//바꾼걸로 인접한 같은색깔 캔디 최댓값 구해보고
				if (ans < temp) ans = temp;//ans보다 크면 바꾸고
				swap(a[i][j], a[i][j + 1]);//원상태로 돌려준다.(이거 없으면 문제가 꼬임)
										   //꼭 원상태로 돌려줘야한다.
			}
			if (i + 1 < n) {//아래.
				swap(a[i][j], a[i + 1][j]);
				int temp = check(a);
				if (ans < temp) ans = temp;
				swap(a[i][j], a[i + 1][j]);
			}
		}
		//swap으로 인접한 두칸(행끼리 N번 열끼리 N번) 바꾸고
		//임시변수 temp에 check 함수를 돌림
		//check함수는 해당 vector를 처음부터 끝까지 오른쪽과 아래를 비교해서 같은게 최대
		//몇개나 있는지 return해주는 함수.
		//고로,행과 열 모든칸마다 양쪽을 swap바꿔보고 인접한 색깔이 최대 몇갠지 확인한다.
		//n^2개를 n^2번 확인한다 -> n^4. n이 50까지라 할 수 있는 무식한 계산법.	
		
	}
	cout << ans << endl;
	return 0;
}
