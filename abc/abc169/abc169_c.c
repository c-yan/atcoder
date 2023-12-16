#include <stdio.h>

int main() {
	long long A;
	double B;

	scanf("%lld %lf", &A, &B);
	printf("%lld\n", A * (int)(B * 100 + 0.5) / 100);
}
