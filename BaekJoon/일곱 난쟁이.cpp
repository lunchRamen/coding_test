#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
일곱 난쟁이

9명중 7명의 합이 100이 되게끔.

9명중 7명을 골라라 =9명중 2명을 빼라.(조합)
*/

int a[10];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> a[i];
		sum += a[i];
	}//난쟁이 키 입력 완료

	sort(a, a + 9);
	for (int i = 0; i < 9; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - a[i] - a[j] == 100) {
				for (int k = 0; k < 9; k++) {
					if (i==k || j == k) continue;
					cout << a[k] << '\n';
				}
				//하나 출력했으니까 return 0으로 종료해야됨. 안쓰면 100이되는 조건 계속 출력함.
				return 0;
			}
		}
	}
	//brute force다보니까 for문을 많이 씀(전수조사 해야됨)
	//0~8까지 돌고, 1~8까지 돌면서 난쟁이 둘씩 뺐을때 합이 100이되면 
	//난쟁이들을 다 출력해준다(빼야되는 난쟁이들 2명 제외하고)
	//조건문에서 k==i k==j가 아닌 i==k j==k인 이유는
	//증감되는 조건변수가 k이기 때문이다. 고정된 한 값에 k를 넣어서 비교해보는거니까.

}
