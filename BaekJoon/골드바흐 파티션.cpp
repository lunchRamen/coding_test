#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;
vector<bool> visit(1000001);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	vector<int> prime;
	
	int pn = 0;//소수를 저장할때 인덱스 위치 가르키는 용도.(소수의 갯수 count)

	int X = 1000000;
	for (int i = 2; i <= X; i++) {
		if (visit[i] == false) {//지워지지 않았으면
			prime[pn++]=i;//i는 소수여서 0번째 index에 저장하고 
						  //pn++(다음 인덱스에 저장하기 위해서)
			for (int j = i + i; j <= X; j += i) {
				visit[j] = true;
				//i*i부터 조사하면 되는데 i+i로 하는 이유?
				//제한 숫자가 클때, j를 제곱으로 두면 overflow발생.
			}
		}
	}
	//에라토스테네스의 체 코드
	//소수 저장 배열(prime)
	//소수 삭제 여부 배열(visit)
	//pn=소수의 갯수 저장 변수.
	//결론적으로 prime배열엔 2~X까지 수 중 소수만 저장됨.

	int T;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		int n;
		cin >> n;
		int ans = 0;
		for (int j = 0; j < prime.size();j++) {
			if (n - prime[j] >= 2 && prime[j] <= n - prime[j]) {
				//A+B=N인 경우를 찾는데 A를 prime[j]로 놨으니 B는 N-prime[j]로 놔야 한다.
				//고로 이 조건은 B가 2보다 크고 A가 B보다 작은 조건을 검사하는 문장.
				//두 조건을 검사하는 이유는 앞의 경우 밑에 visit검사문에서
				//n-a가 음수가 나오게되면 visit의 배열 범위를 벗어나기 때문에
				//소수의 조건중 하나인 2보다 크거나 같다를 건거고
				//두번째 조건은 1 2 // 2 1 처럼 순서는 다르지만 같은 경우를 걸러주는 조건
				//A가 B보다 작거나 같은경우만 따지기 때문에 순서를 따져준다.
				if (visit[n - prime[j]] == false) {
					ans += 1;
				}
			}
			else {
				break;
			}
		}
		//for (int j = 0; j < prime.size();j++) {
		//	if (visit[n - prime[j] == false]) ans++;
		//	else break;
		//}

		/*for (int i = 2; i <= n; i++) {
			이 경우 A를 i로 뒀기때문에 n-i가 B가 되고 i 가 소수인지 n-i가 소수인지
			i<=n-i(A와 B의 순서가 다른지) 걸러주는 조건을 만들면 같게 만들수 있다.
		}*/
		cout << ans << '\n';
	}
	
}
