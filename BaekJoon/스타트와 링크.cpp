#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>

using namespace std;

//백트랙킹:의미없는 brute force를 제외한 brute force
	

/*
14889 스타트링크
N입력(4~20) 주어짐.
둘째줄부터 N개의 줄에 S가 주어진다.
각 줄은 N개의 수로 이루어져있고 i번줄의 j번째수=S(i,j)
S(i,i)는 항상 0. 나머지는 1~100.

N명을 N/2명씩 두팀으로 나눈다.(n<=20)
두 팀의 능력치를 구한 다음, 차이의 최소값을 구하는 문제

한 사람마다 두팀 중 하나 선택.
-> 2^n 시간복잡도.


재귀로 풀어야된다

1.정답이 되는 경우
2.정답이 안되는 경우
3.다음 재귀호출.


go(index,first,second)
->index번째 사람을 어떤팀에 넣을지
정답을 찾은 경우:index==n
다음 경우:
첫번째팀:go(index,index,second)
두번째팀:go(index,first,index)

*/

//int a[20][20];
//int n;
//int solve(int index,vector<int> &first,vector<int> &second) {
//	if (index == n) {//모두 팀에 추가했으면
//		if (first.size() != n / 2) return -1;
//		if (second.size() != n / 2) return -1;
//		//각 팀이 n/2가 맞는지 확인하고 아니면 -1로 예외처리.
//
//		int t1 = 0;//1번팀 능력치
//		int t2 = 0;//2번팀 능력치
//		for (int i = 0; i < n / 2; i++) {
//			for (int j = 0; i < n / 2; j++) {
//				if (i == j) continue;
//				t1 += a[first[i]][first[j]];
//				t2 += a[second[i]][second[j]];
//			}
//		}//모든 순서쌍에 대해서 팀의 능력치를 구함.
//		int diff = t1 - t2;
//		if (diff < 0) diff = -diff;
//		return diff;
//	}
//	//다음 재귀함수 호출.
//	int ans = -1;
//	//index번째 사람을 1번팀에 넣는 경우
//	first.push_back(index);
//	//인덱스를 first에 넣고
//	int t1 = solve(index + 1, first, second);
//	//index+1해서 재귀를 돌림.
//	if (ans == -1 || (t1 != -1 && ans > t1)) {
//		ans = t1;
//	}
//	first.pop_back();
//	//index번째 사람을 2번팀에 넣는 경우.
//	second.push_back(index);
//	int t2 = solve(index + 1, first, second);
//	if (ans == -1 || (t2 != -1 && ans > t2)) {
//		ans = t2;
//	}
//	second.pop_back();
//	return ans;
//}
//
///*
//ex_ 8명일때
//1 2 3 4 5 6 7 8(사람번호)
//1 2 1 1 1 1(팀선택) 일때
//1번팀이 5명이 되었기때문에,더이상 호출이 의미가 없음.
//->불가능한 경우:first>n/2 || second>n/2.
//이런 불가능한 경우를 예외처리하는게 백트랙킹.
//*/
//
//int main() {
//	ios::sync_with_stdio(false);
//	cin.tie(0);
//
//	cin >> n;
//
//	for (int i = 0; i < n; i++) {
//		for (int j = 0; j < n; j++) {
//			cin >> a[i][j];
//		}
//	}
//
//	vector<int> first, second;
//	cout << solve(0, first, second) << '\n';
//
//}
int s[20][20];
int n;
int go(int index, vector<int>& first, vector<int>& second) {
    if (index == n) {
        if (first.size() != n / 2) return -1;
        if (second.size() != n / 2) return -1;
        int t1 = 0;
        int t2 = 0;
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n / 2; j++) {
                if (i == j) continue;
                t1 += s[first[i]][first[j]];
                t2 += s[second[i]][second[j]];
            }
        }
        int diff = t1 - t2;
        if (diff < 0) diff = -diff;
        return diff;
    }
    int ans = -1;
    first.push_back(index);
    int t1 = go(index + 1, first, second);
    if (ans == -1 || (t1 != -1 && ans > t1)) {
        ans = t1;
    }
    first.pop_back();
    second.push_back(index);
    int t2 = go(index + 1, first, second);
    if (ans == -1 || (t2 != -1 && ans > t2)) {
        ans = t2;
    }
    second.pop_back();
    return ans;
}
int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> s[i][j];
        }
    }
    vector<int> first, second;
    cout << go(0, first, second) << '\n';
}
