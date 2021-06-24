#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
날짜 계산.

E(earth) S(sun) M(moon)을 이용해서 날짜를 계산하는 곳.
E는 1~15 S는 1~28 M은 1~19까지 입력 받을수 있음.

우리의 1년(365일) = 1 1 1
1년이 지날때마다 셋다 1씩 증가.해당 행성의 범위가 넘어가는 경우 1로 초기화
ex) 15 15 15까지는 가능한데 1년이 지나면 1 16 16 이 된다.

15*28*19= 7980
처리할 수가 적으니 brute force로 푼다.
*/

int MAX = 7980;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int e, s, m;
	cin >> e>> s>> m;

	int cnt = 1;

	int earth = 1; int sun = 1; int moon = 1;
	//cnt++;
	//cout << cnt << endl;
	while (1) {//입력받은 지구 해 달과 같아야 탈출 가능
		if (e == earth && s == sun && m == moon) {
			cout << cnt << endl;
			break;
		}
		earth++;
		sun++;
		moon++;
		if (earth == 16) earth = 1;
		if (sun == 29) sun = 1;
		if (moon == 20) moon = 1;

		//if (e != earth) {
		//	if (earth == 16) earth = 1;	
		//	else earth++;
		//}
		//if (s != sun) {
		//	if (sun == 29) sun = 1;
		//	else sun++;
		//}
		//if (m != moon) {
		//	if (moon == 20) moon = 1;
		//	else moon++;
		//}
		cnt++;
	}


	//mod연산으로도 풀 수 있음.
	//모든 e s m 에서 e-=1 s-=1 m-=1해놓고
	//for(int i=0;;i++){
	//if(i%15==e && i%28==s && i%19==m) cout<<i+1<<endl; break;하면됨.
	//cout << cnt << endl;

}
