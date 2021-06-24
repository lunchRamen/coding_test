#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

/*
다음 순열

1~N까지 수로 이루어진 순열.

첫째줄에 N을 입력하고
둘째줄에 N자릿수 순열 입력	

->입력한 순열의 다음 순열 출력.
입력한 순열이 마지막 순열이라면 -1 출력.
*/

bool next_permutation(int* a, int n) {
	int i = n - 1;
	//i를 n-1(순열 맨 끝부분)으로 설정
	while (i > 0 && a[i - 1] >= a[i]) i -= 1;
	//i가 0보다 크고 이전숫자(i-1)가 현재 i번째 숫자보다 크면 왼쪽으로 한칸씩 이동. 아니면 냅둠.
	//->내림차순으로 진행되다가 아닌 순간(오름차순인 순간)이 순서를 바꿔야 하는 떄라서.
	if (i <= 0) return false;//i<=0은 위에 i-=1을 하면서 이미 모두 내림차순인 순열의 경우 다 -1씩해서 0이 되니까
							 //가장 마지막 순열의 경우 false를 return한다.
	int j = n - 1;//j도 n-1로 설정.
	while (a[j] <= a[i - 1]) j -= 1;//a[j](a배열의 n-1번째)가 a[i-1]보다 작을때까지 j를 -1씩
	//i번째에서 오름차순으로 바뀌었다? i-1번째의 마지막 수열이다. -> i-1번째 수를 다른 수로 바꿔서
	//첫 순열로 시작하게 만들어야 한다. 이때 i-1번째 수와 바꿀수는 i~n-1까지 수 중에 큰수 중 가장 작은 수와 바꾼다.
	//이때 큰수중 가장 작은 수를 정해주는 역할. j가 더 작은 경우는 j를 왼쪽으로 한칸 옮긴다.
	swap(a[i - 1], a[j]);//

	j = n - 1;
	while (i < j) {
		swap(a[i], a[j]);
		i += 1;
		j -= 1;
	}
	return true;
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n;
	cin >> n;
	int *a = new int[n];
	vector<int> b(n);
	for (int i = 0; i < n; i++) cin >> a[i];

	bool t=next_permutation(a, n);
	if (t) {
		for (int i = 0; i < n; i++) {
			cout << a[i] << ' ';
		}
	}
	else cout << -1;
	cout << '\n';
	//bool t2 = next_permutation(b, n);

}
