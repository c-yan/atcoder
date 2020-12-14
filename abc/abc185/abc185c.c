#include <stdio.h>

long long gcd(long long x, long long y) {
    long long t;

    if (x < y) {
        t = x;
        x = y;
        y = t;
    }

  	while (y > 0) {
        t = x;
        x = y;
        y = t % y;
    }
    return x;
}

int main() {
    int L;
    long long d = 39916800; // 11!
    long long result = 1;
    long long t;

    scanf("%d", &L);

    for (int i = 0; i < 11; i++) {
        t = gcd(L - 1 - i, d);
        result *= (L - 1 - i) / t;
        d /= t;
    }

    printf("%lld", result);
}
