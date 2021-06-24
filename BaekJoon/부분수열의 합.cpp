#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
1182 부분수열의 합 by bitmask.

n개로 이루어진 수열의 모든 부분수열의 갯수:2^n개.(n개에 대해 있고 없고 모두 판별
할 수 있으니까)

10110 -> {4,2,1}

n=0~ 2^n -1까지 다 살펴보면됨
진수를 하나씩 올리는건 i<<n로 조건문을 두면 2^n-1까지 탐색 가능.

*/

int a[20];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, s;
	cin >> n >> s;
		
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	int ans = 0;
	//공집합 제외.

	/*
	1~2^n-1까지
	i하나당 j는 0~n까지 돌면서 i랑 1<<j한 값이 같으면 sum에 a[j]를 더해주고
	sum이 s랑 같으면 ans에 1를 추가해줌.

	outer for문은 00000~11111까지 모두 조사하기위함.
	여기서 outer for문의 숫자(인덱스)가 곧 값이 되는게 아니라,
	-7 -3 -2 5 8 로 위에 입력받았으면
	1=-7
	10=-3
	110=-2
	1110=5
	11110=8로 나타냄.
	inner for문은 outer for문에 i값과 j를 비교해주기 위함
	그래서
	01110의 경우
	inner for문에서 모두 검사하니까 1로 표기된 index 3개를 sum+=a[index]로 한다.
	그래서 00000~11111까지 모든 수에 대해 index선택 여부에따라 입력받은 배열 a의 값을 sum에 더해
	sum이 목표한 s와 같은경우에 정답에 1을 추가해주는 형태.
	*/
	for (int i = 1; i < (1 << n); i++) {
		//i=1부터 2^n보다 작을때까지.
		//모든 부분수열을 돌 수 있는 for문.
		int sum = 0;
		for (int j = 0; j < n; j++) {//각각의 k번째 수가 포함되어있는지 확인
			if (i & (1 << j)) {//i랑 2^j를 &했을때 수가 있다면
				sum += a[j];//해당 수를 더함.
			}
		}//합을 구하는 코드


		if (sum == s) {//for문에서 구한 합이 s와 같으면
			ans += 1;//정답 1개 추가.
		}
	}
	cout << ans << endl;
}
