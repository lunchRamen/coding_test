#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int daysOfMonth[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
int main(void) {
	int mon, day;
	scanf("%d %d", &mon, &day);
	int total_day = 0;

	for (int i = 1; i < mon; i++) {
		total_day += daysOfMonth[i];
	}
	total_day += day;

	switch (total_day % 7) {
	case 0:
		printf("SUN\n");
		break;
	case 1:
		printf("MON\n");
		break;
	case 2:
		printf("TUE\n");
		break;
	case 3:
		printf("WED\n");
		break;
	case 4:
		printf("THR\n");
		break;
	case 5:
		printf("FRI\n");
		break;
	case 6:
		printf("SAT\n");
		break;
	}
	return 0;
}
