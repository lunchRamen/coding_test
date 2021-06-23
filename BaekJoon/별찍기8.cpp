#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

/*
별찍기 8.
1 2 3 ... n n-1 n-2...1 이렇게 별찍히게끔.

1. 1~n n-1~1로 루프를 두번 돌림.
2.inner for는 별찍기 띄어쓰기 띄어쓰기 별찍기 총 4개의 for문 존재.
3.1~n에서의 for문 조건문과 n-1~1에서의 조건문은 다름.
4.inner for는 무조건 i를 따라감.
5.두번째 loop(n-1 ~ 1) 돌릴때는 띄어쓰기가 1~n-1개 생성된다고 생각해야함.
*/
int main(void) {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		for (int j = n; j > i; j--) {
			printf(" ");
		}
		for (int j = n; j > i; j--) {
			printf(" ");
		}
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}//1~5까지

	for (int i = n-1; i >= 1; i--) {
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		for (int j = n - 1; j >= i; j--) {
			printf(" ");
		}
		for (int j = n - 1; j >= i; j--) {
			printf(" ");
		}
		for (int j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}//4~1까지

}
