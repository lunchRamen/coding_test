#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

/*
별찍기 1과 다른점
입력받은 숫자 내에서 오르쪽부터 1~n까지 출력되게끔
-> 이중 for문에서 inner for문에 for문을 2개 씀으로써
첫번째 for문:n-i만큼 띄어쓰기
두번째 for문:원래 별찍기 1에서 쓴 for문
으로 나눠 생각해줘야한다.
*/
int main(void) {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = n; j > i; j--) {
			printf(" ");
		}
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
}
