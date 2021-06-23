#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int minMax[1000001] = { 0 };

int main(void) {
	int num;
	scanf("%d", &num);
	
	int n;
	for (int i = 0; i < num; i++) {	
		n = 0;
		scanf("%d", &n);
		minMax[i] = n;
	}

	int min = minMax[0];
	int max = minMax[0];
	for (int i = 0; i < num-1; i++) {
		if (min < minMax[i + 1]) min = min;
		else min = minMax[i + 1];
	}
	for (int i = 0; i < num-1; i++) {
		if (max < minMax[i + 1]) max = minMax[i + 1];
		else max = max;
	}
	printf("%d %d\n", min, max);
}
