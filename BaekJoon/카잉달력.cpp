#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
카잉달력
1476번 같은경우 지구 해 달 3개의 변수로
1년이 바뀐다면
이건 x y 두개로 바뀌는데
범위가 각각 4만이 최대라
brute force를 하면 시간초과가 뜸.
->하나를 기준 잡고 나머지 하나만 돌리면 됨.

M N x y 를 입력받고

x y에 해당하는 년도가 되려면 몇년이 필요한지 출력
만약 x y에 해당하는 년도가 될 수 없는 년도라면 -1을 출력.
*/
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;

	int m, n, x, y;
	for (int i = 0; i < t; i++) {
		cin >> m >> n >> x >>y;
		y -= 1;
		x -= 1;
		//나머지(mod)연산 쓰려고 -1씩을 해줌.
		//왜 -1씩 해줘야하는가?
		//그냥 mod연산을하면 m이나 n의 배수에서 0이 되어버림. 이걸 방지해주기 위해서.
		//m,n에서 -1을 하는게 아니라 x,y에서 -1을 하는 이유는
		//m,n은 mod연산을 할 mod수라서 변경시키면 안되고
		//x,y에서 -1씩을 하면 (x=3,y=2일때)
		//원래대로라면 x=5 y=4가 되면 (0,4)가 되지만
		//둘다 -1해주면 (4,3)이 되고 여기서 다시 1씩 더해주면 (5,4)이 돼서 원래 형태가 안무너짐.



		//->밑에 ok는 x와 y에 해당되는 년도를 찾았다는 거고 못찾았으면 -1을 return해주기
		//위한 변수고 밑에 for문은 k를 x로 잡고 k가 n*m보다 작을때까지 k를 m씩 증가시켜준다.
		//->n*m에 대한 전수조사를 하는데, m을 고정시킬거니까 n번만큼만 조사하면 돼서
		//시간복잡도는 O(N)이 된다.


		//m씩 증가시켜준다 -> x값을 고정시킨다.
		//그리고 k%n이 y이면 k+1를 출력하고 ok를 true로 바꿔주고 끝냄.
		//(1,1)에서 서로 1씩 똑같이 증가되니까 변수를 k하나로 놓고
		//k만 m씩 증가시켜서 x를 고정시키고 k%n이 y가 될때 출력하면 된다.
		bool ok = false;
		for (int k = x; k < (n * m); k += m) {
			if (k % n == y) {
				cout << k + 1 << endl;//k+1해줘야 mod연산을 위해 x-1 y-1해준거에서 원래대로 돌아옴.
				ok = true;
				break;
			}
		}
		if (!ok) {
			//ok가 false로 설정했는데
			//!ok=true가 돼서 -1 출력.
			cout << -1 << endl;
		}
	}
}

