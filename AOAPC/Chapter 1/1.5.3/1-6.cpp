// 1-6 triangle
#include <iostream>
#include <cmath>

int main() {
	int a, b, c;
	
	scanf("%d %d %d", &a, &b, &c);
	
	if (a + b > c && b + c > a && a + c > b) {
		if (pow(a, 2) + pow(b, 2) == pow(c, 2)) {
			printf("yes");
		} else {
			printf("no");
		}
	} else {
		printf("not a triangle");
	}
} 
