#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
이름(영어) 국 영 수

국어:감소
국어 동일:영어 증가
국 영 동일:수학 감소
모든 점수 동일:이름 사전순 증가
*/

typedef struct student {
	string name;
	int kor;
	int eng;
	int math;
}student;

bool compare(student a,student b) {
	if (a.kor > b.kor) return a.kor > b.kor;
	else if (a.kor == b.kor) {
		if (a.eng < b.eng) return a.eng < b.eng;
		else if (a.eng == b.eng) {
			if (a.math > b.math) return a.math > b.math;
			else if (a.math == b.math) {
				if (a.name < b.name) return a.name < b.name;
			}
		}
	}
	return 0;
}
//모든 조건이 안맞았을때는 false를 return 해줘야 에러처리라도 해준다. void형이 아닌 경우
//조건문에 맞게 return해주는게 아니라 모든 조건문이 아닌경우의 return문도 생각해줘야한다.

int main() {
	int n;
	cin >> n;

	vector<student> s(n);

	for (int i = 0; i < n; i++) {
		cin >> s[i].name >> s[i].kor >> s[i].eng >> s[i].math;
	}

	sort(s.begin(), s.end(), compare);

	for (int i = 0; i < n; i++) cout << s[i].name << "\n";

}
